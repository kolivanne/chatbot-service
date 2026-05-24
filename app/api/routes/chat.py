from fastapi import APIRouter, Depends
import logging

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.llm_factory import get_llm_service
from app.services.llm_service import LLMService

router = APIRouter()

logger = logging.getLogger(__name__)

def get_service() -> LLMService:
    """
    FastAPI Dependency für den LLM Service.

    Wird von FastAPI automatisch aufgerufen und in den Endpoint injiziert.

    Hinweis:
    Depends sorgt dafür, dass die Abhängigkeit nicht manuell erstellt wird,
    sondern pro Request bereitgestellt werden kann.
    """
    return get_llm_service()

@router.post("/chat", response_model=ChatResponse)
# synchron, da aktuell keine echten I/O Calls (nur Mock-Logik) verwendet werden
def chat(
    request: ChatRequest,
    # Dependency Injection über FastAPI
    llm_service: LLMService = Depends(get_service)
    ):
    """
    Nimmt eine Chat-Nachricht entgegen und gibt eine LLM-Antwort zurück.
    """

    # spätere Erweiterung:
    # - Authentifizierung
    # - Rate Limiting
    # - session_id für Conversation Memory
    
    logger.info("Chat request erhalten")

    result = llm_service.generate_response(request.message)

    return ChatResponse(response=result)