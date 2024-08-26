# Standard Library
import uuid
from datetime import datetime

# External Libraries
from svcs import Container

# VerdanTech Source
from src import exceptions, settings
from src.common.domain import Ref
from src.common.interfaces.persistence.uow import AbstractUow
from src.common.interfaces.security.passwords import AbstractPasswordCrypt
from src.common.ops.queries import Query, QueryResult, RefSchema, query_result_transform
from src.cultivars.domain import Cultivar, CultivarAttributeSet, CultivarCollection
from src.garden.domain.commands import GardenKey
from src.user.domain import User

# ======================================
# QueryResults
# ======================================


@query_result_transform
class CultivarSchema(QueryResult[Cultivar]):
    id: uuid.UUID
    name: str
    key: str
    attributes: CultivarAttributeSet
    parent_id: uuid.UUID | None
    created_at: datetime


@query_result_transform
class CultivarCollectionPartialSchema(QueryResult[CultivarCollection]):
    id: uuid.UUID
    name: str
    key: str
    description: str
    tags: set[str]
    parent_ref: RefSchema | None
    user_ref: RefSchema | None
    garden_ref: RefSchema | None
    created_at: datetime


@query_result_transform
class CultivarCollectionFullSchema(QueryResult[CultivarCollection]):
    id: uuid.UUID
    name: str
    key: str
    description: str | None
    tags: set[str]
    parent_ref: RefSchema | None
    user_ref: RefSchema | None
    garden_ref: RefSchema | None
    created_at: datetime
    cultivars: set[CultivarSchema]


@query_result_transform
class CultivarGetByGardenResult(QueryResult[None]):
    collections: set[CultivarCollectionPartialSchema]
    active_collection: Ref[CultivarCollection]


@query_result_transform
class CultivarGetByClientResult(QueryResult[None]):
    collections: set[CultivarCollectionPartialSchema]


# ======================================
# Queries
# ======================================


class CultivarGetByGardenQuery(Query):
    garden_key: GardenKey


class CultivarGetByIdsQuery(Query):
    cultivar_ids: list[uuid.UUID]


# ======================================
# Query handlers
# ======================================


async def get_by_garden(
    query: CultivarGetByGardenQuery, svcs_container: Container, client: User | None
) -> CultivarGetByGardenResult:
    """
    Retrieves the cultivar collections that
    are associated with a garden.

    Args:
        query (CultivarGetByGardenQuery): the query.
        svcs_container (Container): service locator.
        client (User): the client user.

    Returns:
        CultivarGetByGardenResult: references to the
            cultivar collections associated with the garden.
    """
    ...


async def get_by_client(
    svcs_container: Container, client: User | None
) -> CultivarGetByClientResult:
    """
    Retrieves the cultivar collections that
    are associated with the client.

    Returns:
        CultivarGetByClientResult: references to the
            cultivar collections associated with the gardens.
    """
    ...


async def get_by_ids(
    query: CultivarGetByIdsQuery, svcs_container: Container, client: User | None
) -> list[CultivarCollectionFullSchema]:
    """
    Retrieves the cultivars by their ids.

    Args:
        query (CultivarGetByIdsQuery): the query.
        svcs_container (Container): service locator.
        client (User): the client user.

    Returns:
        set[Cultivar]: the cultivars.
    """
    ...