import json

from fastapi.testclient import TestClient

from ..main import app
from . import utils

client = TestClient(app)


def test_get_negative_star():
    utils.test_get_negative("star")


### endpoint: /pig/{id}/star/Velocity/{group_id}
# Basic positive tests
def test_get_star_velocity_251():
    response = client.get("/pig/251/star/Velocity/1")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Velocity data should be a 561897*3 array list
    star_velocity = json.loads(response.json()["star_velocity"])
    assert type(star_velocity) is list
    assert star_velocity[0] == [37.31153869628906, 0.5733818411827087, 84.45280456542969]
    assert len(star_velocity) == 561897


def test_get_star_velocity_271():
    response = client.get("/pig/271/star/Velocity/1")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Velocity data should be a 622535*3 array list
    star_velocity = json.loads(response.json()["star_velocity"])
    assert type(star_velocity) is list
    assert star_velocity[0] == [-36.19582748413086, -32.4619255065918, 53.46745681762695]
    assert len(star_velocity) == 622535


### endpoint: /pig/{id}/star/Generation/{group_id}
# Basic positive tests
def test_get_star_generation_251():
    response = client.get("/pig/251/star/Generation/2")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Generation data should be a 1*1 array list
    star_generation = json.loads(response.json()["star_generation"])
    assert type(star_generation) is list
    assert star_generation == [1]
    assert len(star_generation) == 1


def test_get_star_generation_271():
    response = client.get("/pig/271/star/Generation/2")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Generation data should be a 7*1 array list
    star_generation = json.loads(response.json()["star_generation"])
    assert type(star_generation) is list
    assert star_generation == [1, 3, 1, 1, 1, 1, 1]
    assert len(star_generation) == 7


### endpoint: /pig/{id}/star/GroupID/{group_id}
# Basic positive tests
def test_get_star_groupid_251():
    response = client.get("/pig/251/star/GroupID/3")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star GroupID data should be a 173607*1 array list
    star_groupid = json.loads(response.json()["star_groupid"])
    assert type(star_groupid) is list
    assert star_groupid[0] == 3
    assert star_groupid[1000] == 3
    assert len(star_groupid) == 173607


def test_get_star_groupid_271():
    response = client.get("/pig/271/star/GroupID/4")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star GroupID data should be a 232226*1 array list
    star_groupid = json.loads(response.json()["star_groupid"])
    assert type(star_groupid) is list
    assert star_groupid[0] == 4
    assert star_groupid[4000] == 4
    assert len(star_groupid) == 232226


### endpoint: /pig/{id}/star/Mass/{group_id}
# Basic positive tests
def test_get_star_mass_251():
    response = client.get("/pig/251/star/Mass/5")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Mass data should be a 83207*1 array list
    star_mass = json.loads(response.json()["star_mass"])
    assert type(star_mass) is list
    assert star_mass[0] == 5.9055611927760765e-05
    assert star_mass[:4] == [5.9055611927760765e-05, 5.9055611927760765e-05, 5.9055611927760765e-05,
                             5.9055611927760765e-05]
    assert len(star_mass) == 83207


def test_get_star_mass_271():
    response = client.get("/pig/271/star/Mass/5")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Mass data should be a 129814*1 array list
    star_mass = json.loads(response.json()["star_mass"])
    assert type(star_mass) is list
    assert star_mass[0] == 5.9055611927760765e-05
    assert star_mass[:4] == [5.9055611927760765e-05, 5.9055611927760765e-05, 5.9055611927760765e-05,
                             5.9055611927760765e-05]
    assert len(star_mass) == 129814


### endpoint: /pig/{id}/star/Metallicity/{group_id}
# Basic positive tests
def test_get_star_metallicity_251():
    response = client.get("/pig/251/star/Metallicity/6")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Metallicity data should be a 112913*1 array list
    star_metallicity = json.loads(response.json()["star_metallicity"])
    assert type(star_metallicity) is list
    assert star_metallicity[0] == 0.00014949783508200198
    assert star_metallicity[:4] == [0.00014949783508200198, 2.5153325623250566e-05, 9.778260573511943e-05,
                                    6.009096250636503e-05]
    assert len(star_metallicity) == 112913


def test_get_star_metallicity_271():
    response = client.get("/pig/271/star/Metallicity/6")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Metallicity data should be a 166805*1 array list
    star_metallicity = json.loads(response.json()["star_metallicity"])
    assert type(star_metallicity) is list
    assert star_metallicity[0] == 0.0005383077659644186
    assert star_metallicity[:4] == [0.0005383077659644186, 0.00023857371706981212, 9.642468648962677e-05,
                                    0.00032759408350102603]
    assert len(star_metallicity) == 166805


### endpoint: /pig/{id}/star/Position/{group_id}
# Basic positive tests
def test_get_star_position_251():
    response = client.get("/pig/251/star/Position/7")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Position data should be a 72130*1 array list
    star_position = json.loads(response.json()["star_position"])
    assert type(star_position) is list
    assert star_position[0] == [15306.750499744992, 146851.4949004134, 290343.8793858092]
    assert star_position[1] == [15299.60735418374, 146849.01632511956, 290340.75453723327]
    assert len(star_position) == 72130


def test_get_star_position_271():
    response = client.get("/pig/271/star/Position/7")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Position data should be a 87826*1 array list
    star_position = json.loads(response.json()["star_position"])
    assert type(star_position) is list
    assert star_position[0] == [15291.412338536844, 146606.6175727497, 290255.58836157114]
    assert star_position[1] == [15291.47553922203, 146606.87190717706, 290255.52017585444]
    assert len(star_position) == 87826


### endpoint: /pig/{id}/star/Potential/{group_id}
# Basic positive tests
def test_get_star_potential_251():
    response = client.get("/pig/251/star/Potential/8")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Potential data should be a 112659*1 array list
    star_potential = json.loads(response.json()["star_potential"])
    assert type(star_potential) is list
    assert star_potential[0] == -325438.15625
    assert star_potential[4] == -323459.0
    assert len(star_potential) == 112659


def test_get_star_potential_271():
    response = client.get("/pig/271/star/Potential/8")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Potential data should be a 88416*1 array list
    star_potential = json.loads(response.json()["star_potential"])
    assert type(star_potential) is list
    assert star_potential[0] == 67014.3359375
    assert star_potential[4] == 66768.3671875
    assert len(star_potential) == 88416


### endpoint: /pig/{id}/star/StarFormationTime/{group_id}
# Basic positive tests
def test_get_star_starformationtime_251():
    response = client.get("/pig/251/star/StarFormationTime/9")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star StarFormationTime data should be a 112659*1 array list
    star_starformationtime = json.loads(response.json()["star_starformationtime"])
    assert type(star_starformationtime) is list
    assert star_starformationtime[0] == 0.11749737709760666
    assert star_starformationtime[:4] == [0.11749737709760666, 0.11677927523851395, 0.12459807097911835,
                                          0.12012547254562378]
    assert len(star_starformationtime) == 103097


def test_get_star_starformationtime_271():
    response = client.get("/pig/271/star/StarFormationTime/9")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star StarFormationTime data should be a 88416*1 array list
    star_starformationtime = json.loads(response.json()["star_starformationtime"])
    assert type(star_starformationtime) is list
    assert star_starformationtime[0] == 0.12901991605758667
    assert star_starformationtime[:4] == [0.12901991605758667, 0.12974964082241058, 0.12079867720603943,
                                          0.10510993748903275]
    assert len(star_starformationtime) == 102714


#################################################################################################


### tests for advanced star query with post method
def test_post_advanced_star_generation_251():
    groupid_list = []
    for i in range(1, 300):
        groupid_list.append(str(i))
    response = client.post("/pig/251/star/Generation/", data='[' + ', '.join(groupid_list) + ']')
    utils.common_positive_tests(response)
    star_generation_1 = json.loads(response.json()["star_generation"]["1"])
    assert type(star_generation_1) is list
    assert star_generation_1[:4] == [2, 1, 1, 1]
    assert len(star_generation_1) == 561897
    star_generation_2 = json.loads(response.json()["star_generation"]["2"])
    assert type(star_generation_2) is list
    assert star_generation_2 == [1]
    assert len(star_generation_2) == 1
    star_generation_3 = json.loads(response.json()["star_generation"]["3"])
    assert type(star_generation_3) is list
    assert star_generation_3[:4] == [1, 1, 1, 1]
    assert len(star_generation_3) == 173607


def test_post_advanced_star_groupid_251():
    groupid_list = []
    for i in range(1, 30):
        groupid_list.append(str(i))
    response = client.post("/pig/251/star/GroupID/", data='[' + ', '.join(groupid_list) + ']')
    utils.common_positive_tests(response)
    star_groupid_4 = json.loads(response.json()["star_groupid"]["4"])
    assert type(star_groupid_4) is list
    assert star_groupid_4[1000:1004] == [4, 4, 4, 4]
    assert len(star_groupid_4) == 206388
    star_groupid_5 = json.loads(response.json()["star_groupid"]["5"])
    assert type(star_groupid_5) is list
    assert star_groupid_5[:4] == [5, 5, 5, 5]
    assert len(star_groupid_5) == 83207
    star_groupid_6 = json.loads(response.json()["star_groupid"]["6"])
    assert type(star_groupid_6) is list
    assert star_groupid_6[:4] == [6, 6, 6, 6]
    assert len(star_groupid_6) == 112913


def test_post_advanced_star_position_251():
    groupid_list = []
    for i in range(1, 30):
        groupid_list.append(str(i))
    response = client.post("/pig/251/star/Position/", data='[' + ', '.join(groupid_list) + ']')
    utils.common_positive_tests(response)
    star_position_7 = json.loads(response.json()["star_position"]["7"])
    assert type(star_position_7) is list
    assert star_position_7[0] == [15306.750499744992, 146851.4949004134, 290343.8793858092]
    assert len(star_position_7) == 72130
    star_position_8 = json.loads(response.json()["star_position"]["8"])
    assert type(star_position_8) is list
    assert star_position_8[0] == [72839.80296707667, 195137.84803168938, 229726.26036081064]
    assert len(star_position_8) == 112659
    star_position_9 = json.loads(response.json()["star_position"]["9"])
    assert type(star_position_9) is list
    assert star_position_9[0] == [40394.3379824241, 38879.60468057035, 388657.5242690556]
    assert len(star_position_9) == 103097


def test_post_advanced_star_potential_251():
    groupid_list = []
    for i in range(10, 30):
        groupid_list.append(str(i))
    response = client.post("/pig/251/star/Potential/", data='[' + ', '.join(groupid_list) + ']')
    utils.common_positive_tests(response)
    star_potential_10 = json.loads(response.json()["star_potential"]["10"])
    assert type(star_potential_10) is list
    assert star_potential_10[:4] == [-293036.9375, -289590.84375, -292476.09375, -292596.40625]
    assert len(star_potential_10) == 98685
    star_potential_11 = json.loads(response.json()["star_potential"]["11"])
    assert type(star_potential_11) is list
    assert star_potential_11[:4] == [109452.8671875, 76191.0546875, 75398.890625, 77083.0703125]
    assert len(star_potential_11) == 140880
    star_potential_12 = json.loads(response.json()["star_potential"]["12"])
    assert type(star_potential_12) is list
    assert star_potential_12[:4] == [-336633.625, -331236.21875, -327860.375, -327338.78125]
    assert len(star_potential_12) == 154946


def test_post_advanced_star_velocity_251():
    groupid_list = []
    for i in range(10, 20):
        groupid_list.append(str(i))
    response = client.post("/pig/251/star/Velocity/", data='[' + ', '.join(groupid_list) + ']')
    utils.common_positive_tests(response)
    star_velocity_13 = json.loads(response.json()["star_velocity"]["13"])
    assert type(star_velocity_13) is list
    assert star_velocity_13[0] == [85.484130859375, -6.347171306610107, -15.724801063537598]
    assert len(star_velocity_13) == 124345
    star_velocity_14 = json.loads(response.json()["star_velocity"]["14"])
    assert type(star_velocity_14) is list
    assert star_velocity_14[0] == [29.978708267211914, 6.427834510803223, -15.628321647644043]
    assert len(star_velocity_14) == 137328
    star_velocity_15 = json.loads(response.json()["star_velocity"]["15"])
    assert type(star_velocity_15) is list
    assert star_velocity_15[0] == [37.52377700805664, -45.30293273925781, 40.19329833984375]
    assert len(star_velocity_15) == 133705


def test_post_advanced_star_mass_251():
    groupid_list = []
    for i in range(15, 25):
        groupid_list.append(str(i))
    response = client.post("/pig/251/star/Mass/", data='[' + ', '.join(groupid_list) + ']')
    utils.common_positive_tests(response)
    star_mass_16 = json.loads(response.json()["star_mass"]["16"])
    assert type(star_mass_16) is list
    assert star_mass_16[0] == 5.9055611927760765e-05
    assert len(star_mass_16) == 90938
    star_mass_17 = json.loads(response.json()["star_mass"]["17"])
    assert type(star_mass_17) is list
    assert star_mass_17[0] == 5.9055611927760765e-05
    assert len(star_mass_17) == 84443
    star_mass_18 = json.loads(response.json()["star_mass"]["18"])
    assert type(star_mass_18) is list
    assert star_mass_18[0] == 5.9055611927760765e-05
    assert len(star_mass_18) == 91087


def test_post_advanced_star_metallicity_251():
    groupid_list = []
    for i in range(15, 25):
        groupid_list.append(str(i))
    response = client.post("/pig/251/star/Metallicity/", data='[' + ', '.join(groupid_list) + ']')
    utils.common_positive_tests(response)
    star_metallicity_19 = json.loads(response.json()["star_metallicity"]["19"])
    assert type(star_metallicity_19) is list
    assert star_metallicity_19[:4] == [0.0012646712129935622, 6.0607515479205176e-05, 3.3099680877057835e-05,
                                       2.955297168227844e-05]
    assert len(star_metallicity_19) == 124501
    star_metallicity_20 = json.loads(response.json()["star_metallicity"]["20"])
    assert type(star_metallicity_20) is list
    assert star_metallicity_20[:4] == [0.0029382354114204645, 0.00031041487818583846, 0.0022197291254997253,
                                       0.003966968506574631]
    assert len(star_metallicity_20) == 91037
    star_metallicity_21 = json.loads(response.json()["star_metallicity"]["21"])
    assert type(star_metallicity_21) is list
    assert star_metallicity_21[:4] == [3.0326231353683397e-05, 5.4236138566921e-06, 0.00040298831299878657,
                                       0.0008918109233491123]
    assert len(star_metallicity_21) == 130522


def test_post_advanced_star_starformationtime_251():
    groupid_list = []
    for i in range(15, 25):
        groupid_list.append(str(i))
    response = client.post("/pig/251/star/StarFormationTime/", data='[' + ', '.join(groupid_list) + ']')
    utils.common_positive_tests(response)
    star_sft_22 = json.loads(response.json()["star_starformationtime"]["22"])
    assert type(star_sft_22) is list
    assert star_sft_22[:4] == [0.12779149413108826, 0.1142561063170433, 0.11241203546524048, 0.10575153678655624]
    assert len(star_sft_22) == 61896
    star_sft_23 = json.loads(response.json()["star_starformationtime"]["23"])
    assert type(star_sft_23) is list
    assert star_sft_23[:4] == [0.10786198079586029, 0.07991418242454529, 0.08404412865638733, 0.10528453439474106]
    assert len(star_sft_23) == 122115
    star_sft_24 = json.loads(response.json()["star_starformationtime"]["24"])
    assert type(star_sft_24) is list
    assert star_sft_24[:4] == [0.1294180303812027, 0.12327970564365387, 0.12431872636079788, 0.12420389801263809]
    assert len(star_sft_24) == 75418
