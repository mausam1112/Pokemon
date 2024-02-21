from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='app/config/.env', env_file_encoding='utf-8', extra='allow')


settings = Settings()
