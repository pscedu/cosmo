import json

from fastapi.testclient import TestClient

from ..main import app
from . import utils

client = TestClient(app)


def test_get_negative_gas():
    utils.test_get_negative("gas")


### endpoint: /pig/{id}/gas/position/{group_id}
# Basic positive tests
def test_get_gas_position_251():
    response = client.get("/pig/251/gas/Position/1")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 446499*3 array list
    gas_position = json.loads(response.json()["gas_position"])
    assert type(gas_position) is list
    assert gas_position[0] == [278202.3184792972, 28013.68036349728, 248672.55276327548]
    assert len(gas_position[0]) == 3
    assert len(gas_position) == 446499


def test_get_gas_position_271():
    response = client.get("/pig/271/gas/Position/1")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 513379*3 array list
    gas_position = json.loads(response.json()["gas_position"])
    assert type(gas_position) is list
    assert gas_position[0] == [278198.07020316395, 27948.384391798045, 248697.5992484129]
    assert len(gas_position[0]) == 3
    assert len(gas_position) == 513379


def test_get_gas_position_largeID():
    response = client.get("/pig/251/gas/Position/2117968")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 804*3 array list
    gas_position = json.loads(response.json()["gas_position"])
    assert type(gas_position) is list
    assert gas_position[3] == [198335.0403950171, 40257.09799530143, 189707.9848941324]
    assert len(gas_position[0]) == 3
    assert len(gas_position) == 804


### endpoint: /pig/{id}/gas/electron/{group_id}
# Basic positive tests
def test_get_gas_electron_251():
    response = client.get("/pig/251/gas/ElectronAbundance/1")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas electron data should be a 446499*1 array list
    gas_electron = json.loads(response.json()["gas_electronabundance"])
    assert type(gas_electron) is list
    assert gas_electron[0] == 1.157894253730774
    assert len(gas_electron) == 446499


def test_get_gas_electron_271():
    response = client.get("/pig/271/gas/ElectronAbundance/1")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas electron data should be a 513379*1 array list
    gas_electron = json.loads(response.json()["gas_electronabundance"])
    assert type(gas_electron) is list
    assert gas_electron[0] == 1.157894492149353
    assert len(gas_electron) == 513379


### endpoint: /pig/{id}/gas/H2fraction/{group_id}
# Basic positive tests
def test_get_gas_h2fraction_251():
    response = client.get("/pig/251/gas/H2Fraction/1")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas h2fraction data should be a 446499*1 array list
    gas_h2fraction = json.loads(response.json()["gas_h2fraction"])
    assert type(gas_h2fraction) is list
    assert gas_h2fraction[0] == 0.0
    assert gas_h2fraction[100000] == 0.9962370991706848
    assert len(gas_h2fraction) == 446499


def test_get_gas_h2fraction_271():
    response = client.get("/pig/271/gas/H2Fraction/1")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas h2fraction data should be a 513379*1 array list
    gas_h2fraction = json.loads(response.json()["gas_h2fraction"])
    assert type(gas_h2fraction) is list
    assert gas_h2fraction[0] == 0.0
    assert gas_h2fraction[100000] == 0.13368326425552368
    assert len(gas_h2fraction) == 513379


### endpoint: /pig/{id}/gas/InternalEnergy/{group_id}
# Basic positive tests
def test_get_gas_internal_energy_251():
    response = client.get("/pig/251/gas/InternalEnergy/1")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas InternalEnergy data should be a 446499*1 array list
    gas_internal_energy = json.loads(response.json()["gas_internalenergy"])
    assert type(gas_internal_energy) is list
    assert gas_internal_energy[0] == 112487.609375
    assert len(gas_internal_energy) == 446499


def test_get_gas_internal_energy_271():
    response = client.get("/pig/271/gas/InternalEnergy/1")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas InternalEnergy data should be a 513379*1 array list
    gas_internal_energy = json.loads(response.json()["gas_internalenergy"])
    assert type(gas_internal_energy) is list
    assert gas_internal_energy[0] == 163354.578125
    assert len(gas_internal_energy) == 513379


### endpoint: /pig/{id}/gas/Density/{group_id}
# Basic positive tests
def test_get_gas_density_251():
    response = client.get("/pig/251/gas/Density/1")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas Density data should be a 446499*1 array list
    gas_density = json.loads(response.json()["gas_density"])
    assert type(gas_density) is list
    assert gas_density[0] == 2.9312253957414214e-08
    assert gas_density[:4] == [2.9312253957414214e-08, 3.0495591829549085e-08, 3.838168538550235e-08,
                               4.375229067932196e-08]
    assert len(gas_density) == 446499


def test_get_gas_density_271():
    response = client.get("/pig/271/gas/Density/1")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas Density data should be a 513379*1 array list
    gas_density = json.loads(response.json()["gas_density"])
    assert type(gas_density) is list
    assert gas_density[0] == 2.121526954113051e-08
    assert gas_density[:4] == [2.121526954113051e-08, 2.48780214207045e-08, 3.295386008517198e-08,
                               3.252150193588932e-08]
    assert len(gas_density) == 513379


### endpoint: /pig/{id}/gas/Entropy/{group_id}
# Basic positive tests
def test_get_gas_entropy_251():
    response = client.get("/pig/251/gas/Entropy/100")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas Entropy data should be a 68419*1 array list
    gas_entropy = json.loads(response.json()["gas_entropy"])
    assert type(gas_entropy) is list
    assert gas_entropy[0] == 2959285.5
    assert gas_entropy[:4] == [2959285.5, 77811.4609375, 100789.5625, 111917.515625]
    assert len(gas_entropy) == 68419


def test_get_gas_entropy_271():
    response = client.get("/pig/271/gas/Entropy/100")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas Entropy data should be a 77457*1 array list
    gas_entropy = json.loads(response.json()["gas_entropy"])
    assert type(gas_entropy) is list
    assert gas_entropy[0] == 40433988.0
    assert gas_entropy[:4] == [40433988.0, 11036351.0, 22856564.0, 211525.53125]
    assert len(gas_entropy) == 77457


### endpoint: /pig/{id}/gas/JUV/{group_id}
# Basic positive tests
def test_get_gas_juv_251():
    response = client.get("/pig/251/gas/JUV/10")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas JUV data should be a 134377*1 array list
    gas_juv = json.loads(response.json()["gas_juv"])
    assert type(gas_juv) is list
    assert gas_juv[0] == 9.999999682655225e-22
    assert len(gas_juv) == 134377


def test_get_gas_juv_271():
    response = client.get("/pig/271/gas/JUV/10")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas JUV data should be a 145402*1 array list
    gas_juv = json.loads(response.json()["gas_juv"])
    assert type(gas_juv) is list
    assert gas_juv[0] == 9.999999682655225e-22
    assert len(gas_juv) == 145402


### endpoint: /pig/{id}/gas/NeutralHydrogenFraction/{group_id}
# Basic positive tests
def test_get_gas_nhf_251():
    response = client.get("/pig/251/gas/NeutralHydrogenFraction/20")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas NeutralHydrogenFraction data should be a 102446*1 array list
    gas_nhf = json.loads(response.json()["gas_neutralhydrogenfraction"])
    assert type(gas_nhf) is list
    assert gas_nhf[0] == 1.5026954542918247e-06
    assert len(gas_nhf) == 102446


def test_get_gas_nhf_271():
    response = client.get("/pig/271/gas/NeutralHydrogenFraction/20")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas NeutralHydrogenFraction data should be a 119976*1 array list
    gas_nhf = json.loads(response.json()["gas_neutralhydrogenfraction"])
    assert type(gas_nhf) is list
    assert gas_nhf[0] == 6.849857072666055e-06
    assert len(gas_nhf) == 119976


### endpoint: /pig/{id}/gas/Pressure/{group_id}
# Basic positive tests
def test_get_gas_pressure_251():
    response = client.get("/pig/251/gas/Pressure/30")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas Pressure data should be a 83500*1 array list
    gas_pressure = json.loads(response.json()["gas_pressure"])
    assert type(gas_pressure) is list
    assert gas_pressure[0] == 1.6903873984119855e-05
    assert gas_pressure[:4] == [1.6903873984119855e-05, 1.3225580005382653e-05, 1.914056383611751e-06,
                                4.885966973233735e-06]
    assert len(gas_pressure) == 83500


def test_get_gas_pressure_271():
    response = client.get("/pig/271/gas/Pressure/30")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas Pressure data should be a 102438*1 array list
    gas_pressure = json.loads(response.json()["gas_pressure"])
    assert type(gas_pressure) is list
    assert gas_pressure[0] == 6.205591773777996e-08
    assert gas_pressure[:4] == [6.205591773777996e-08, 1.3783197800876223e-06, 3.136743202958314e-07,
                                1.2491647112256032e-06]
    assert len(gas_pressure) == 102438


### endpoint: /pig/{id}/gas/Velocity/{group_id}
# Basic positive tests
def test_get_gas_velocity_251():
    response = client.get("/pig/251/gas/Velocity/30")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas Velocity data should be a 83500*1 array list
    gas_velocity = json.loads(response.json()["gas_velocity"])
    assert type(gas_velocity) is list
    assert gas_velocity[0] == [-65.1724624633789, 24.529680252075195, 38.377403259277344]
    assert len(gas_velocity) == 83500


def test_get_gas_velocity_271():
    response = client.get("/pig/271/gas/Velocity/30")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas Velocity data should be a 102438*1 array list
    gas_velocity = json.loads(response.json()["gas_velocity"])
    assert type(gas_velocity) is list
    assert gas_velocity[0] == [61.37261962890625, 30.83819007873535, 15.464899063110352]
    assert len(gas_velocity) == 102438


### endpoint: /pig/{id}/gas/EgyWtDensity/{group_id}
# Basic positive tests
def test_get_gas_egywtdensity_251():
    response = client.get("/pig/251/gas/EgyWtDensity/40")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas EgyWtDensity data should be a 75980*1 array list
    gas_egywtdensity = json.loads(response.json()["gas_egywtdensity"])
    assert type(gas_egywtdensity) is list
    assert gas_egywtdensity[0] == 1.1311906078503853e-08
    assert gas_egywtdensity[:4] == [1.1311906078503853e-08, 1.0542879458341758e-08, 4.6664844433053077e-08,
                                    6.323491419379934e-08]
    assert len(gas_egywtdensity) == 75980


def test_get_gas_egywtdensity_271():
    response = client.get("/pig/271/gas/EgyWtDensity/40")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas EgyWtDensity data should be a 51832*1 array list
    gas_egywtdensity = json.loads(response.json()["gas_egywtdensity"])
    assert type(gas_egywtdensity) is list
    assert gas_egywtdensity[0] == 1.3695033374006016e-07
    assert gas_egywtdensity[:4] == [1.3695033374006016e-07, 1.5859635595916188e-06, 4.7282750159638454e-08,
                                    3.3221699595742393e-06]
    assert len(gas_egywtdensity) == 51832


### endpoint: /pig/{id}/gas/Generation/{group_id}
# Basic positive tests
def test_get_gas_generation_251():
    response = client.get("/pig/251/gas/Generation/40")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas Generation data should be a 75980*1 array list
    gas_generation = json.loads(response.json()["gas_generation"])
    assert type(gas_generation) is list
    assert gas_generation[10000] == 1
    assert len(gas_generation) == 75980


def test_get_gas_generation_271():
    response = client.get("/pig/271/gas/Generation/40")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas Generation data should be a 51832*1 array list
    gas_generation = json.loads(response.json()["gas_generation"])
    assert type(gas_generation) is list
    assert gas_generation[15000] == 0
    assert len(gas_generation) == 51832


### endpoint: /pig/{id}/gas/Mass/{group_id}
# Basic positive tests
def test_get_gas_mass_251():
    response = client.get("/pig/251/gas/Mass/50")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas Mass data should be a 76352*1 array list
    gas_mass = json.loads(response.json()["gas_mass"])
    assert type(gas_mass) is list
    assert gas_mass[0] == 0.00023622244771104306
    assert gas_mass[:4] == [0.00023622244771104306, 0.00023622244771104306, 0.00023622244771104306,
                            0.00023622244771104306]
    assert len(gas_mass) == 76352


def test_get_gas_mass_271():
    response = client.get("/pig/271/gas/Mass/50")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas Mass data should be a 86405*1 array list
    gas_mass = json.loads(response.json()["gas_mass"])
    assert type(gas_mass) is list
    assert gas_mass[0] == 0.00023622244771104306
    assert gas_mass[:4] == [0.00023622244771104306, 0.00023622244771104306, 0.00023622244771104306,
                            0.00023622244771104306]
    assert len(gas_mass) == 86405


### endpoint: /pig/{id}/gas/SmoothingLength/{group_id}
# Basic positive tests
def test_get_gas_smoothinglength_251():
    response = client.get("/pig/251/gas/SmoothingLength/60")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas SmoothingLength data should be a 68059*1 array list
    gas_smoothinglength = json.loads(response.json()["gas_smoothinglength"])
    assert type(gas_smoothinglength) is list
    assert gas_smoothinglength[0] == 57.098350524902344
    assert gas_smoothinglength[:4] == [57.098350524902344, 31.1713924407959, 32.398929595947266, 25.489093780517578]
    assert len(gas_smoothinglength) == 68059


def test_get_gas_smoothinglength_271():
    response = client.get("/pig/271/gas/SmoothingLength/60")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas SmoothingLength data should be a 96354*1 array list
    gas_smoothinglength = json.loads(response.json()["gas_smoothinglength"])
    assert type(gas_smoothinglength) is list
    assert gas_smoothinglength[0] == 84.1534652709961
    assert gas_smoothinglength[:4] == [84.1534652709961, 97.58158874511719, 94.68399810791016, 81.02495574951172]
    assert len(gas_smoothinglength) == 96354


### endpoint: /pig/{id}/gas/GroupID/{group_id}
# Basic positive tests
def test_get_gas_groupid_251():
    response = client.get("/pig/251/gas/GroupID/70")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas GroupID data should be a 84132*1 array list
    gas_groupid = json.loads(response.json()["gas_groupid"])
    assert type(gas_groupid) is list
    assert gas_groupid[100] == 70
    assert gas_groupid[500] == 70
    assert len(gas_groupid) == 84132


def test_get_gas_groupid_271():
    response = client.get("/pig/271/gas/GroupID/80")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas GroupID data should be a 95309*1 array list
    gas_groupid = json.loads(response.json()["gas_groupid"])
    assert type(gas_groupid) is list
    assert gas_groupid[1000] == 80
    assert gas_groupid[2000] == 80
    assert len(gas_groupid) == 95309


### endpoint: /pig/{id}/gas/Metallicity/{group_id}
# Basic positive tests
def test_get_gas_metallicity_251():
    response = client.get("/pig/251/gas/Metallicity/80")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas Metallicity data should be a 84749*1 array list
    gas_metallicity = json.loads(response.json()["gas_metallicity"])
    assert type(gas_metallicity) is list
    assert gas_metallicity[1] == 6.301722169155255e-05
    assert gas_metallicity[7] == 3.587197852539248e-06
    assert len(gas_metallicity) == 84749


def test_get_gas_metallicity_271():
    response = client.get("/pig/271/gas/Metallicity/80")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas Metallicity data should be a 95309*1 array list
    gas_metallicity = json.loads(response.json()["gas_metallicity"])
    assert type(gas_metallicity) is list
    assert gas_metallicity[2] == 0.010519527830183506
    assert gas_metallicity[100] == 0.0
    assert len(gas_metallicity) == 95309


### endpoint: /pig/{id}/gas/Potential/{group_id}
# Basic positive tests
def test_get_gas_potential_251():
    response = client.get("/pig/251/gas/Potential/90")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas Potential data should be a 93123*1 array list
    gas_potential = json.loads(response.json()["gas_potential"])
    assert type(gas_potential) is list
    assert gas_potential[0] == -332538.125
    assert gas_potential[4] == -334103.46875
    assert len(gas_potential) == 93123


def test_get_gas_potential_271():
    response = client.get("/pig/271/gas/Potential/90")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas Potential data should be a 50143*1 array list
    gas_potential = json.loads(response.json()["gas_potential"])
    assert type(gas_potential) is list
    assert gas_potential[0] == -155053.03125
    assert gas_potential[:4] == [-155053.03125, -155029.625, -155162.640625, -155010.75]
    assert len(gas_potential) == 50143


### endpoint: /pig/{id}/gas/StarFormationRate/{group_id}
# Basic positive tests
def test_get_gas_starformationrate_251():
    response = client.get("/pig/251/gas/StarFormationRate/100")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas StarFormationRate data should be a 68419*1 array list
    gas_starformationrate = json.loads(response.json()["gas_starformationrate"])
    assert type(gas_starformationrate) is list
    assert gas_starformationrate[1000] == 0
    assert gas_starformationrate[5000] == 0.0003683421527966857
    assert len(gas_starformationrate) == 68419


def test_get_gas_starformationrate_271():
    response = client.get("/pig/271/gas/StarFormationRate/100")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas StarFormationRate data should be a 50143*1 array list
    gas_starformationrate = json.loads(response.json()["gas_starformationrate"])
    assert type(gas_starformationrate) is list
    assert gas_starformationrate[15000] == 0.016309794038534164
    assert gas_starformationrate[10000] == 0
    assert len(gas_starformationrate) == 77457


#################################################################################################


### tests for advanced gas query with post method
def test_post_advanced_gas_density_251():
    groupid_list = []
    for i in range(1, 300):
        groupid_list.append(str(i))
    response = client.post("/pig/251/gas/Density/", data='[' + ', '.join(groupid_list) + ']')
    utils.common_positive_tests(response)
    gas_density_1 = json.loads(response.json()["gas_density"]["1"])
    assert type(gas_density_1) is list
    assert gas_density_1[:4] == [2.9312253957414214e-08, 3.0495591829549085e-08, 3.838168538550235e-08,
                                 4.375229067932196e-08]
    assert len(gas_density_1) == 446499
    gas_density_2 = json.loads(response.json()["gas_density"]["2"])
    assert type(gas_density_2) is list
    assert gas_density_2[:4] == [6.8903700523037514e-09, 6.851533118634734e-09, 8.200615297937475e-09,
                                 7.598972118216807e-09]
    assert len(gas_density_2) == 700225
    gas_density_3 = json.loads(response.json()["gas_density"]["3"])
    assert type(gas_density_3) is list
    assert gas_density_3[:4] == [2.12554578382651e-08, 2.075496752240724e-08, 2.7879844211042837e-08,
                                 2.678831378943869e-08]
    assert len(gas_density_3) == 239021


def test_post_advanced_gas_entropy_251():
    groupid_list = []
    for i in range(4, 14):
        groupid_list.append(str(i))
    response = client.post("/pig/251/gas/Entropy/", data='[' + ', '.join(groupid_list) + ']')
    utils.common_positive_tests(response)
    gas_entropy_4 = json.loads(response.json()["gas_entropy"]["4"])
    assert type(gas_entropy_4) is list
    assert gas_entropy_4[:4] == [9321008.0, 53421.7734375, 63790.05859375, 53965.58984375]
    assert len(gas_entropy_4) == 125966
    gas_entropy_5 = json.loads(response.json()["gas_entropy"]["5"])
    assert type(gas_entropy_5) is list
    assert gas_entropy_5[:4] == [411603.28125, 146572.4375, 255028.5625, 110186.3046875]
    assert len(gas_entropy_5) == 172170
    gas_entropy_6 = json.loads(response.json()["gas_entropy"]["6"])
    assert type(gas_entropy_6) is list
    assert gas_entropy_6[:4] == [81743.9140625, 132288.1875, 73330.1796875, 104180.6171875]
    assert len(gas_entropy_6) == 154147


def test_post_advanced_gas_h2fraction_251():
    groupid_list = []
    for i in range(5, 10):
        groupid_list.append(str(i))
    response = client.post("/pig/251/gas/H2Fraction/", data='[' + ', '.join(groupid_list) + ']')
    utils.common_positive_tests(response)
    gas_h2fraction_7 = json.loads(response.json()["gas_h2fraction"]["7"])
    assert type(gas_h2fraction_7) is list
    assert gas_h2fraction_7[10000:10004] == [0.009490085765719414, 0, 0, 0]
    assert len(gas_h2fraction_7) == 177623
    gas_h2fraction_8 = json.loads(response.json()["gas_h2fraction"]["8"])
    assert type(gas_h2fraction_8) is list
    assert gas_h2fraction_8[20000:20004] == [0, 0, 0, 0.04939519986510277]
    assert len(gas_h2fraction_8) == 142821
    gas_h2fraction_9 = json.loads(response.json()["gas_h2fraction"]["9"])
    assert type(gas_h2fraction_9) is list
    assert gas_h2fraction_9[15000:15004] == [0.15932804346084595, 0, 0.0031604496762156487, 0]
    assert len(gas_h2fraction_9) == 140981


def test_get_advanced_gas_juv_251():
    groupid_list = []
    for i in range(10, 15):
        groupid_list.append(str(i))
    response = client.post("/pig/251/gas/JUV/", data='[' + ', '.join(groupid_list) + ']')
    utils.common_positive_tests(response)
    gas_juv_10 = json.loads(response.json()["gas_juv"]["10"])
    assert type(gas_juv_10) is list
    assert gas_juv_10[10000:10004] == [9.999999682655225e-22, 9.999999682655225e-22, 9.999999682655225e-22,
                                       9.999999682655225e-22]
    assert len(gas_juv_10) == 134377
    gas_juv_11 = json.loads(response.json()["gas_juv"]["11"])
    assert type(gas_juv_11) is list
    assert gas_juv_11[20000] == 9.999999682655225e-22
    assert len(gas_juv_11) == 102244
    gas_juv_12 = json.loads(response.json()["gas_juv"]["12"])
    assert type(gas_juv_12) is list
    assert gas_juv_12[15000] == 9.999999682655225e-22
    assert len(gas_juv_12) == 91408


def test_post_advanced_gas_nhf_251():
    groupid_list = []
    for i in range(10, 16):
        groupid_list.append(str(i))
    response = client.post("/pig/251/gas/NeutralHydrogenFraction/", data='[' + ', '.join(groupid_list) + ']')
    utils.common_positive_tests(response)
    gas_nhf_13 = json.loads(response.json()["gas_neutralhydrogenfraction"]["13"])
    assert type(gas_nhf_13) is list
    assert gas_nhf_13[:4] == [0.00016779893485363573, 0.001974311890080571, 0.0013231453485786915, 0.004058866761624813]
    assert len(gas_nhf_13) == 109887
    gas_nhf_14 = json.loads(response.json()["gas_neutralhydrogenfraction"]["14"])
    assert type(gas_nhf_14) is list
    assert gas_nhf_14[:4] == [1.6623314422758995e-06, 3.881593784171855e-06, 1.4636433661507908e-05,
                              0.021240321919322014]
    assert len(gas_nhf_14) == 101137
    gas_nhf_15 = json.loads(response.json()["gas_neutralhydrogenfraction"]["15"])
    assert type(gas_nhf_15) is list
    assert gas_nhf_15[:4] == [0.006793433800339699, 0.005498229991644621, 0.009771108627319336, 0.007732793223112822]
    assert len(gas_nhf_15) == 99544


def test_post_advanced_gas_pressure_251():
    groupid_list = []
    for i in range(15, 25):
        groupid_list.append(str(i))
    response = client.post("/pig/251/gas/Pressure/", data='[' + ', '.join(groupid_list) + ']')
    utils.common_positive_tests(response)
    gas_pressure_16 = json.loads(response.json()["gas_pressure"]["16"])
    assert type(gas_pressure_16) is list
    assert gas_pressure_16[:4] == [3.65005826097331e-06, 7.030094479887339e-07, 8.947169476414274e-07,
                                   1.1282971854598145e-06]
    assert len(gas_pressure_16) == 119751
    gas_pressure_17 = json.loads(response.json()["gas_pressure"]["17"])
    assert type(gas_pressure_17) is list
    assert gas_pressure_17[:4] == [1.4249569630919723e-06, 1.5151192656048806e-06, 8.5890900436425e-07,
                                   5.033523393649375e-07]
    assert len(gas_pressure_17) == 123411
    gas_pressure_18 = json.loads(response.json()["gas_pressure"]["18"])
    assert type(gas_pressure_18) is list
    assert gas_pressure_18[:4] == [1.0433600436954293e-06, 1.858478412941622e-06, 2.476672761986265e-06,
                                   4.140899363846984e-06]
    assert len(gas_pressure_18) == 119046


def test_post_advanced_gas_velocity_251():
    groupid_list = []
    for i in range(15, 25):
        groupid_list.append(str(i))
    response = client.post("/pig/251/gas/Velocity/", data='[' + ', '.join(groupid_list) + ']')
    utils.common_positive_tests(response)
    gas_velocity_19 = json.loads(response.json()["gas_velocity"]["19"])
    assert type(gas_velocity_19) is list
    assert gas_velocity_19[0] == [-10.421012878417969, -11.563729286193848, -8.927306175231934]
    assert len(gas_velocity_19) == 87054
    gas_velocity_20 = json.loads(response.json()["gas_velocity"]["20"])
    assert type(gas_velocity_20) is list
    assert gas_velocity_20[0] == [55.109683990478516, 4.177705764770508, -14.314995765686035]
    assert len(gas_velocity_20) == 102446
    gas_velocity_21 = json.loads(response.json()["gas_velocity"]["21"])
    assert type(gas_velocity_21) is list
    assert gas_velocity_21[0] == [-34.447486877441406, -1.5274184942245483, 37.998382568359375]
    assert len(gas_velocity_21) == 70998


def test_post_advanced_gas_egywtdensity_251():
    groupid_list = []
    for i in range(15, 25):
        groupid_list.append(str(i))
    response = client.post("/pig/251/gas/EgyWtDensity/", data='[' + ', '.join(groupid_list) + ']')
    utils.common_positive_tests(response)
    gas_egywtdensity_22 = json.loads(response.json()["gas_egywtdensity"]["22"])
    assert type(gas_egywtdensity_22) is list
    assert gas_egywtdensity_22[:4] == [2.2912860231372179e-07, 3.1595209293300286e-07, 1.8586334249448555e-07,
                                       1.6548617054468195e-07]
    assert len(gas_egywtdensity_22) == 116596
    gas_egywtdensity_23 = json.loads(response.json()["gas_egywtdensity"]["23"])
    assert type(gas_egywtdensity_23) is list
    assert gas_egywtdensity_23[:4] == [4.04710620571791e-09, 3.262977799067812e-08, 1.7940589458476097e-08,
                                       4.2827828394820244e-08]
    assert len(gas_egywtdensity_23) == 79297
    gas_egywtdensity_24 = json.loads(response.json()["gas_egywtdensity"]["24"])
    assert type(gas_egywtdensity_24) is list
    assert gas_egywtdensity_24[:4] == [0.0008164836326614022, 0.0009103499469347298, 0.0007278427365235984,
                                       0.0010858536697924137]
    assert len(gas_egywtdensity_24) == 110136


def test_post_advanced_gas_generation_251():
    groupid_list = []
    for i in range(25, 35):
        groupid_list.append(str(i))
    response = client.post("/pig/251/gas/Generation/", data='[' + ', '.join(groupid_list) + ']')
    utils.common_positive_tests(response)
    gas_generation_25 = json.loads(response.json()["gas_generation"]["25"])
    assert type(gas_generation_25) is list
    assert gas_generation_25[10000:10004] == [3, 0, 2, 2]
    assert len(gas_generation_25) == 88846
    gas_generation_26 = json.loads(response.json()["gas_generation"]["26"])
    assert type(gas_generation_26) is list
    assert gas_generation_26[10000:10004] == [0, 0, 1, 0]
    assert len(gas_generation_26) == 84177
    gas_generation_27 = json.loads(response.json()["gas_generation"]["27"])
    assert type(gas_generation_27) is list
    assert gas_generation_27[10000:10004] == [3, 1, 3, 1]
    assert len(gas_generation_27) == 102526


def test_post_advanced_gas_mass_251():
    groupid_list = []
    for i in range(25, 35):
        groupid_list.append(str(i))
    response = client.post("/pig/251/gas/Mass/", data='[' + ', '.join(groupid_list) + ']')
    utils.common_positive_tests(response)
    gas_mass_28 = json.loads(response.json()["gas_mass"]["28"])
    assert type(gas_mass_28) is list
    assert gas_mass_28[:4] == [0.00023622244771104306, 0.0001771668321453035, 0.00023622244771104306,
                               0.00023622244771104306]
    assert len(gas_mass_28) == 100721
    gas_mass_29 = json.loads(response.json()["gas_mass"]["29"])
    assert type(gas_mass_29) is list
    assert gas_mass_29[:4] == [0.00023622244771104306, 0.00023622244771104306, 0.00011811122385552153,
                               0.00023622244771104306]
    assert len(gas_mass_29) == 70201
    gas_mass_30 = json.loads(response.json()["gas_mass"]["30"])
    assert type(gas_mass_30) is list
    assert gas_mass_30[:4] == [0.00023622244771104306, 0.0001771668321453035, 0.00023622244771104306,
                               0.00023622244771104306]
    assert len(gas_mass_30) == 83500


def test_post_advanced_gas_position_251():
    groupid_list = []
    for i in range(25, 35):
        groupid_list.append(str(i))
    response = client.post("/pig/251/gas/Position/", data='[' + ', '.join(groupid_list) + ']')
    utils.common_positive_tests(response)
    gas_position_31 = json.loads(response.json()["gas_position"]["31"])
    assert type(gas_position_31) is list
    assert gas_position_31[0] == [261684.06480544538, 190740.5113315618, 283722.12778867374]
    assert len(gas_position_31) == 108047
    gas_position_32 = json.loads(response.json()["gas_position"]["32"])
    assert type(gas_position_32) is list
    assert gas_position_32[0] == [239949.80821999058, 360579.35982060776, 92336.4958515453]
    assert len(gas_position_32) == 110424
    gas_position_33 = json.loads(response.json()["gas_position"]["33"])
    assert type(gas_position_33) is list
    assert gas_position_33[0] == [146760.48069256212, 158676.33736712005, 243417.30848672]
    assert len(gas_position_33) == 93972


def test_post_advanced_gas_smoothinglength_251():
    groupid_list = []
    for i in range(30, 40):
        groupid_list.append(str(i))
    response = client.post("/pig/251/gas/SmoothingLength/", data='[' + ', '.join(groupid_list) + ']')
    utils.common_positive_tests(response)
    gas_smoothinglength_34 = json.loads(response.json()["gas_smoothinglength"]["34"])
    assert type(gas_smoothinglength_34) is list
    assert gas_smoothinglength_34[:4] == [38.94357681274414, 44.94118118286133, 91.891845703125, 53.394989013671875]
    assert len(gas_smoothinglength_34) == 90000
    gas_smoothinglength_35 = json.loads(response.json()["gas_smoothinglength"]["35"])
    assert type(gas_smoothinglength_35) is list
    assert gas_smoothinglength_35[:4] == [46.461490631103516, 46.1546745300293, 54.993202209472656, 50.32440185546875]
    assert len(gas_smoothinglength_35) == 112088
    gas_smoothinglength_36 = json.loads(response.json()["gas_smoothinglength"]["36"])
    assert type(gas_smoothinglength_36) is list
    assert gas_smoothinglength_36[:4] == [22.021921157836914, 23.436626434326172, 23.384023666381836, 22.77919578552246]
    assert len(gas_smoothinglength_36) == 51870


def test_post_advanced_gas_electronabundance_251():
    groupid_list = []
    for i in range(30, 40):
        groupid_list.append(str(i))
    response = client.post("/pig/251/gas/ElectronAbundance/", data='[' + ', '.join(groupid_list) + ']')
    utils.common_positive_tests(response)
    gas_electronabundance_37 = json.loads(response.json()["gas_electronabundance"]["37"])
    assert type(gas_electronabundance_37) is list
    assert gas_electronabundance_37[:4] == [1.0644114017486572, 1.0524873733520508, 1.0467177629470825,
                                            1.0695151090621948]
    assert len(gas_electronabundance_37) == 78470
    gas_electronabundance_38 = json.loads(response.json()["gas_electronabundance"]["38"])
    assert type(gas_electronabundance_38) is list
    assert gas_electronabundance_38[:4] == [1.0412324666976929, 1.0787979364395142, 1.0481164455413818,
                                            1.0394285917282104]
    assert len(gas_electronabundance_38) == 75265
    gas_electronabundance_39 = json.loads(response.json()["gas_electronabundance"]["39"])
    assert type(gas_electronabundance_39) is list
    assert gas_electronabundance_39[:4] == [1.0403106212615967, 1.0531127452850342, 1.047825574874878,
                                            1.0436707735061646]
    assert len(gas_electronabundance_39) == 72586


def test_post_advanced_gas_groupid_251():
    groupid_list = []
    for i in range(40, 50):
        groupid_list.append(str(i))
    response = client.post("/pig/251/gas/GroupID/", data='[' + ', '.join(groupid_list) + ']')
    utils.common_positive_tests(response)
    gas_groupid_40 = json.loads(response.json()["gas_groupid"]["40"])
    assert type(gas_groupid_40) is list
    assert gas_groupid_40[:4] == [40, 40, 40, 40]
    assert len(gas_groupid_40) == 75980
    gas_groupid_41 = json.loads(response.json()["gas_groupid"]["41"])
    assert type(gas_groupid_41) is list
    assert gas_groupid_41[:4] == [41, 41, 41, 41]
    assert len(gas_groupid_41) == 51734
    gas_groupid_42 = json.loads(response.json()["gas_groupid"]["42"])
    assert type(gas_groupid_42) is list
    assert gas_groupid_42[:4] == [42, 42, 42, 42]
    assert len(gas_groupid_42) == 97485


def test_post_advanced_gas_internalenergy_251():
    groupid_list = []
    for i in range(40, 50):
        groupid_list.append(str(i))
    response = client.post("/pig/251/gas/InternalEnergy/", data='[' + ', '.join(groupid_list) + ']')
    utils.common_positive_tests(response)
    gas_internalenergy_43 = json.loads(response.json()["gas_internalenergy"]["43"])
    assert type(gas_internalenergy_43) is list
    assert gas_internalenergy_43[:4] == [605.2543334960938, 26076.884765625, 372.16851806640625, 2094.2353515625]
    assert len(gas_internalenergy_43) == 113564
    gas_internalenergy_44 = json.loads(response.json()["gas_internalenergy"]["44"])
    assert type(gas_internalenergy_44) is list
    assert gas_internalenergy_44[:4] == [9611.853515625, 16080.3818359375, 260.51898193359375, 270.278076171875]
    assert len(gas_internalenergy_44) == 97688
    gas_internalenergy_45 = json.loads(response.json()["gas_internalenergy"]["45"])
    assert type(gas_internalenergy_45) is list
    assert gas_internalenergy_45[:4] == [108447.421875, 89918.0234375, 104446.4921875, 67976.984375]
    assert len(gas_internalenergy_45) == 54896


def test_post_advanced_gas_metallicity_251():
    groupid_list = []
    for i in range(45, 50):
        groupid_list.append(str(i))
    response = client.post("/pig/251/gas/Metallicity/", data='[' + ', '.join(groupid_list) + ']')
    utils.common_positive_tests(response)
    gas_metallicity_46 = json.loads(response.json()["gas_metallicity"]["46"])
    assert type(gas_metallicity_46) is list
    assert gas_metallicity_46[8:12] == [4.771889507537708e-05, 0.0, 0.0, 1.0208200365013909e-05]
    assert len(gas_metallicity_46) == 89250
    gas_metallicity_47 = json.loads(response.json()["gas_metallicity"]["47"])
    assert type(gas_metallicity_47) is list
    assert gas_metallicity_47[:4] == [3.263609323767014e-05, 0.0, 0.0, 0.0]
    assert len(gas_metallicity_47) == 80899
    gas_metallicity_48 = json.loads(response.json()["gas_metallicity"]["48"])
    assert type(gas_metallicity_48) is list
    assert gas_metallicity_48[4:10] == [0.00017874645709525794, 0.0, 0.0, 0.0, 0.0, 1.3768882126896642e-05]
    assert len(gas_metallicity_48) == 74641


def test_get_advanced_gas_potential_251():
    groupid_list = []
    for i in range(45, 55):
        groupid_list.append(str(i))
    response = client.post("/pig/251/gas/Potential/", data='[' + ', '.join(groupid_list) + ']')
    utils.common_positive_tests(response)
    gas_potential_49 = json.loads(response.json()["gas_potential"]["49"])
    assert type(gas_potential_49) is list
    assert gas_potential_49[:4] == [-331288.28125, -333441.75, -333552.75, -336382.40625]
    assert len(gas_potential_49) == 95157
    gas_potential_50 = json.loads(response.json()["gas_potential"]["50"])
    assert type(gas_potential_50) is list
    assert gas_potential_50[:4] == [-155418.140625, -155361.90625, -155329.9375, -155540.046875]
    assert len(gas_potential_50) == 76352
    gas_potential_51 = json.loads(response.json()["gas_potential"]["51"])
    assert type(gas_potential_51) is list
    assert gas_potential_51[:4] == [-358705.3125, -358668.9375, -358822.28125, -358974.9375]
    assert len(gas_potential_51) == 93642


def test_post_advanced_gas_starformationrate_251():
    groupid_list = []
    for i in range(50, 55):
        groupid_list.append(str(i))
    response = client.post("/pig/251/gas/StarFormationRate/", data='[' + ', '.join(groupid_list) + ']')
    utils.common_positive_tests(response)
    gas_sfr_52 = json.loads(response.json()["gas_starformationrate"]["52"])
    assert type(gas_sfr_52) is list
    assert gas_sfr_52[2000:2004] == [0.0037621604278683662, 0.00268386909738183, 0.0022346717305481434,
                                     0.001048594480380416]
    assert len(gas_sfr_52) == 101766
    gas_sfr_53 = json.loads(response.json()["gas_starformationrate"]["53"])
    assert type(gas_sfr_53) is list
    assert gas_sfr_53[2000:2004] == [0.004331901669502258, 0.0017521338304504752, 0.0037914812564849854,
                                     0.0016839097952470183]
    assert len(gas_sfr_53) == 93875
    gas_sfr_54 = json.loads(response.json()["gas_starformationrate"]["54"])
    assert type(gas_sfr_54) is list
    assert gas_sfr_54[2000:2004] == [0, 0, 0, 0]
    assert len(gas_sfr_54) == 61188
