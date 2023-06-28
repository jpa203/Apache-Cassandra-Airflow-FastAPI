from functools import lru_cache # caching for in memory settings 
import os
from pydantic import BaseSettings, Field

if os.getenv("CQLENG_ALLOW_SCHEMA_MANAGEMENT") is None:
    os.environ["CQLENG_ALLOW_SCHEMA_MANAGEMENT"] = "1"

class Settings(BaseSettings):
    name: str = Field(..., env = "PROJ_NAME")
    db_client_id: str = Field(..., env = 'ASTRA_DB_CLIENT_ID') # path to .env file
    db_client_secret: str = Field(..., env = 'ASTRA_DB_CLIENT_SECRET')
    redis_url: str = Field(..., env = 'REDIS_URL')

    class Config:  # Config class is a special class provided by Pydantic - allows you to configure various settings and behaviours in the model. 
        env_file = '.env'


@lru_cache # cache 
def get_settings():
    return Settings()