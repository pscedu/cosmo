import json

from fastapi.testclient import TestClient

from ..main import app
from . import utils

client = TestClient(app)

""" BlackholeAccretionRate  BlackholeJumpToMinPot  BlackholeMinPotVel    GroupID   Potential
BlackholeDensity        BlackholeLastMergerID  BlackholePressure     ID        StarFormationTime
BlackholeEntropy        BlackholeMass          BlackholeProgenitors  Mass      Velocity
BlackholeGasVel         BlackholeMinPotPos     Generation                      Position    """


def test_get_negative_bh():
    utils.test_get_negative("bh")


### endpoint: /pig/{id}/bh/Position/{group_id}
# Basic positive tests
def test_get_bh_position_251():
    response = client.get("/pig/251/bh/Position/2")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Velocity data should be a 561897*3 array list
    data = json.loads(response.json()["bh_position"])
    assert type(data) is list
    assert data == []


def test_get_bh_position_271():
    response = client.get("/pig/271/bh/Position/10")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Velocity data should be a 561897*3 array list
    data = json.loads(response.json()["bh_position"])
    assert type(data) is list
    assert len(data) == 5
    assert data[0] == [72656.0567335518135224, 194831.9271345908055082, 229774.9501834622642491]


### endpoint: /pig/{id}/bh/Velocity/{group_id}
# Basic positive tests
def test_get_bh_velocity_251():
    response = client.get("/pig/251/bh/Velocity/20")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Velocity data should be a 561897*3 array list
    data = json.loads(response.json()["bh_velocity"])
    assert type(data) is list
    assert len(data) == 8
    assert data[0] == [54.4735107421875000, -16.7231864929199219, -10.2117156982421875]


def test_get_bh_velocity_271():
    response = client.get("/pig/271/bh/Velocity/20")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Velocity data should be a 561897*3 array list
    data = json.loads(response.json()["bh_velocity"])
    assert type(data) is list
    assert len(data) == 7
    assert data[0] == [24.9600467681884766, 37.8858528137207031, -24.7577743530273438]


### endpoint: /pig/{id}/bh/Generation/{group_id}
# Basic positive tests
def test_get_bh_generation_251():
    response = client.get("/pig/251/bh/Generation/3")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Generation data should be a 1*1 array list
    data = json.loads(response.json()["bh_generation"])
    assert type(data) is list
    assert data == [1, 1, 1, 1, 2, 1, 2, 1]


def test_get_bh_generation_271():
    response = client.get("/pig/271/bh/Generation/3")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Generation data should be a 1*1 array list
    data = json.loads(response.json()["bh_generation"])
    assert type(data) is list
    assert data == [1, 1, 1, 1, 2, 1, 2]


### endpoint: /pig/{id}/bh/GroupID/{group_id}
# Basic positive tests
def test_get_bh_groupid_251():
    response = client.get("/pig/251/bh/GroupID/5")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh GroupID data should be a 173607*1 array list
    data = json.loads(response.json()["bh_groupid"])
    assert type(data) is list
    assert data[0] == 5
    assert len(data) == 11


def test_get_bh_groupid_271():
    response = client.get("/pig/271/bh/GroupID/5")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh GroupID data should be a 173607*1 array list
    data = json.loads(response.json()["bh_groupid"])
    assert type(data) is list
    assert data[6] == 5
    assert len(data) == 7


### endpoint: /pig/{id}/bh/Mass/{group_id}
# Basic positive tests
def test_get_bh_mass_251():
    response = client.get("/pig/251/bh/Mass/6")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Mass data should be a 83207*1 array list
    data = json.loads(response.json()["bh_mass"])
    assert type(data) is list
    assert abs(data[0] - 0.0003362224379089) < 1e-8
    assert len(data) == 7


def test_get_bh_mass_271():
    response = client.get("/pig/271/bh/Mass/6")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Mass data should be a 83207*1 array list
    data = json.loads(response.json()["bh_mass"])
    assert type(data) is list
    assert abs(data[0] - 0.0002862224355340) < 1e-8
    assert len(data) == 8


### endpoint: /pig/{id}/bh/BlackholeMass/{group_id}
# Basic positive tests
def test_get_bh_blackholemass_251():
    response = client.get("/pig/251/bh/BlackholeMass/6")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholemass"])
    assert type(data) is list
    assert abs(data[0] - 0.0001233712100657) < 1e-8
    assert len(data) == 7


def test_get_bh_blackholemass_271():
    response = client.get("/pig/271/bh/BlackholeMass/6")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholemass"])
    assert type(data) is list
    assert abs(data[0] - 0.0001511774753453) < 1e-8

    assert len(data) == 8


### endpoint: /pig/{id}/bh/Potential/{group_id}
# Basic positive tests
def test_get_bh_potential_251():
    response = client.get("/pig/251/bh/Potential/8")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_potential"])
    assert type(data) is list
    assert data[0] == -277161.1250
    assert len(data) == 5


def test_get_bh_potential_271():
    response = client.get("/pig/271/bh/Potential/8")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_potential"])
    assert type(data) is list
    assert data[0] == 44106.32031250
    assert len(data) == 10


### endpoint: /pig/{id}/bh/ID/{group_id}
# Basic positive tests
def test_get_bh_id_251():
    response = client.get("/pig/251/bh/ID/10")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_id"])
    assert type(data) is list
    assert data[8] == 72057843939697633
    assert len(data) == 9


def test_get_bh_id_271():
    response = client.get("/pig/271/bh/ID/8")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_id"])
    assert type(data) is list
    assert data[9] == 72057727253357575
    assert len(data) == 10


### endpoint: /pig/{id}/bh/BlackholeProgenitors/{group_id}
# Basic positive tests
def test_get_bh_blackholeprogenitors_251():
    response = client.get("/pig/251/bh/BlackholeProgenitors/12")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholeprogenitors"])
    assert type(data) is list
    assert data == [0, 0]


def test_get_bh_blackholeprogenitors_271():
    response = client.get("/pig/271/bh/BlackholeProgenitors/8")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholeprogenitors"])
    assert type(data) is list
    assert data[5] == 0
    assert len(data) == 10


### endpoint: /pig/{id}/bh/BlackholeMinPotVel/{group_id}
# Basic positive tests
def test_get_bh_blackholeminpotvel_251():
    response = client.get("/pig/251/bh/BlackholeMinPotVel/14")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholeminpotvel"])
    assert type(data) is list
    assert data[0] == [30.8339633941650391, -8.3439722061157227, -1.4297494888305664]
    assert len(data) == 5


def test_get_bh_blackholeminpotvel_271():
    response = client.get("/pig/271/bh/BlackholeMinPotVel/14")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholeminpotvel"])
    assert type(data) is list
    assert data[0] == [-68.5757751464843750, -48.4527740478515625, 22.2900638580322266]
    assert len(data) == 6


### endpoint: /pig/{id}/bh/BlackholeMinPotPos/{group_id}
# Basic positive tests
def test_get_bh_blackholeminpotpos_251():
    response = client.get("/pig/251/bh/BlackholeMinPotPos/16")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholeminpotpos"])
    assert type(data) is list
    assert data[0] == [385029.0029749941313639, 386472.4315522146061994, 188237.1807050006464124]
    assert len(data) == 7


def test_get_bh_blackholeminpotpos_271():
    response = client.get("/pig/271/bh/BlackholeMinPotPos/16")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholeminpotpos"])
    assert type(data) is list
    assert data[0] == [321746.1416593762696721, 45754.5331728641976952, 119495.5197756342240609]
    assert len(data) == 6


### endpoint: /pig/{id}/bh/BlackholeLastMergerID/{group_id}
# Basic positive tests
def test_get_bh_blackholelastmergerid_251():
    response = client.get("/pig/251/bh/BlackholeLastMergerID/18")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholelastmergerid"])
    assert type(data) is list
    assert data == [0, 0, 0, 0, 0]


def test_get_bh_blackholelastmergerid_271():
    response = client.get("/pig/271/bh/BlackholeLastMergerID/18")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholelastmergerid"])
    assert type(data) is list
    assert data == [0, 72057930757709835, 0, 0, 0]


### endpoint: /pig/{id}/bh/BlackholeGasVel/{group_id}
# Basic positive tests
def test_get_bh_blackholegasvel_251():
    response = client.get("/pig/251/bh/BlackholeGasVel/20")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholegasvel"])
    assert type(data) is list
    assert data[0] == [59.5527992248535156, -23.2456321716308594, -10.0467796325683594]
    assert len(data) == 8


def test_get_bh_blackholegasvel_271():
    response = client.get("/pig/271/bh/BlackholeGasVel/20")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholegasvel"])
    assert type(data) is list
    assert data[0] == [17.7611846923828125, 44.2505416870117188, -26.4937973022460938]
    assert len(data) == 7


### endpoint: /pig/{id}/bh/BlackholeEntropy/{group_id}
# Basic positive tests
def test_get_bh_blackholeentropy_251():
    response = client.get("/pig/251/bh/BlackholeEntropy/22")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholeentropy"])
    assert type(data) is list
    assert data[0] == 267099.3125
    assert len(data) == 7


def test_get_bh_blackholeentropy_271():
    response = client.get("/pig/271/bh/BlackholeEntropy/22")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholeentropy"])
    assert type(data) is list
    assert data[0] == 439651.875
    assert len(data) == 6


### endpoint: /pig/{id}/bh/BlackholeDensity/{group_id}
# Basic positive tests
def test_get_bh_blackholedensity_251():
    response = client.get("/pig/251/bh/BlackholeDensity/24")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholedensity"])
    assert type(data) is list
    assert abs(data[0] - 0.0003469409130048) < 1e-8
    assert len(data) == 4


def test_get_bh_blackholedensity_271():
    response = client.get("/pig/271/bh/BlackholeDensity/24")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholedensity"])
    assert type(data) is list
    assert abs(data[0] - 0.0008554264204577) < 1e-8
    assert len(data) == 8


### endpoint: /pig/{id}/bh/BlackholeAccretionRate/{group_id}
# Basic positive tests
def test_get_bh_blackholeaccretionrate_251():
    response = client.get("/pig/251/bh/BlackholeAccretionRate/26")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholeaccretionrate"])
    assert type(data) is list
    assert abs(data[0] - 0.0025596539489925) < 1e-8
    assert len(data) == 3


def test_get_bh_blackholeaccretionrate_271():
    response = client.get("/pig/271/bh/BlackholeAccretionRate/26")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholeaccretionrate"])
    assert type(data) is list
    assert abs(data[0] - 0.0007860922487453) < 1e-8
    assert len(data) == 8


#################################################################################################

### tests for advanced bh query with post method
def test_post_advanced_bh_generation_251():
    groupid_list = []
    for i in range(1, 300):
        groupid_list.append(str(i))
    response = client.post("/pig/251/bh/Generation/", data='[' + ', '.join(groupid_list) + ']')
    # response = client.get("/pig/251/bh/Generation/", params = {'groupid_list': [1,2,3]})
    utils.common_positive_tests(response)
    bh_generation_1 = json.loads(response.json()["bh_generation"]["1"])
    assert type(bh_generation_1) is list
    assert bh_generation_1 == [1, 1, 1, 1, 1, 2, 1]
    assert len(bh_generation_1) == 7
    bh_generation_2 = json.loads(response.json()["bh_generation"]["2"])
    assert type(bh_generation_2) is list
    assert bh_generation_2 == []
    assert len(bh_generation_2) == 0
    bh_generation_3 = json.loads(response.json()["bh_generation"]["3"])
    assert type(bh_generation_3) is list
    assert bh_generation_3 == [1, 1, 1, 1, 2, 1, 2, 1]
    assert len(bh_generation_3) == 8


def test_post_advanced_bh_groupid_251():
    groupid_list = []
    for i in range(4, 10):
        groupid_list.append(str(i))
    response = client.post("/pig/251/bh/GroupID/", data='[' + ', '.join(groupid_list) + ']')
    # response = client.get("/pig/251/bh/GroupID/", params = {'groupid_list': [4,5,6]})
    utils.common_positive_tests(response)
    bh_groupid_4 = json.loads(response.json()["bh_groupid"]["4"])
    assert type(bh_groupid_4) is list
    assert bh_groupid_4[:4] == [4, 4]
    assert len(bh_groupid_4) == 2
    bh_groupid_5 = json.loads(response.json()["bh_groupid"]["5"])
    assert type(bh_groupid_5) is list
    assert bh_groupid_5[:4] == [5, 5, 5, 5]
    assert len(bh_groupid_5) == 11
    bh_groupid_6 = json.loads(response.json()["bh_groupid"]["6"])
    assert type(bh_groupid_6) is list
    assert bh_groupid_6[:4] == [6, 6, 6, 6]
    assert len(bh_groupid_6) == 7


def test_post_advanced_bh_position_251():
    groupid_list = []
    for i in range(7, 20):
        groupid_list.append(str(i))
    response = client.post("/pig/251/bh/Position/", data='[' + ', '.join(groupid_list) + ']')
    # response = client.get("/pig/251/bh/Position/", params = {'groupid_list': [7,8,9]})
    utils.common_positive_tests(response)
    bh_position_7 = json.loads(response.json()["bh_position"]["7"])
    assert type(bh_position_7) is list
    assert bh_position_7[0] == [15382.678998266496, 145925.19427169597, 290399.2446326842]
    assert len(bh_position_7) == 12
    bh_position_8 = json.loads(response.json()["bh_position"]["8"])
    assert type(bh_position_8) is list
    assert bh_position_8[0] == [72208.11967420416, 194269.7290507568, 229826.71613942046]
    assert len(bh_position_8) == 5
    bh_position_9 = json.loads(response.json()["bh_position"]["9"])
    assert type(bh_position_9) is list
    assert bh_position_9[0] == [40455.22049012193, 38824.604163998105, 388659.6113405379]
    assert len(bh_position_9) == 8


def test_post_advanced_bh_potential_251():
    groupid_list = []
    for i in range(10, 25):
        groupid_list.append(str(i))
    response = client.post("/pig/251/bh/Potential/", data='[' + ', '.join(groupid_list) + ']')
    # response = client.get("/pig/251/bh/Potential/", params = {'groupid_list': [10,11,12]})
    utils.common_positive_tests(response)
    bh_potential_10 = json.loads(response.json()["bh_potential"]["10"])
    assert type(bh_potential_10) is list
    assert bh_potential_10[:4] == [-292802.53125, -311502.59375, -299892.75, -319366.15625]
    assert len(bh_potential_10) == 9
    bh_potential_11 = json.loads(response.json()["bh_potential"]["11"])
    assert type(bh_potential_11) is list
    assert bh_potential_11[:4] == [48769.54296875, 73449.7421875, 87866.609375, 104375.203125]
    assert len(bh_potential_11) == 6
    bh_potential_12 = json.loads(response.json()["bh_potential"]["12"])
    assert type(bh_potential_12) is list
    assert bh_potential_12 == [-401701.46875, -592302.5]
    assert len(bh_potential_12) == 2


def test_post_advanced_bh_velocity_251():
    groupid_list = []
    for i in range(13, 25):
        groupid_list.append(str(i))
    response = client.post("/pig/251/bh/Velocity/", data='[' + ', '.join(groupid_list) + ']')
    # response = client.get("/pig/251/bh/Velocity/", params = {'groupid_list': [13,14,15]})
    utils.common_positive_tests(response)
    bh_velocity_13 = json.loads(response.json()["bh_velocity"]["13"])
    assert type(bh_velocity_13) is list
    assert bh_velocity_13[0] == [51.82337188720703, 57.168174743652344, 16.91756248474121]
    assert len(bh_velocity_13) == 3
    bh_velocity_14 = json.loads(response.json()["bh_velocity"]["14"])
    assert type(bh_velocity_14) is list
    assert bh_velocity_14[0] == [20.97827911376953, -3.9093408584594727, -18.333993911743164]
    assert len(bh_velocity_14) == 5
    bh_velocity_15 = json.loads(response.json()["bh_velocity"]["15"])
    assert type(bh_velocity_15) is list
    assert bh_velocity_15[0] == [9.807731628417969, -31.17384147644043, 39.47724533081055]
    assert len(bh_velocity_15) == 4


def test_post_advanced_bh_mass_251():
    groupid_list = []
    for i in range(15, 25):
        groupid_list.append(str(i))
    response = client.post("/pig/251/bh/Mass/", data='[' + ', '.join(groupid_list) + ']')
    # response = client.get("/pig/251/bh/Mass/", params = {'groupid_list': [16,17,18]})
    utils.common_positive_tests(response)
    bh_mass_16 = json.loads(response.json()["bh_mass"]["16"])
    assert type(bh_mass_16) is list
    assert bh_mass_16[:4] == [0.00023622244771104306, 0.013051284477114677, 0.00023622244771104306,
                              0.00023622244771104306]
    assert len(bh_mass_16) == 7
    bh_mass_17 = json.loads(response.json()["bh_mass"]["17"])
    assert type(bh_mass_17) is list
    assert bh_mass_17[:4] == [0.0002862224355340004, 0.0002862224355340004, 0.007765813730657101, 0.0005224448977969587]
    assert len(bh_mass_17) == 8
    bh_mass_18 = json.loads(response.json()["bh_mass"]["18"])
    assert type(bh_mass_18) is list
    assert bh_mass_18[:4] == [0.0002862224355340004, 0.0012401678832247853, 0.004192948807030916, 0.001003945479169488]
    assert len(bh_mass_18) == 5


def test_post_advanced_bh_starformationtime_251():
    groupid_list = []
    for i in range(20, 30):
        groupid_list.append(str(i))
    response = client.post("/pig/251/bh/StarFormationTime/", data='[' + ', '.join(groupid_list) + ']')
    # response = client.get("/pig/251/bh/StarFormationTime/", params = {'groupid_list': [22,23,24]})
    utils.common_positive_tests(response)
    bh_sft_22 = json.loads(response.json()["bh_starformationtime"]["22"])
    assert type(bh_sft_22) is list
    assert bh_sft_22 == [0.0, 0.1111111119389534, 0.0, 0.0, 0.0, 0.0, 0.0]
    assert len(bh_sft_22) == 7
    bh_sft_23 = json.loads(response.json()["bh_starformationtime"]["23"])
    assert type(bh_sft_23) is list
    assert bh_sft_23 == [0.0, 0.11428570747375488, 0.12747056782245636, 0.1149425283074379]
    assert len(bh_sft_23) == 4
    bh_sft_24 = json.loads(response.json()["bh_starformationtime"]["24"])
    assert type(bh_sft_24) is list
    assert bh_sft_24[:4] == [0.0, 0.11956783384084702, 0.0, 0.0]
    assert len(bh_sft_24) == 4


def test_post_advanced_bh_blackholeaccretionrate_251():
    groupid_list = []
    for i in range(25, 30):
        groupid_list.append(str(i))
    response = client.post("/pig/251/bh/BlackholeAccretionRate/", data='[' + ', '.join(groupid_list) + ']')
    # response = client.get("/pig/251/bh/BlackholeAccretionRate/", params = {'groupid_list': [25,26,27]})
    utils.common_positive_tests(response)
    bh_bar_25 = json.loads(response.json()["bh_blackholeaccretionrate"]["25"])
    assert type(bh_bar_25) is list
    assert bh_bar_25 == [0.0017296597361564636, 0.01974768377840519, 0.0006966761429794133, 1.0660497906656019e-07]
    assert len(bh_bar_25) == 4
    bh_bar_26 = json.loads(response.json()["bh_blackholeaccretionrate"]["26"])
    assert type(bh_bar_26) is list
    assert bh_bar_26 == [0.0025596539489924908, 0.022932419553399086, 0.0013235744554549456]
    assert len(bh_bar_26) == 3
    bh_bar_27 = json.loads(response.json()["bh_blackholeaccretionrate"]["27"])
    assert type(bh_bar_27) is list
    assert bh_bar_27 == [0.012562813237309456, 0.008227601647377014, 0.001624724711291492]
    assert len(bh_bar_27) == 3


def test_post_advanced_bh_blackholejumptominpot_251():
    groupid_list = []
    for i in range(25, 35):
        groupid_list.append(str(i))
    response = client.post("/pig/251/bh/BlackholeJumpToMinPot/", data='[' + ', '.join(groupid_list) + ']')
    # response = client.get("/pig/251/bh/BlackholeJumpToMinPot/", params = {'groupid_list': [28,29,30]})
    utils.common_positive_tests(response)
    bh_bjtmp_28 = json.loads(response.json()["bh_blackholejumptominpot"]["28"])
    assert type(bh_bjtmp_28) is list
    assert bh_bjtmp_28 == [0, 0, 0, 0, 0, 0]
    assert len(bh_bjtmp_28) == 6
    bh_bjtmp_29 = json.loads(response.json()["bh_blackholejumptominpot"]["29"])
    assert type(bh_bjtmp_29) is list
    assert bh_bjtmp_29 == [0, 0]
    assert len(bh_bjtmp_29) == 2
    bh_bjtmp_30 = json.loads(response.json()["bh_blackholejumptominpot"]["30"])
    assert type(bh_bjtmp_30) is list
    assert bh_bjtmp_30 == [0, 0]
    assert len(bh_bjtmp_30) == 2


def test_post_advanced_bh_blackholeminpotvel_251():
    groupid_list = []
    for i in range(30, 35):
        groupid_list.append(str(i))
    response = client.post("/pig/251/bh/BlackholeMinPotVel/", data='[' + ', '.join(groupid_list) + ']')
    # response = client.get("/pig/251/bh/BlackholeMinPotVel/", params = {'groupid_list': [31,32,33]})
    utils.common_positive_tests(response)
    bh_bmpv_31 = json.loads(response.json()["bh_blackholeminpotvel"]["31"])
    assert type(bh_bmpv_31) is list
    assert bh_bmpv_31[0] == [27.996049880981445, -24.18301773071289, 37.580970764160156]
    assert len(bh_bmpv_31) == 5
    bh_bmpv_32 = json.loads(response.json()["bh_blackholeminpotvel"]["32"])
    assert type(bh_bmpv_32) is list
    assert bh_bmpv_32[0] == [0.41657987236976624, -81.5214614868164, 3.174196481704712]
    assert len(bh_bmpv_32) == 10
    bh_bmpv_33 = json.loads(response.json()["bh_blackholeminpotvel"]["33"])
    assert type(bh_bmpv_33) is list
    assert bh_bmpv_33[0] == [5.418471336364746, 8.822249412536621, -48.358001708984375]
    assert len(bh_bmpv_33) == 5


def test_post_advanced_bh_blackholedensity_251():
    groupid_list = []
    for i in range(30, 40):
        groupid_list.append(str(i))
    response = client.post("/pig/251/bh/BlackholeDensity/", data='[' + ', '.join(groupid_list) + ']')
    # response = client.get("/pig/251/bh/BlackholeDensity/", params = {'groupid_list': [34,35,36]})
    utils.common_positive_tests(response)
    bh_bd_34 = json.loads(response.json()["bh_blackholedensity"]["34"])
    assert type(bh_bd_34) is list
    assert bh_bd_34 == [5.013505506212823e-05, 0.0005382715607993305, 0.0009130614926107228]
    assert len(bh_bd_34) == 3
    bh_bd_35 = json.loads(response.json()["bh_blackholedensity"]["35"])
    assert type(bh_bd_35) is list
    assert bh_bd_35[:4] == [0.000524784903973341, 0.00024969057994894683, 4.7002093197079375e-05, 0.0006094202399253845]
    assert len(bh_bd_35) == 9
    bh_bd_36 = json.loads(response.json()["bh_blackholedensity"]["36"])
    assert type(bh_bd_36) is list
    assert bh_bd_36 == [0.11018983274698257]
    assert len(bh_bd_36) == 1


def test_post_advanced_bh_blackholelastmergerid_251():
    groupid_list = []
    for i in range(35, 40):
        groupid_list.append(str(i))
    response = client.post("/pig/251/bh/BlackholeLastMergerID/", data='[' + ', '.join(groupid_list) + ']')
    # response = client.get("/pig/251/bh/BlackholeLastMergerID/", params = {'groupid_list': [37,38,39]})
    utils.common_positive_tests(response)
    bh_blmid_37 = json.loads(response.json()["bh_blackholelastmergerid"]["37"])
    assert type(bh_blmid_37) is list
    assert bh_blmid_37 == [0, 0, 0]
    assert len(bh_blmid_37) == 3
    bh_blmid_38 = json.loads(response.json()["bh_blackholelastmergerid"]["38"])
    assert type(bh_blmid_38) is list
    assert bh_blmid_38 == [0, 0, 0]
    assert len(bh_blmid_38) == 3
    bh_blmid_39 = json.loads(response.json()["bh_blackholelastmergerid"]["39"])
    assert type(bh_blmid_39) is list
    assert bh_blmid_39 == [0]
    assert len(bh_blmid_39) == 1


def test_post_advanced_bh_blackholepressure_251():
    groupid_list = []
    for i in range(40, 47):
        groupid_list.append(str(i))
    response = client.post("/pig/251/bh/BlackholePressure/", data='[' + ', '.join(groupid_list) + ']')
    # response = client.get("/pig/251/bh/BlackholePressure/", params = {'groupid_list': [40,41,42]})
    utils.common_positive_tests(response)
    bh_bp_40 = json.loads(response.json()["bh_blackholepressure"]["40"])
    assert type(bh_bp_40) is list
    assert bh_bp_40 == [112.67707824707031]
    assert len(bh_bp_40) == 1
    bh_bp_41 = json.loads(response.json()["bh_blackholepressure"]["41"])
    assert type(bh_bp_41) is list
    assert bh_bp_41 == [0.0066551933996379375, 10.079965591430664]
    assert len(bh_bp_41) == 2
    bh_bp_42 = json.loads(response.json()["bh_blackholepressure"]["42"])
    assert type(bh_bp_42) is list
    assert bh_bp_42 == [0.018974779173731804, 0.022676007822155952, 0.12151334434747696, 141.8990936279297]
    assert len(bh_bp_42) == 4


def test_post_advanced_bh_blackholeentropy_251():
    groupid_list = []
    for i in range(43, 53):
        groupid_list.append(str(i))
    response = client.post("/pig/251/bh/BlackholeEntropy/", data='[' + ', '.join(groupid_list) + ']')
    # response = client.get("/pig/251/bh/BlackholeEntropy/", params = {'groupid_list': [43,44,45]})
    utils.common_positive_tests(response)
    bh_be_43 = json.loads(response.json()["bh_blackholeentropy"]["43"])
    assert type(bh_be_43) is list
    assert bh_be_43[:4] == [17099.06640625, 28533.619140625, 338281.5, 767330.5625]
    assert len(bh_be_43) == 9
    bh_be_44 = json.loads(response.json()["bh_blackholeentropy"]["44"])
    assert type(bh_be_44) is list
    assert bh_be_44[:4] == [3100466.0, 73767.734375, 30041.2578125, 80111.7109375]
    assert len(bh_be_44) == 6
    bh_be_45 = json.loads(response.json()["bh_blackholeentropy"]["45"])
    assert type(bh_be_45) is list
    assert bh_be_45 == [423649.125, 48610.53125, 78370.8828125]
    assert len(bh_be_45) == 3


def test_post_advanced_bh_blackholemass_251():
    groupid_list = []
    for i in range(45, 55):
        groupid_list.append(str(i))
    response = client.post("/pig/251/bh/BlackholeMass/", data='[' + ', '.join(groupid_list) + ']')
    # response = client.get("/pig/251/bh/BlackholeMass/", params = {'groupid_list': [46,47,48]})
    utils.common_positive_tests(response)
    bh_bm_46 = json.loads(response.json()["bh_blackholemass"]["46"])
    assert type(bh_bm_46) is list
    assert bh_bm_46 == [9.721509559312835e-05, 0.0011907505104318261, 0.0007833917625248432, 0.004231594502925873]
    assert len(bh_bm_46) == 4
    bh_bm_47 = json.loads(response.json()["bh_blackholemass"]["47"])
    assert type(bh_bm_47) is list
    assert bh_bm_47 == [0.00013148481957614422, 0.0014098959509283304, 0.006093608681112528, 8.305722440127283e-05]
    assert len(bh_bm_47) == 4
    bh_bm_48 = json.loads(response.json()["bh_blackholemass"]["48"])
    assert type(bh_bm_48) is list
    assert bh_bm_48 == [0.0004951045266352594, 0.017347518354654312]
    assert len(bh_bm_48) == 2


def test_post_advanced_bh_blackholeprogenitors_251():
    groupid_list = []
    for i in range(45, 55):
        groupid_list.append(str(i))
    response = client.post("/pig/251/bh/BlackholeProgenitors/", data='[' + ', '.join(groupid_list) + ']')
    # response = client.get("/pig/251/bh/BlackholeProgenitors/", params = {'groupid_list': [49,50,51]})
    utils.common_positive_tests(response)
    bh_bp_49 = json.loads(response.json()["bh_blackholeprogenitors"]["49"])
    assert type(bh_bp_49) is list
    assert bh_bp_49 == [0, 0, 0, 0]
    assert len(bh_bp_49) == 4
    bh_bp_50 = json.loads(response.json()["bh_blackholeprogenitors"]["50"])
    assert type(bh_bp_50) is list
    assert bh_bp_50 == [0, 0, 0, 0, 0]
    assert len(bh_bp_50) == 5
    bh_bp_51 = json.loads(response.json()["bh_blackholeprogenitors"]["51"])
    assert type(bh_bp_51) is list
    assert bh_bp_51 == [0, 0, 0, 0, 0]
    assert len(bh_bp_51) == 5


def test_post_advanced_bh_blackholegasvel_251():
    groupid_list = []
    for i in range(50, 55):
        groupid_list.append(str(i))
    response = client.post("/pig/251/bh/BlackholeGasVel/", data='[' + ', '.join(groupid_list) + ']')
    # response = client.get("/pig/251/bh/BlackholeGasVel/", params = {'groupid_list': [52,53,54]})
    utils.common_positive_tests(response)
    bh_bgv_52 = json.loads(response.json()["bh_blackholegasvel"]["52"])
    assert type(bh_bgv_52) is list
    assert bh_bgv_52[0] == [56.60761642456055, 30.670557022094727, 0.703578770160675]
    assert len(bh_bgv_52) == 5
    bh_bgv_53 = json.loads(response.json()["bh_blackholegasvel"]["53"])
    assert type(bh_bgv_53) is list
    assert bh_bgv_53[0] == [57.00897216796875, -38.592403411865234, -15.049301147460938]
    assert len(bh_bgv_53) == 4
    bh_bgv_54 = json.loads(response.json()["bh_blackholegasvel"]["54"])
    assert type(bh_bgv_54) is list
    assert bh_bgv_54[0] == [7.264092922210693, -2.342128276824951, 38.25501251220703]
    assert len(bh_bgv_54) == 2


def test_post_advanced_bh_blackholeminpotpos_251():
    groupid_list = []
    for i in range(55, 60):
        groupid_list.append(str(i))
    response = client.post("/pig/251/bh/BlackholeMinPotPos/", data='[' + ', '.join(groupid_list) + ']')
    # response = client.get("/pig/251/bh/BlackholeMinPotPos/", params = {'groupid_list': [55,56,57]})
    utils.common_positive_tests(response)
    bh_bmpp_55 = json.loads(response.json()["bh_blackholeminpotpos"]["55"])
    assert type(bh_bmpp_55) is list
    assert bh_bmpp_55[0] == [136916.93460704634, 135750.07441420588, 346376.0120192033]
    assert len(bh_bmpp_55) == 3
    bh_bmpp_56 = json.loads(response.json()["bh_blackholeminpotpos"]["56"])
    assert type(bh_bmpp_56) is list
    assert bh_bmpp_56[0] == [278271.69589058624, 73374.85884896181, 391.2034806571572]
    assert len(bh_bmpp_56) == 3
    bh_bmpp_57 = json.loads(response.json()["bh_blackholeminpotpos"]["57"])
    assert type(bh_bmpp_57) is list
    assert bh_bmpp_57[0] == [36850.991004548894, 44258.21038807316, 42993.6106879176]
    assert len(bh_bmpp_57) == 3
