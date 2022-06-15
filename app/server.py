from fastapi import (
    FastAPI
)
from uvicorn import run

from .core.settings import settings

app = FastAPI(
    title=settings.project_title,
    description=settings.project_description,
    version=settings.project_version,
    docs_url=settings.project_docs_url
)


if __name__ == "__main__":
    run(
        settings.app,
        port=settings.port,
        log_level=settings.log_level,
        reload=settings.reload
    )
