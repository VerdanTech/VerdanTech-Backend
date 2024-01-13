# VerdanTech Source
from mocks.infra.persistence.repository.user_mock import MockUserRepository
from src.interfaces.persistence.user.repository import AbstractUserRepository

session_scoped_mock_user_repository = MockUserRepository()


async def provide_user_mock_repository() -> AbstractUserRepository:
    """Configure and provide a mocked user repository for testing on the session scope."""
    return session_scoped_mock_user_repository
