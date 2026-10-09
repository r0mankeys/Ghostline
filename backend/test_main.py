from io import BytesIO

import pytest
from fastapi import UploadFile
from fastapi.testclient import TestClient
from starlette.datastructures import Headers

from main import app, image_check

client = TestClient(app)

# A few bytes that start like a real PNG. The endpoint only checks the declared content type, so the rest doesn't need to be a valid image.
PNG_BYTES = b"\x89PNG\r\n\x1a\n" + b"\x00" * 100


def make_upload(content_type: str | None) -> UploadFile:
    """Build an UploadFile with the given content type (or none at all)."""
    headers = Headers({"content-type": content_type}) if content_type else None
    return UploadFile(file=BytesIO(b""), filename="test", headers=headers)


# --- image_check: the function on its own, no server involved ---


@pytest.mark.parametrize(
    ("content_type", "expected"),
    [
        ("image/png", True),
        ("image/jpeg", True),
        ("text/plain", False),
        ("audio/aac", False),
        ("video/x-msvideo", False),
        ("font/otf", False),
        ("application/x-image-editor", False),  # the case the regex let through
        (None, False),  # client sent no content type at all
    ],
)
def test_image_check(content_type, expected):
    assert image_check(make_upload(content_type)) is expected


# --- endpoints, called through TestClient (no running server needed) ---


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_upload_image_returns_name_and_size():
    response = client.post(
        "/submissions", files={"file": ("drill.png", PNG_BYTES, "image/png")}
    )
    assert response.status_code == 200
    assert response.json() == {"file": "drill.png", "size": len(PNG_BYTES)}


def test_upload_non_image_is_rejected():
    response = client.post(
        "/submissions", files={"file": ("notes.txt", b"hello", "text/plain")}
    )
    assert response.status_code == 415


def test_upload_without_file_is_rejected():
    # FastAPI's own validation: the required `file` field is missing.
    response = client.post("/submissions")
    assert response.status_code == 422
