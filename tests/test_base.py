# ** Base Modules
from fastapi import status
# ** App Modules
from main import testClient as client


def test_home():
    response = client.get("/", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert response.json() == {
        "status": status.HTTP_200_OK
    }
