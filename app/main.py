from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.core.config import get_settings
from app.core.logging import configure_logging


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""

    settings = get_settings()

    configure_logging()

    application = FastAPI(
        title=settings.app_name,
        description=(
            "A production-style multi-agent platform "
            "for automating software engineering workflows."
        ),
        version="0.1.0",
    )

    application.include_router(
        health_router,
        prefix="/api/v1",
        tags=["Health"],
    )

    return application


app = create_app()