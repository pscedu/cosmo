from fastapi.testclient import TestClient
from ..main import app
from .. import utils

client = TestClient(app)


# Common basic positive tests
def common_positive_tests(response):
    # Validate the status code: 200
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"


# Negative testing with invalid input
# Missing required parameters
def test_get_missing_input(id: int, type: str, attribute: str, group_id: int):
    # Validate the status code: 404
    response_without_group_id = client.get(
        "/pig/{id}/{type}/{attribute}/".format(id=id, type=type, attribute=attribute))
    assert response_without_group_id.status_code == 405
    response_without_pig_id = client.get(
        "/pig//{type}/{attribute}/{group_id}".format(type=type, attribute=attribute, group_id=group_id))
    assert response_without_pig_id.status_code == 404
    response_without_type = client.get(
        "/pig/{id}//{attribute}/{group_id}".format(id=id, attribute=attribute, group_id=group_id))
    assert response_without_type.status_code == 404
    response_without_attribure = client.get("/pig/{id}/{type}//{group_id}".format(id=id, type=type, group_id=group_id))
    assert response_without_attribure.status_code == 404


# Invalid value for endpoint parameters.
def test_get_invalid_input(id: int, type: str, attribute: str, group_id: int):
    # Validate the status code: 404
    response = client.get(
        "/pig/{id}/{type}/{attribute}/{group_id}".format(id=id, type=type, attribute=attribute, group_id=group_id))
    assert response.status_code == 404


def test_get_negative(type: str):
    pig_subdirectories = utils.get_pig_folders()
    for pig_subdir in pig_subdirectories:
        pig_id = pig_subdir.replace("PIG_", "")
        max_groupid = get_max_groupid(pig_id)
        field = utils.get_part_subfield(int(pig_id), type)
        # missing required parameters
        test_get_missing_input(pig_id, type, field, 30)
        # group_id not in [1,max_groupid] for this pig folder
        test_get_invalid_input(pig_id, type, field, -10)
        test_get_invalid_input(pig_id, type, field, 0)
        test_get_invalid_input(pig_id, type, field, max_groupid + 1)
        # pig id not in folder
        test_get_invalid_input(5555, type, field, 30)
        test_get_invalid_input(-100, type, field, 30)
        # invalid feature
        test_get_invalid_input(pig_id, type, "xyz", 30)


def get_max_groupid(id: int):
    pig = utils.get_pig_data(id)
    total_group = pig.open('FOFGroups/LengthByType').size
    return total_group
