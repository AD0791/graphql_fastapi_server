from fastapi import (
    FastAPI
)
from uvicorn import run

from core.settings import setting

app = FastAPI(
    title=setting.project_title,
    description=setting.project_description,
    version=setting.project_version,
    docs_url=setting.project_docs_url
)

if __name__ == "__main__":
    run(
        setting.app,
        port=setting.port,
        log_level=setting.log_level,
        reload=setting.reload
    )
