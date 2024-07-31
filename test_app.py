import pytest
import httpx
from fastapi.testclient import TestClient
from app import app, get_prediction, transform_image

client = TestClient(app)


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_create_file():
    file_content = b"Hello, world!"
    response = client.post("/files/", files={"file": ("test.txt", file_content)})
    assert response.status_code == 200
    assert response.json() == {"file_size": len(file_content)}


def test_create_upload_file():
    response = client.post(
        "/uploadfile/", files={"file": ("test.txt", b"Test file content")}
    )
    assert response.status_code == 200
    assert response.json() == {"filename": "test.txt"}
