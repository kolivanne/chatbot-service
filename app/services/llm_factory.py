from app.core.config import settings
from app.services.azure_openai_service import AzureOpenAIService
from app.services.llm_service import LLMService

# Bedrock wird hier nur als Platzhalter gezeigt,
# um die Austauschbarkeit der Architektur zu verdeutlichen.
# Die echte Implementierung wäre später AWS SDK basiert.
from app.services.aws_bedrock_service import BedrockService


def get_llm_service() -> LLMService:
    """
    Factory zur Auswahl des passenden LLM Providers.

    Zweck:
    - zentrale Stelle für die Provider-Auswahl
    - ermöglicht Austausch ohne Änderungen im API Layer
    - Entscheidung basiert auf Konfiguration (.env)

    Unterstützte Provider:
    - azure  -> Azure OpenAI
    - bedrock -> AWS Bedrock (Platzhalter)
    """

    provider = settings.llm_provider.lower()

    if provider == "azure":
        return AzureOpenAIService()

    if provider == "bedrock":
        return BedrockService()

    raise ValueError(
        f"Unbekannter LLM Provider: {settings.llm_provider}. "
        f"Erlaubt sind: azure, bedrock"
    )