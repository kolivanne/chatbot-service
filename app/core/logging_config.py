import logging

from app.core.config import settings


def setup_logging():
    """
    Zentrale Konfiguration des Loggings für die Anwendung..

    Der Log-Level wird aus der Konfiguration geladen,
    um Verhalten je nach Umgebung (z.B. Entwicklung oder Produktion) anzupassen.
    Einheitliches Log-Format erleichtert Debugging und Fehleranalyse.
    """
    logging.basicConfig(
        level=settings.log_level,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )