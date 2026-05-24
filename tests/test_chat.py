def test_chat_endpoint(client):
    """
    Testet den Chat-Endpunkt
    mit einer gültigen Nachricht.
    """
    payload = {
        "message": "Hallo"
    }

    response = client.post(
        "/api/v1/chat",
        json=payload
    )

    assert response.status_code == 200
    assert "response" in response.json()


def test_chat_validation_error(client):
    """
    Testet einen Validation Error:
    Eine Anfrage ohne Pflichtfeld
    soll fehlschlagen.
    """
    response = client.post(
        "/api/v1/chat",
        json={}
    )

    assert response.status_code == 422