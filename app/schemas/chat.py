from pydantic import BaseModel, Field, field_validator


class ChatRequest(BaseModel):
    """
    Request-Modell für eine Chatnachricht.

    Hier wird sichergestellt, dass nur gültige Eingaben
    überhaupt in die Anwendung gelangen.
    """

    message: str = Field(
        ...,
        min_length=1,
        max_length=4000,
        description="Nachricht des Users an den Chatbot",
    )

    @field_validator("message")
    @classmethod
    def validate_message(cls, value: str) -> str:
        """
        Entfernt unnötige Leerzeichen und verhindert leere Eingaben.

        Warum das hier?
        - frühe Validierung direkt am Input
        - verhindert unnötige Verarbeitung im Service Layer
        """

        value = value.strip()

        if not value:
            raise ValueError("Nachricht darf nicht leer sein")

        return value


class ChatResponse(BaseModel):
    """
    Response-Modell für eine Chatantwort.

    Antwort des LLM.
    """

    response: str