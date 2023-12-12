# External Libraries
from litestar import Controller, delete, patch, post
from litestar.di import Provide
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from svcs import Container

# VerdanTech Source
from src.asgi.litestar.exceptions import litestar_exception_map
from src.ops.user.schemas import write as write_schemas

from .. import routes, schemas, urls


class UserWriteApiController(Controller):
    """User write api controller"""

    path = urls.USER_WRITE_CONTROLLER_URL_BASE

    @post(
        name=routes.USER_CREATE_NAME,
        summary="User registration",
        description="Register a new user and send an email verification",
        tags=["users"],
        path=urls.USER_CREATE_URL,
        return_dto=schemas.UserSelfDetail,
    )
    async def user_create(
        self,
        data: write_schemas.UserCreateInput,
        svcs_container: Container,
    ) -> None:
        """
        Call the main user creation application operation.

        Args:
            data (UserCreateInput): input DTO.
            svcs_container (Container): svcs service
                locator container.

        Returns:
            UserSelfDetail: user self-reference DTO.
        """
        pass
        # async with litestar_exception_map:
        # user = await user_write_operations.create(
        # data=data,
        # user_sanitizer=user_sanitizer,
        # password_crypt=password_crypt,
        # email_emitter=email_emitter,
        # )
        # return user

    """
    @patch(path=urls.USER_CHANGE_USERNAME_URL)
    async def user_change_username() -> None:
        pass

    @patch(path=urls.USER_CHANGE_PASSWORD_URL)
    async def user_change_password() -> None:
        pass

    @post(path=urls.USER_EMAIL_CHANGE_REQUEST_URL)
    async def user_email_change_request() -> None:
        pass

    @delete(path=urls.USER_DELETE_URL)
    async def user_delete() -> None:
        pass
    """
