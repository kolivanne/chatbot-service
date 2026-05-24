# Architekturübersicht

Der Service stellt ein einfaches Backend für einen Chat-Endpunkt bereit.

Die Struktur ist bewusst modular aufgebaut, sodass der Service später einfach erweitert und an verschiedene LLM-Provider angebunden werden kann.

---

## Architektur

Der Code ist in drei Ebenen getrennt:

```text
API → Service → LLM-Provider
```

Diese Trennung sorgt für klare Verantwortlichkeiten und bessere Wartbarkeit.

---

## API-Schicht

Hier werden HTTP-Anfragen entgegengenommen und validiert.

**Verantwortlichkeiten:**

- Request-Validierung
- Routing
- Übergabe an die Service-Schicht
- Rückgabe der API-Responses

**Datei:**

```text
app/api/routes/chat.py
```

---

## Service-Schicht

Hier liegt die eigentliche Business-Logik für den Chat.

Die Service-Schicht verarbeitet Anfragen und kommuniziert mit der Provider-Schicht.

**Verantwortlichkeiten:**

- Verarbeitung von Chat-Nachrichten
- Steuerung der LLM-Kommunikation
- Fehlerhandling

**Datei:**

```text
app/services/llm_service.py
```

---

## Provider-Schicht

Hier ist die Anbindung an externe LLM-Dienste vorgesehen.

Aktuell existiert eine Platzhalter-Implementierung, die später durch echte Provider ersetzt werden kann.

**Aktueller Stand:**

- Platzhalter-Implementierung
- Beispielstruktur für Azure OpenAI

**Geplante Provider:**

- Azure OpenAI
- AWS Bedrock

---

## Konfiguration

Die Konfiguration erfolgt über Umgebungsvariablen.

Typische Konfigurationswerte:

- API Keys
- Service-Endpunkte
- Modellnamen
- Logging-Level

Beispiel:

```env
API_KEY=your-api-key
LOG_LEVEL=INFO
```

---

## Logging

Das Logging ist bewusst einfach gehalten.

Es protokolliert:

- eingehende Requests
- Verarbeitungsschritte
- Fehlerfälle

Ziel ist eine einfache Nachvollziehbarkeit während der Entwicklung und des Betriebs.

---

## Fehlerbehandlung

Für Fehler in der Kommunikation mit dem LLM ist eine eigene Exception-Klasse vorgesehen.

Dadurch können Fehler zentral behandelt und standardisierte API-Responses zurückgegeben werden.

---

## Erweiterbarkeit

Die aktuelle Architektur erlaubt spätere Erweiterungen ohne größere Umbauten.

Geplante Erweiterungen:

- echte Anbindung an Azure OpenAI oder AWS Bedrock
- Speicherung von Chatverläufen
- Authentifizierung
- Rate Limiting
- erweiterte Validierung
- Monitoring & Observability
