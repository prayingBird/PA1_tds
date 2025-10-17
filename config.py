from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
import os
class Settings(BaseSettings):
    GEMINI_API_KEY: str
    GITHUB_TOKEN: str
    STUDENT_SECRET: str
    GITHUB_USERNAME: str
    
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )
    def __init__(self, **kwargs):
# Read from environment first (for Hugging Face Spaces)
# Then fall back to .env file (for local development)
        super().__init__(**kwargs)
@lru_cache()
def get_settings():
    return Settings()
