from fastapi import FastAPI

from app.api.routes.chat import router as chat_router
from app.api.routes.system import router as system_router
from app.core.logging_config import setup_logging


def create_app() -> FastAPI:
    """
    Application Factory für den FastAPI-Service.

    Bietet einen zentralen Einstiegspunkt zur Initialisierung der Anwendung
    und erleichtert Tests sowie den Einsatz in unterschiedlichen Umgebungen.
    """
    setup_logging()
    
    app = FastAPI(
        title="Chatbot Service",
        description="FastAPI-Service für KI-Bot",
        version="1.0.0",
    )

    app.include_router(chat_router, prefix="/api/v1")
    app.include_router(system_router)

    # einfacher Root-Endpoint zur Prüfung, ob der Service läuft
    @app.get("/")
    def root():
        return {
            "service": "chatbot-service",
            "status": "running"
        }

    return app

app = create_app()