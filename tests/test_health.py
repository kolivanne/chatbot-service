
def test_health_endpoint_returns_200(client):
    """
    Testet den Happy Path:
    Der Health-Endpunkt ist erreichbar
    und liefert den erwarteten Statuscode zurück.
    """
    response = client.get("/health")

    assert response.status_code == 200


def test_health_endpoint_returns_expected_response(client):
    """
    Testet den Happy Path:
    Die Antwort des Health-Endpunkts
    enthält die erwartete JSON-Struktur.
    """
    response = client.get("/health")

    assert response.json() == {"status": "ok"}


def test_health_endpoint_uses_get_method(client):
    """
    Testet einen Negative Case:
    Der Health-Endpunkt darf keine POST-Requests akzeptieren.
    """
    response = client.post("/health")

    assert response.status_code == 405


def test_health_endpoint_with_trailing_slash(client):
    """
    Testet einen Edge Case:
    Prüft, ob der Endpunkt mit einem
    abschließenden Slash erreichbar ist.
    """
    response = client.get("/health/")

    assert response.status_code in [200, 307]


def test_health_endpoint_response_content_type(client):
    """
    Testet einen Edge Case:
    Die API sollte eine JSON-Antwort liefern.
    """
    response = client.get("/health")

    assert response.headers["content-type"].startswith(
        "application/json"
    )