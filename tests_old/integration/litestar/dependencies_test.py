# External Libraries
import pytest
from litestar.datastructures import State as LitestarGlobalState
from litestar.testing import AsyncTestClient
from litestar_svcs import SvcsPlugin
from sqlalchemy.ext.asyncio import AsyncSession as AsyncSession
from svcs import Container

# VerdanTech Source
from src.common.adapters.persistence.sqlalchemy.client import AlchemyClient
from src.common.interfaces.email import AbstractEmailClient
from src.common.interfaces.email import AbstractEmailEmitter
from src.user.interfaces.persistence.user.user import AbstractUserRepository
from src.common.interfaces.security.crypt.crypt import AbstractPasswordCrypt
from src.ops.user import controllers as user_ops

pytestmark = [pytest.mark.asgi]


@pytest.mark.skip
async def test_container(litestar_client: AsyncTestClient) -> None:
    """
    Ensure that the svcs Registry created on the Litestar global application
    state can successfully retrieve all required dependencies.

    Args:
        litestar_client (AsyncTestClient): litestar test client.
    """
    # Retrieve svcs registry from litestar
    svcs_plugin = litestar_client.app.plugins.get(SvcsPlugin)
    registry_state_key = svcs_plugin._config.registry_state_key
    registry = getattr(litestar_client.app.state, registry_state_key, None)
    assert registry is not None

    async with Container(registry=registry) as container:
        # Currently, Litestar global state is registered as a local
        # value in each route handler. Replicated here for consistency.
        state = getattr(litestar_client.app, "state")
        container.register_local_value(LitestarGlobalState, state)
        # ======================================
        # OPERATIONS CONTROLLERS
        # ======================================
        # User
        user_write_ops_controller = await container.aget(
            user_ops.UserWriteOpsController
        )
        assert user_write_ops_controller is not None

        # ======================================
        # SANITIZERS
        # ======================================

        # User
        user_sanitizer = await container.aget(UserSanitizer)
        assert user_sanitizer is not None

        # ======================================
        # PERSISTENCE
        # ======================================

        # Repository
        alchemy_client = await container.aget(AlchemyClient)
        assert alchemy_client is not None

        alchemy_transaction = await container.aget(AsyncSession)
        assert alchemy_transaction is not None

        # Repository
        user_repo = await container.aget_abstract(AbstractUserRepository)
        assert user_repo is not None

        # ======================================
        # QUEUE
        # ======================================

        # ======================================
        # EMAIL
        # ======================================

        # Client
        email_client = await container.aget_abstract(AbstractEmailClient)
        assert email_client is not None

        # Emitter
        email_emitter = await container.aget_abstract(AbstractEmailEmitter)
        assert email_emitter is not None

        # ======================================
        # SECURITY
        # ======================================

        password_crypt = await container.aget_abstract(AbstractPasswordCrypt)
        assert password_crypt is not None
