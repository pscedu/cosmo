import json

from fastapi.testclient import TestClient

from ..main import app
from . import utils

client = TestClient(app)


### endpoint: /pig/{id}/fofgroup/MinID/{group_id}
# Basic positive tests
def test_get_fofgroup_minid_251():
    response = client.get("/pig/251/fofgroup/MinID/10")  # test boundary case
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas internal_energy data should be a 446499*1 array list
    fof_data = json.loads(response.json()["fof_data"])
    assert type(fof_data) is int
    assert fof_data == 597130367454


def test_get_fofgroup_minid_271():
    response = client.get("/pig/271/fofgroup/MinID/20")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas internal_energy data should be a 513379*1 array list
    fof_data = json.loads(response.json()["fof_data"])
    assert type(fof_data) is int
    assert fof_data == 437900381799


### endpoint: /pig/{id}/fofgroup/BlackholeMass/{group_id}
# Basic positive tests
def test_get_fofgroup_bhmass_251():
    response = client.get("/pig/251/fofgroup/BlackholeMass/10")  # test boundary case
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas internal_energy data should be a 446499*1 array list
    fof_data = json.loads(response.json()["fof_data"])
    assert type(fof_data) is float
    assert fof_data == 0.020697657018899918


def test_get_fofgroup_bhmass_271():
    response = client.get("/pig/271/fofgroup/BlackholeMass/20")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas internal_energy data should be a 513379*1 array list
    fof_data = json.loads(response.json()["fof_data"])
    assert type(fof_data) is float
    assert fof_data == 0.013113398104906082


### endpoint: /pig/{id}/fofgroup/StarFormationRate/{group_id}
# Basic positive tests
def test_get_fofgroup_sfr_251():
    response = client.get("/pig/251/fofgroup/StarFormationRate/10")  # test boundary case
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas internal_energy data should be a 446499*1 array list
    fof_data = json.loads(response.json()["fof_data"])
    assert type(fof_data) is float
    assert fof_data == 73.0089416503906250


def test_get_fofgroup_sfr_271():
    response = client.get("/pig/271/fofgroup/StarFormationRate/20")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas internal_energy data should be a 513379*1 array list
    fof_data = json.loads(response.json()["fof_data"])
    assert type(fof_data) is float
    assert fof_data == 101.4774246215820312


### endpoint: /pig/{id}/fofgroup/Mass/{group_id}
# Basic positive tests
def test_get_fofgroup_mass_251():
    response = client.get("/pig/251/fofgroup/Mass/286036300")  # test boundary case
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas internal_energy data should be a 446499*1 array list
    fof_data = json.loads(response.json()["fof_data"])
    assert type(fof_data) is float
    assert fof_data == 0.023881886154413223


def test_get_fofgroup_mass_271():
    response = client.get("/pig/271/fofgroup/Mass/20")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas internal_energy data should be a 513379*1 array list
    fof_data = json.loads(response.json()["fof_data"])
    assert type(fof_data) is float
    assert fof_data == 181.4469909667968750


### endpoint: /pig/{id}/fofgroup/BlackholeAccretionRate/{group_id}
# Basic positive tests
def test_get_fofgroup_bhacc_251():
    response = client.get("/pig/251/fofgroup/BlackholeAccretionRate/10")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas internal_energy data should be a 446499*1 array list
    fof_data = json.loads(response.json()["fof_data"])
    assert type(fof_data) is float
    assert fof_data == 0.10691969841718674


def test_get_fofgroup_bhacc_271():
    response = client.get("/pig/271/fofgroup/BlackholeAccretionRate/20")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas internal_energy data should be a 513379*1 array list
    fof_data = json.loads(response.json()["fof_data"])
    assert type(fof_data) is float
    assert fof_data == 0.18356771767139435


### endpoint: /pig/{id}/fofgroup/MassByType/{group_id}
# Basic positive tests
def test_get_fofgroup_mbt_251():
    response = client.get("/pig/251/fofgroup/MassByType/10")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas internal_energy data should be a 446499*1 array list
    fof_data = json.loads(response.json()["fof_data"])
    assert type(fof_data) is list
    assert fof_data == [28.0266895294189453, 166.1539764404296875, 0., 0., 5.8279027938842773, 0.022659240290522575]


def test_get_fofgroup_mbt_271():
    response = client.get("/pig/271/fofgroup/MassByType/10")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas internal_energy data should be a 513379*1 array list
    fof_data = json.loads(response.json()["fof_data"])
    assert type(fof_data) is list
    assert fof_data == [30.0651035308837891, 190.1893615722656250, 0., 0., 7.6514310836791992, 0.021950561553239822]


### endpoint: /pig/{id}/fofgroup/MassCenterPosition/{group_id}
# Basic positive tests
def test_get_fofgroup_mcp_251():
    response = client.get("/pig/251/fofgroup/MassCenterPosition/10")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas internal_energy data should be a 446499*1 array list
    fof_data = json.loads(response.json()["fof_data"])
    assert type(fof_data) is list
    assert fof_data == [286021.04757619253, 99592.58435937122, 186922.28821872440]


def test_get_fofgroup_mcp_271():
    response = client.get("/pig/271/fofgroup/MassCenterPosition/10")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas internal_energy data should be a 513379*1 array list
    fof_data = json.loads(response.json()["fof_data"])
    assert type(fof_data) is list
    assert fof_data == [72871.81341054394, 195094.91935102656, 229728.45949624668]


### endpoint: /pig/{id}/fofgroup/MassCenterVelocity/{group_id}
# Basic positive tests
def test_get_fofgroup_mcv_251():
    response = client.get("/pig/251/fofgroup/MassCenterVelocity/10")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas internal_energy data should be a 446499*1 array list
    fof_data = json.loads(response.json()["fof_data"])
    assert type(fof_data) is list
    assert fof_data == [-7.5896172523498535, 29.7871456146240234, 9.3012847900390625]


def test_get_fofgroup_mcv_271():
    response = client.get("/pig/271/fofgroup/MassCenterVelocity/10")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas internal_energy data should be a 513379*1 array list
    fof_data = json.loads(response.json()["fof_data"])
    assert type(fof_data) is list
    assert fof_data == [30.488758087158203, -15.635041236877441, 44.830150604248047]


def test_get_fofgroup_negative():
    # missing required parameters
    for field in ['MassCenterVelocity', 'MassCenterPosition', 'MassByType', 'Mass', 'BlackholeMass', 'MinID']:
        utils.test_get_missing_input(251, "FoFGroup", field, 400)
        utils.test_get_missing_input(271, "FoFGroup", field, 400)
        # pig 251 group_id not in [1,286036300] or pig 271 group_id not [1,294288056]
        utils.test_get_invalid_input(251, "FoFGroup", field, -30)
        utils.test_get_invalid_input(251, "FoFGroup", field, 286036400)
        utils.test_get_invalid_input(271, "FoFGroup", field, 0)
        utils.test_get_invalid_input(271, "FoFGroup", field, 294288100)
        # pig id not in folder
        utils.test_get_invalid_input(333, "FoFGroup", field, 400)
        # invalid feature
        utils.test_get_invalid_input(10, "FoFGroup", "xyz", 400)
