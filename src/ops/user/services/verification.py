# VerdanTech Source
from src.domain import exceptions as domain_exceptions
from src.domain.user import User
from src.interfaces.email.emitter import AbstractEmailEmitter
from src.interfaces.persistence.user.repository import AbstractUserRepository
from src.ops import exceptions as ops_exceptions
from src.utils.key_generator import generate_unique_key


async def email_confirmation_create(
    user: User,
    email_address: str,
    key_length: int,
    user_repo: AbstractUserRepository,
    email_emitter: AbstractEmailEmitter,
) -> None:
    """
    Generate new email confirmation key, add a new email confirmation
    on the domain model, and emit the email confirmation email.

    Args:
        user (User): user to add a new confirmation on.
        address (str): email to add a new confirmation on.
        key_length (int): length of the confirmation key to generate,
            application setting.
        user_repo (AbstractUserRepository): user repository interface.
        email_emitter (AbstractEmailEmitter): email emitter interface.

    Returns:
        str: generated key.
    """
    key = await generate_unique_email_confirmation_key(
        length=key_length, user_repo=user_repo
    )
    user.email_confirmation_create(address=email_address, key=key)
    await email_emitter.emit_user_email_confirmation(
        email_address=email_address, username=user.username, key=key
    )


async def password_reset_create(
    user: User,
    email_address: str,
    key_length: int,
    user_repo: AbstractUserRepository,
    email_emitter: AbstractEmailEmitter,
) -> None:
    """
    Generate a new password reset confirmation key, and add a new
    password reset confirmation.

    Args:
        user (User): user to add a new confirmation on.
        key_length (int): application setting.
        user_repo (AbstractUserRepository): user repository interface.
        email_emitter (AbstractEmailEmitter): email emitter interface.
    """
    if user.id is None:
        raise domain_exceptions.EntityIntegrityException(
            "Password reset attempt on unpersisted User."
        )

    primary_email = user.primary_email
    if not email_address == primary_email.address:
        raise ops_exceptions.EntityNotFound(
            "The email address provided is not the user's primary email."
        )
    key = await _generate_unique_password_reset_key(
        length=key_length, user_repo=user_repo
    )
    user.password_reset_create(key=key)
    await email_emitter.emit_user_password_reset(
        email_address=email_address, username=user.username, user_id=user.id, key=key
    )


async def generate_unique_email_confirmation_key(
    length: int, user_repo: AbstractUserRepository
) -> str:
    """
    Generate a unique email confirmation key.

    Args:
        length (int): length of the key to generate.
        user_repo (AbstractUserRepository): user repository.

    Returns:
        str: the unique key.
    """
    return await generate_unique_key(
        length=length,
        repo=user_repo,
        existence_method_name="email_confirmation_key_exists",
        existence_method_argument_name="key",
    )


async def _generate_unique_password_reset_key(
    length: int, user_repo: AbstractUserRepository
) -> str:
    """
    Generate a unique password reset key.

    Args:
        length (int): length of the key to generate.
        user_repo (AbstractUserRepository): user repository.

    Returns:
        str: the unique key.
    """
    return await generate_unique_key(
        length=length,
        repo=user_repo,
        existence_method_name="password_reset_confirmation_key_exists",
        existence_method_argument_name="key",
    )
