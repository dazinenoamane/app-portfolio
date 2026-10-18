from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_healthz():
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_about_has_expected_fields():
    response = client.get("/api/about")
    assert response.status_code == 200
    body = response.json()
    assert set(body) == {"pod", "version", "uptime_seconds"}
    assert body["uptime_seconds"] >= 0
