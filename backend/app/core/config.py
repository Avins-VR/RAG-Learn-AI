from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    GROQ_API_KEY: str = ""
    ALLOWED_ORIGINS: str = "http://localhost:5173,http://localhost:3000,https://rag-learn-ai.netlify.app"

    class Config:
        env_file = ".env"

settings = Settings()