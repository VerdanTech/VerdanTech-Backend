# External Libraries
from litestar import Litestar
from litestar.datastructures import State

# VerdanTech Source
from src import exceptions, settings
from src.common.adapters.persistence.sqlalchemy import litestar_alchemy_client_lifespan

from .auth import jwt_auth
from .dependencies import svcs_plugin
from .exceptions import application_exception_handler
from .openapi import openapi_config
from .router import create_base_router


def create_app(alchemy_uri=settings.POSTGRES_URI) -> "Litestar":
    # VerdanTech Source
    from src.common.ops.processors import asgi_processor
    from src.user.ops import (
        commands as user_commands,
        events as user_events,
        queries as user_queries,
    )

    base_router = create_base_router()

    return Litestar(
        route_handlers=[base_router],
        lifespan=[litestar_alchemy_client_lifespan],
        plugins=[svcs_plugin],
        openapi_config=openapi_config,
        on_app_init=[jwt_auth.on_app_init],
        state=State({"alchemy_uri": alchemy_uri}),
        exception_handlers={
            exceptions.ApplicationException: application_exception_handler
        },
        debug=True,
    )