# Standard Library
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # External Libraries
    from litestar import Litestar


def create_app() -> "Litestar":
    # External Libraries
    from litestar import Litestar

    # VerdanTech Source
    from src.asgi.litestar.dependencies import svcs_plugin
    from src.asgi.litestar.lifecycle import lifecycle
    from src.asgi.litestar.router import create_base_router

    base_router = create_base_router()

    app = Litestar(
        route_handlers=[base_router], 
        #lifespan=lifecycle, 
        plugins=[svcs_plugin]
    )
    return app
