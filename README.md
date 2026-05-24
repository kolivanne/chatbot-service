# Chat Service (FastAPI)

Dieses Projekt ist ein einfacher Backend-Service auf Basis von FastAPI.

Der Service stellt einen Chat-Endpunkt bereit, der eine Nachricht entgegennimmt und eine Antwort zurückgibt. Die LLM-Anbindung ist aktuell als Platzhalter umgesetzt.

---

## Projekt starten

### Lokal starten

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Mit Docker

```bash
docker build -t chat-service .
docker run -p 8000:8000 chat-service
```

---

## Endpunkte

### Health Check

**GET `/health`**

Gibt zurück, ob der Service läuft.

#### Beispiel-Response

```json
{
  "status": "ok"
}
```

---

### Chat

**POST `/api/v1/chat`**

#### Beispiel-Request

```json
{
  "message": "Hallo"
}
```

---

## Projektstruktur

```text
app/
├── api/          # HTTP-Endpunkte
├── services/     # Logik für LLM-Anbindung
├── schemas/      # Datenmodelle
├── core/         # Konfiguration und Logging
└── exceptions/   # Fehlerklassen
└── tests/        # Tests
```

---

## Hinweise

Die aktuelle LLM-Integration ist ein Platzhalter.

Eine Anbindung an **Azure OpenAI** oder **AWS Bedrock** ist vorgesehen, aber aktuell noch nicht implementiert.
