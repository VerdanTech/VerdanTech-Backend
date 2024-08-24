# External Libraries
from litestar import Controller, get, Request
from litestar.datastructures import State
from litestar.params import Dependency
from svcs import Container

# VerdanTech Source
from src.common.entrypoints.litestar.auth.guard import requires_account
from src.cultivars.ops import queries

class CultivarQueryController(Controller):
    """Cultivar read operations controller"""

    path = "query"
    tags = ["cultivars"]

    @get(
        path="get_by_garden",
        summary="Get cultivar collections from a garden.",
        description="Retrieves the cultivar collections associated with this garden.",
        operation_id=queries.CultivarGetByGardenQuery.to_operation_id(),
    )
    async def get_by_garden(
        self,
        garden_key: str,
        request: Request,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> queries.CultivarGetByGardenResult:
        """
        Calls the garden associated cultivar collections query.

        Args:
            garden_key (str): the key of the garden to request.
            request (Request): Litestar request object.
            state (State): Litestar global app state.
            request (Request): Litestar http request object.
            svcs_container (Container): service locator.

        Returns:
            CultivarGetByGardenResult: references to the cultivar collections.
        """
        svcs_container.register_local_value(State, state)
        result = await queries.get_by_garden(query=queries.CultivarGetByGardenQuery(garden_key=garden_key), svcs_container=svcs_container, client=request.user)
        return result
    
    @get(
        path="get_by_garden",
        summary="Get cultivar collections from a garden.",
        description="Retrieves the cultivar collections associated with this garden.",
        operation_id=queries.CultivarGetByGardenQuery.to_operation_id(),
        guards=[requires_account]
    )
    async def get_by_client(
        self,
        request: Request,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> queries.CultivarGetByClientResult:
        """
        Calls the client associated cultivar collections query.

        Args:
            request (Request): Litestar request object.
            state (State): Litestar global app state.
            request (Request): Litestar http request object.
            svcs_container (Container): service locator.

        Returns:
            CultivarGetByClientResult: references to the 
                cultivar collections.
        """
        svcs_container.register_local_value(State, state)
        result = await queries.get_by_client(svcs_container=svcs_container, client=request.user)
        return result