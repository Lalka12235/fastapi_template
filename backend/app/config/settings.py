from pydantic_settings import BaseSettings,SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    #SECRET_KEY: str

    @property
    def sync_db_url(self):
        return f'postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
    
    @property
    def async_db_url(self):
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
    
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / '.env',         # Указывает, что настройки будут загружаться из файла .env
        extra='ignore'           # Игнорировать дополнительные поля в .env, которых нет в классе Settings
    )

    #@property
    #def get_secret_key(self):
    #    return self.SECRET_KEY



settings = Settings()