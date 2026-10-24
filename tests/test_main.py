from app.main import app


def test_home():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.json["status"] == "success"


def test_health():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_pipeline_stages():
    client = app.test_client()
    response = client.get("/pipeline")

    assert response.status_code == 200
    assert response.json["stages"] == [
        "Build",
        "Test",
        "Package",
        "Deploy",
        "Verify"
    ]