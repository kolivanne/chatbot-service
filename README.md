# Chat Service (FastAPI)

Dieses Projekt ist ein einfacher Backend-Service auf Basis von FastAPI.

Der Service stellt einen Chat-Endpunkt bereit, der eine Nachricht entgegennimmt und eine Antwort zurückgibt. Die LLM-Anbindung ist aktuell als Platzhalter umgesetzt.

## Start des Projekts

### Lokal

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload