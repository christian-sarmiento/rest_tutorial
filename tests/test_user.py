import pytest

from myapp import app


@pytest.fixture
def client():
    return app.test_client()


class TestUser:

    def test_succesful_fetching_a_user(self, client):
        response = client.get("api/v1/users/1")

        assert response.status_code == 200
        assert response.json == {
            "id": 1,
            "firstname": "foo",
            "lastname": "bar",
        }

    def test_failed_fetching_a_user(self, client):
        response = client.get("api/v1/users/999")

        assert response.status_code == 404
        assert response.json["error"] == "user not found"

    def test_successful_updating_a_user(self, client):
        updated_payload = {"firstname": "newfirstname", "lastname": "newlastname"}
        response = client.put("api/v1/users/1", json=updated_payload)
        assert response.status_code == 200
        assert response.json["msg"] == "user updated"

    def test_successful_no_change_on_user(self, client):
        updated_payload = {"firstname": "newfirstname", "lastname": "newlastname"}
        response = client.put("api/v1/users/1", json=updated_payload)
        assert response.status_code == 200
        assert response.json["msg"] == "no changes made"

    def test_failed_updating_a_user(self, client):
        updated_payload = {"firstname": "newfirstname", "lastname": "newlastname"}
        response = client.put("api/v1/users/99", json=updated_payload)
        assert response.status_code == 404
        assert response.json["error"] == "user not found"

    def test_successful_deleting_a_user(self, client):
        response = client.delete("api/v1/users/1")
        assert response.status_code == 200
        assert response.json["msg"] == "user deleted"

    def test_failed_deleting_a_user(self, client):
        response = client.delete("api/v1/users/99")
        assert response.status_code == 404
        assert response.json["error"] == "user not found"

    # adding back user for subsequent tests to pass
    def test_successful_adding_user(self, client):
        response = client.post(
            "api/v1/users",
            data={
                "firstname": "foo",
                "lastname": "bar",
            },
        )

        assert response.status_code == 201
        assert response.json["msg"] == "successfully inserted new user"
    
    
    

    

    
