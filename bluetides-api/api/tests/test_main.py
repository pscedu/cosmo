import json

from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200


### endpoint: /pig/
# Basic positive tests
def test_get_pig():
    response = client.get("/pig/")
    # Validate the status code: 200
    assert response.status_code == 200
    # Validate payload: Response is a well-formed JSON object
    # response data -- LIST should be a list and match the file data.
    assert type(response.json()["LIST"]) is list
    assert type(response.json()["LIST"][0]["num_halos"]) is int
    assert type(response.json()["LIST"][0]["time"]) is float
    assert response.json() == {
        "LIST": [
            {
                "id": "208", "name": "PIG_208", "num_halos": 267649410, "time": 7.000000015821968
            },
            {
                "id": "230", "name": "PIG_230", "num_halos": 276771522, "time": 6.8500000034945225
            },
            {
                "id": "237", "name": "PIG_237", "num_halos": 279858719, "time": 6.800000003768498
            },
            {
                "id": "216", "name": "PIG_216", "num_halos": 271256543, "time": 6.94000002648998
            },
            {
                "id": "265", "name": "PIG_265", "num_halos": 292040891, "time": 6.600000041506778
            },
            {
                "id": "244", "name": "PIG_244", "num_halos": 282939566, "time": 6.750000008196768
            },
            {
                "id": "271", "name": "PIG_271", "num_halos": 294288056, "time": 6.560000154967445
            },
            {
                "id": "258", "name": "PIG_258", "num_halos": 289106271, "time": 6.650000043417158
            },
            {
                "id": "222", "name": "PIG_222", "num_halos": 273696821, "time": 6.900000011215548
            },
            {
                "id": "251", "name": "PIG_251", "num_halos": 286036300, "time": 6.700000064799543
            },
            {
                "id": "184", "name": "PIG_184", "num_halos": 255434058, "time": 7.200000019001509
            },
            {
                "id": "197", "name": "PIG_197", "num_halos": 261596356, "time": 7.100000019919435
            }
        ]
    }
    # Validate headers
    assert response.headers["content-type"] == "application/json"


# Negative testing with invalid input
# Invalid URL path.
def test_get_pig_invalid_url():
    response = client.get("/pig/2")
    # Validate the status code: 404
    assert response.status_code == 404
