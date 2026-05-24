"""
Sehr einfache Schutzschicht gegen offensichtliche Prompt Injection Versuche.

Ziel ist nicht vollständige Sicherheit, sondern das Bewusstsein für das Problem
und eine minimale Absicherung im Grundgerüst.
"""

from typing import List


def sanitize_message(message: str) -> str:
    """
    Prüft User Input auf einfache Manipulationsversuche.

    Diese Implementierung ist bewusst simpel gehalten und ersetzt keine
    echte Security-Lösung.
    """

    blocked_patterns: List[str] = [
        "ignore previous instructions",
        "system prompt",
        "reveal system",
        "you are now",
    ]

    lower_msg = message.lower()

    for pattern in blocked_patterns:
        if pattern in lower_msg:
            raise ValueError("Ungültige Eingabe erkannt")

    return message.strip()