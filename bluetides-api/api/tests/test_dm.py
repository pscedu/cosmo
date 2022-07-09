import json

from fastapi.testclient import TestClient

from ..main import app
from . import utils

client = TestClient(app)


###################################################################
#                           DM Tests                              #
################################################################### 

def test_get_negative_dm():
    utils.test_get_negative("dm")


# DM POSITION
### endpoint: /pig/{id}/dm/position/{group_id}
# Basic positive tests
def test_get_dm_position_244():
    response = client.get("/pig/244/dm/Position/331526")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 2585*3 array list
    dm_position = json.loads(response.json()["dm_position"])
    assert type(dm_position) is list
    assert dm_position[456] == [394903.89612031489, 43208.98194487528, 257613.16877157817]
    assert len(dm_position[0]) == 3
    assert len(dm_position) == 2585


def test_get_dm_position_271():
    response = client.get("/pig/271/dm/Position/10")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 158970*3 array list
    dm_position = json.loads(response.json()["dm_position"])
    assert type(dm_position) is list
    assert dm_position[1] == [72973.67144294265, 195179.85487456998, 229742.43473667066]
    assert len(dm_position[0]) == 3
    assert len(dm_position) == 158970


# DM VELOCITY
def test_get_dm_velocity_244():
    response = client.get("/pig/244/dm/Velocity/1862")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 26324*3 array list
    data = json.loads(response.json()["dm_velocity"])
    assert type(data) is list
    assert data[2000] == [14.788228034973145, 49.952144622802734, 23.566410064697266]
    assert len(data[0]) == 3
    assert len(data) == 26324


def test_get_dm_velocity_271():
    response = client.get("/pig/271/dm/Velocity/10")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 158970*3 array list
    data = json.loads(response.json()["dm_velocity"])
    assert type(data) is list
    assert data[0] == [-2.3727707862854004, 65.58319854736328, 70.11107635498047]
    assert len(data[0]) == 3
    assert len(data) == 158970


# DM MASS
def test_get_dm_mass_265():
    response = client.get("/pig/265/dm/Mass/10")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 158970*1 array list
    data = json.loads(response.json()["dm_mass"])
    assert type(data) is list
    assert data[6] == 0.0011963852448388934
    assert data[:4] == [0.0011963852448388934, 0.0011963852448388934, 0.0011963852448388934, 0.0011963852448388934]
    assert len(data) == 153341


def test_get_dm_mass_271():
    response = client.get("/pig/271/dm/Mass/10")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 158970*1 array list
    data = json.loads(response.json()["dm_mass"])
    assert type(data) is list
    assert data[0] == 0.0011963852448388934
    assert data[:4] == [0.0011963852448388934, 0.0011963852448388934, 0.0011963852448388934, 0.0011963852448388934]
    assert len(data) == 158970


# DM POTENTIAL
def test_get_dm_potential_244():
    response = client.get("/pig/244/dm/Potential/10")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 158970*1 array list
    data = json.loads(response.json()["dm_potential"])
    assert type(data) is list
    assert data[6] == 109580.484375
    assert data[:4] == [109690.15625, 109334.671875, 108381.1640625, 108467.40625]
    assert len(data) == 120864


def test_get_dm_potential_271():
    response = client.get("/pig/271/dm/Potential/10")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 158970*1 array list
    data = json.loads(response.json()["dm_potential"])
    assert type(data) is list
    assert data[0] == -330457.6875
    assert data[:4] == [-330457.6875, -329781.90625, -330611.59375, -330459.625]
    assert len(data) == 158970


# DM GENERATION
def test_get_dm_generation_244():
    response = client.get("/pig/271/dm/Generation/100")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 158970*1 array list
    data = json.loads(response.json()["dm_generation"])
    assert type(data) is list
    assert data[0] == 0
    assert data[:4] == [0, 0, 0, 0]
    assert len(data) == 79204


def test_get_dm_generation_271():
    response = client.get("/pig/271/dm/Generation/10")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 158970*1 array list
    data = json.loads(response.json()["dm_generation"])
    assert type(data) is list
    assert data[0] == 0
    assert data[:4] == [0, 0, 0, 0]
    assert len(data) == 158970


# DM GROUPID
def test_get_dm_groupid_244():
    response = client.get("/pig/271/dm/GroupID/210")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 158970*1 array list
    data = json.loads(response.json()["dm_groupid"])
    assert type(data) is list
    assert data[0] == 210
    assert data[:4] == [210, 210, 210, 210]
    assert len(data) == 60163


def test_get_dm_groupid_271():
    response = client.get("/pig/271/dm/GroupID/10")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 158970*1 array list
    data = json.loads(response.json()["dm_groupid"])
    assert type(data) is list
    assert data[0] == 10
    assert data[:4] == [10, 10, 10, 10]
    assert len(data) == 158970


#################################################################################################


### tests for advanced dm query with post method
def test_post_advanced_dm_velocity_251():
    groupid_list = []
    for i in range(1, 300):
        groupid_list.append(str(i))
    response = client.post("/pig/251/dm/Velocity/", data='[' + ', '.join(groupid_list) + ']')
    # response = client.post("/pig/251/dm/Velocity/", json={"id_list": [13, 14, 15]})
    utils.common_positive_tests(response)
    dm_velocity_13 = json.loads(response.json()["dm_velocity"]["13"])
    assert type(dm_velocity_13) is list
    assert dm_velocity_13[0] == [77.28153228759766, -19.17745018005371, -11.987783432006836]
    assert len(dm_velocity_13) == 122785
    dm_velocity_14 = json.loads(response.json()["dm_velocity"]["14"])
    assert type(dm_velocity_14) is list
    assert dm_velocity_14[0] == [16.777849197387695, 9.605594635009766, -19.376659393310547]
    assert len(dm_velocity_14) == 118147
    dm_velocity_15 = json.loads(response.json()["dm_velocity"]["15"])
    assert type(dm_velocity_15) is list
    assert dm_velocity_15[0] == [33.94892501831055, -33.81675720214844, 34.32453536987305]
    assert len(dm_velocity_15) == 111295


def test_post_advanced_dm_generation_251():
    groupid_list = []
    for i in range(1, 10):
        groupid_list.append(str(i))
    response = client.post("/pig/251/dm/Generation/", data='[' + ', '.join(groupid_list) + ']')
    # response = client.get("/pig/251/dm/Generation/", params = {'groupid_list': [1,2,3]})
    utils.common_positive_tests(response)
    dm_generation_1 = json.loads(response.json()["dm_generation"]["1"])
    assert type(dm_generation_1) is list
    assert dm_generation_1[1000:1004] == [0, 0, 0, 0]
    assert len(dm_generation_1) == 507723
    dm_generation_2 = json.loads(response.json()["dm_generation"]["2"])
    assert type(dm_generation_2) is list
    assert dm_generation_2 == []
    assert len(dm_generation_2) == 0
    dm_generation_3 = json.loads(response.json()["dm_generation"]["3"])
    assert type(dm_generation_3) is list
    assert dm_generation_3[:4] == [0, 0, 0, 0]
    assert len(dm_generation_3) == 247773


def test_post_advanced_dm_groupid_251():
    groupid_list = []
    for i in range(3, 20):
        groupid_list.append(str(i))
    response = client.post("/pig/251/dm/GroupID/", data='[' + ', '.join(groupid_list) + ']')
    # response = client.get("/pig/251/dm/GroupID/", params = {'groupid_list': [4,5,6]})
    utils.common_positive_tests(response)
    dm_groupid_4 = json.loads(response.json()["dm_groupid"]["4"])
    assert type(dm_groupid_4) is list
    assert dm_groupid_4[1000:1004] == [4, 4, 4, 4]
    assert len(dm_groupid_4) == 152736
    dm_groupid_5 = json.loads(response.json()["dm_groupid"]["5"])
    assert type(dm_groupid_5) is list
    assert dm_groupid_5[:4] == [5, 5, 5, 5]
    assert len(dm_groupid_5) == 171025
    dm_groupid_6 = json.loads(response.json()["dm_groupid"]["6"])
    assert type(dm_groupid_6) is list
    assert dm_groupid_6[:4] == [6, 6, 6, 6]
    assert len(dm_groupid_6) == 157684


def test_post_advanced_dm_position_251():
    groupid_list = []
    for i in range(7, 40):
        groupid_list.append(str(i))
    response = client.post("/pig/251/dm/Position/", data='[' + ', '.join(groupid_list) + ']')
    # response = client.get("/pig/251/dm/Position/", params = {'groupid_list': [7,8,9]})
    utils.common_positive_tests(response)
    dm_position_7 = json.loads(response.json()["dm_position"]["7"])
    assert type(dm_position_7) is list
    assert dm_position_7[0] == [15090.16638884406, 146822.30592489312, 290425.66656379856]
    assert len(dm_position_7) == 170384
    dm_position_8 = json.loads(response.json()["dm_position"]["8"])
    assert type(dm_position_8) is list
    assert dm_position_8[0] == [72839.05917071458, 195137.4504980916, 229727.11374453927]
    assert len(dm_position_8) == 153747
    dm_position_9 = json.loads(response.json()["dm_position"]["9"])
    assert type(dm_position_9) is list
    assert dm_position_9[0] == [40435.308715295134, 38807.45872604284, 388542.1490711037]
    assert len(dm_position_9) == 147433


def test_post_advanced_dm_potential_251():
    groupid_list = []
    for i in range(10, 30):
        groupid_list.append(str(i))
    response = client.post("/pig/251/dm/Potential/", data='[' + ', '.join(groupid_list) + ']')
    # response = client.get("/pig/251/dm/Potential/", params = {'groupid_list': [10,11,12]})
    utils.common_positive_tests(response)
    dm_potential_10 = json.loads(response.json()["dm_potential"]["10"])
    assert type(dm_potential_10) is list
    assert dm_potential_10[:4] == [-290229.0, -289857.75, -289965.1875, -290330.96875]
    assert len(dm_potential_10) == 138880
    dm_potential_11 = json.loads(response.json()["dm_potential"]["11"])
    assert type(dm_potential_11) is list
    assert dm_potential_11[:4] == [109564.109375, 109792.53125, 109916.40625, 110013.859375]
    assert len(dm_potential_11) == 121770
    dm_potential_12 = json.loads(response.json()["dm_potential"]["12"])
    assert type(dm_potential_12) is list
    assert dm_potential_12[:4] == [-340517.1875, -340340.96875, -342288.875, -342052.5625]
    assert len(dm_potential_12) == 112594
