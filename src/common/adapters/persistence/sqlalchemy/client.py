# Standard Library
from dataclasses import dataclass

# External Libraries
from sqlalchemy.ext.asyncio import AsyncEngine

from .mapper import mapper_registry


@dataclass
class AlchemyClient:
    """Wrapper around SqlAlchemy database client objects"""

    engine: AsyncEngine

    async def init(self) -> None:
        """
        Initialize the SqlAlchemy database connection by
        creating table metadata on the engine
        """
        async with self.engine.begin() as connection:
            await connection.run_sync(mapper_registry.metadata.create_all)

    async def close(self) -> None:
        """
        Deinitialize the SqlAlchemy database connection
        by closing the engine's connection.
        """
        await self.engine.dispose()
