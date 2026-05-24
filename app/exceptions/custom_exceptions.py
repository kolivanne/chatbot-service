class LLMServiceError(Exception):
    """
    Wird ausgelöst, wenn die Kommunikation mit dem LLM-Provider fehlschlägt.

    Warum eine eigene Exception?
    - trennt fachliche Fehler (LLM/Provider) von allgemeinen Python Fehlern
    - ermöglicht gezieltes Fehlerhandling im API Layer
    - macht Fehlerquellen im Service klar erkennbar
    """

    pass