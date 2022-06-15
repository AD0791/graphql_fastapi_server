from pydantic import (
    BaseSettings,
    Field
)


class Settings(BaseSettings):
    project_title: str = "GraphQL-Server"
    project_description: str = "A graphql powerered services for learning purposes"
    project_version: str = "v0.0.1"
    project_docs_url: str = "/"

    app: str = "server:app"
    port: int = Field(..., env='PORT')
    log_level: str = "info"
    reload: bool = True

    class Config:
        env_prefix = ""
        case_sensitive = False
        env_file = "../.env"
        env_file_encoding = "utf-8"


settings = Settings()
