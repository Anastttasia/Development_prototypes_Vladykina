from pydantic_settings import BaseSettings, SettingsConfigDict

# PG_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/postgres"

class ApiConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )
    pg_user: str = "auto"
    pg_password: str = "123"
    pg_host: str = "my_host"
    pg_port: int = 5432

    app_host: str = "my_host"
    app_port: int = 8080

    redis_url: str = ""

settings = ApiConfig()

if __name__ == "__main__":

    print(settings)