# Standard Library
import uuid
from datetime import datetime

# External Libraries
from svcs import Container

# VerdanTech Source
from src import exceptions, settings
from src.common.interfaces.persistence.uow import AbstractUow
from src.common.interfaces.security.passwords import AbstractPasswordCrypt
from src.common.ops.queries import Query, QueryResult, query_result_transform
from src.user.domain import Email, User
from src.user.domain.commands import EmailStr, Password, Username

# ======================================
# QueryResults
# ======================================


@query_result_transform
class UserEmailSchema(QueryResult[Email]):
    """Schema for returning a detailed representation of an Email."""

    address: str
    primary: bool
    verified: bool


@query_result_transform
class UserFullSchema(QueryResult[User]):
    """
    Schema for returning a detailed representation of a User
    to that User.
    """

    id: uuid.UUID
    username: str
    emails: list[UserEmailSchema]
    is_superuser: bool
    created_at: datetime


@query_result_transform
class UserPublicSchema(QueryResult[User]):
    """
    Schema for returning a detailed representation of a User,
    to other Users.
    """

    id: uuid.UUID
    username: str


@query_result_transform
class UserPasswordVerificationResult(QueryResult[None]):
    """Schema for returning the result of a password verification query."""

    verified: bool
    email_verification_required: bool = False
    user_id: uuid.UUID | None = None


# ======================================
# Queries
# ======================================


class UserPasswordVerificationQuery(Query):
    """
    Verifies the password of a user.
    """

    email_address: EmailStr
    password: Password


class UserPublicProfilesQuery(Query):
    """
    Retrieves public profiles for a list of user IDs.
    """

    user_ids: list[uuid.UUID]


class UsernameExistsQuery(Query):
    """
    Returns whether a username exists.
    """

    username: str


class UserSearchQuery(Query):
    """
    Retrieves public profiles with usernames similar to the query.
    """

    username: Username


# ======================================
# Query handlers
# ======================================


async def verify_password(
    query: UserPasswordVerificationQuery, svcs_container: Container
) -> UserPasswordVerificationResult:
    """
    Verifies the password of a user.

    Args:
        query (UserPasswordVerificationQuery): the query object.

    Returns:
        UserPasswordVerificationResult: indicates verified as true if the user can be authenticated,
            and if not, indicates whether an email confirmation is required.
    """
    uow, password_crypt = await svcs_container.aget_abstract(
        AbstractUow, AbstractPasswordCrypt
    )
    async with uow:
        user = await uow.repos.users.get_by_email_address(query.email_address)
        if user is None:
            raise exceptions.NotFoundError(
                field_errors=[("email_address", "The email does not exist")]
            )

    # Prohibit logging in if the user is not verified and verification is required
    if (
        not user.is_verified()
        and settings.EMAIL_CONFIRMATION
        == settings.EmailConfirmationOptions.REQUIRED_FOR_LOGIN
    ):
        return UserPasswordVerificationResult(
            verified=False, email_verification_required=True
        )

    password_verified = await user.verify_password(
        password=query.password.get_secret_value(), password_crypt=password_crypt
    )

    if password_verified:
        return UserPasswordVerificationResult(verified=True, user_id=user.id_or_error())
    else:
        return UserPasswordVerificationResult(verified=False)


async def public_profiles(
    query: UserPublicProfilesQuery,
    svcs_container: Container,
) -> list[UserPublicSchema]:
    """
    Returns a list of public profiles from a list of IDs.

    Args:
        query (ProfilesQuery): the query object.
        svcs_container (Container): service locator.

    Returns:
        list[UserPublicSchema]: the list of public profiles.
    """
    # Locate services
    uow = await svcs_container.aget_abstract(AbstractUow)

    async with uow:
        users = await uow.repos.users.get_by_ids(ids=query.user_ids)

    user_schemas = [UserPublicSchema.cast(user) for user in users]
    return user_schemas


async def client_profile(client: User | None) -> UserFullSchema:
    """
    Returns the full profile of the client user.

    Args:
        client (User): the client user.

    Returns:
        UserFullSchema: the full profile of the client user.
    """
    if client is None:
        raise exceptions.AuthenticationError(
            "Client set to non on an authenticated route."
        )
    return UserFullSchema.cast(client)


async def username_exists(
    query: UsernameExistsQuery, svcs_container: Container
) -> bool:
    """
    Returns whether a username exists.

    Args:
        query (UserSearchQuery): the query object.
        svcs_container (Container): service locator.

    Returns:
        True if the username exists.
    """
    ...


async def username_search(
    query: UserSearchQuery, svcs_container: Container
) -> list[UserPublicSchema]:
    """
    Returns a list of users with usernames that most closely match the query.

    Args:
        query (UserSearchQuery): the query object.
        svcs_container (Container): service locator.

    Returns:
        list[UserPublicSchema]: the list of public profiles.
    """
    ...
