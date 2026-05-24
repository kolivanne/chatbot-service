from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    """
    Zentrale Konfiguration der Anwendung.

    Umgebungsvariablen werden aus der .env Datei geladen.
    """

    # Azure OpenAI Konfiguration
    azure_openai_endpoint: str = ""
    azure_openai_api_key: str = ""
    azure_openai_model: str = ""

    # steuert, welcher Provider genutzt wird
    llm_provider: str = Field(default="azure", alias="LLM_PROVIDER") 

    log_level: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()