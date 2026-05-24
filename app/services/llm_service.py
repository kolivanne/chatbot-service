from abc import ABC, abstractmethod


class LLMService(ABC):
    """
    Basis für alle LLM Anbieter.

    Dient dazu, verschiedene Provider austauschbar zu halten.
    """

    @abstractmethod
    def generate_response(self, message: str) -> str:
        pass