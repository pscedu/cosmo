import json

from fastapi.testclient import TestClient

from ..main import app
from . import utils

client = TestClient(app)


def test_get_pig():
    response = client.get("/pig/")
    utils.common_positive_tests(response)
    pig_list = response.json()["LIST"]
    for pig in pig_list:
        if pig["id"] == "244":
            assert pig["name"] == "PIG_244"
            assert pig["num_halos"] == 282939566
            assert pig["time"] == 6.750000008196768
        elif pig["id"] == "251":
            assert pig["name"] == "PIG_251"
            assert pig["num_halos"] == 286036300
            assert pig["time"] == 6.700000064799543
        elif pig["id"] == "271":
            assert pig["name"] == "PIG_271"
            assert pig["num_halos"] == 294288056
            assert pig["time"] == 6.560000154967445


def test_get_pig_244():
    response = client.get("/pig/244")
    utils.common_positive_tests(response)
    pig_244 = response.json()
    assert pig_244["subdirs"] == [
        "fofgroup",
        "gas",
        "dm",
        "star",
        "bh"
    ]
    assert pig_244["num_gas"] == 18949544012
    assert pig_244["num_dm"] == 20702705412
    assert pig_244["num_star"] == 560638945
    assert pig_244["num_bh"] == 219666


def test_get_pig_251():
    response = client.get("/pig/251")
    utils.common_positive_tests(response)
    pig_251 = response.json()
    assert pig_251["subdirs"] == [
        "fofgroup",
        "gas",
        "dm",
        "star",
        "bh"
    ]
    assert pig_251["num_gas"] == 19358022252
    assert pig_251["num_dm"] == 21165203462
    assert pig_251["num_star"] == 587619843
    assert pig_251["num_bh"] == 235967


def test_get_pig_271():
    response = client.get("/pig/271")
    utils.common_positive_tests(response)
    pig_271 = response.json()
    assert pig_271["subdirs"] == [
        "fofgroup",
        "gas",
        "dm",
        "star",
        "bh"
    ]
    assert pig_271["num_gas"] == 20556534261
    assert pig_271["num_dm"] == 22490179360
    assert pig_271["num_star"] == 670401945
    assert pig_271["num_bh"] == 260639


def test_get_fofgroup_251():
    response = client.get("/pig/251/fofgroup")
    utils.common_positive_tests(response)
    pig_251 = response.json()
    assert pig_251["fof_subdirs"] == [
        "Imom",
        "GroupID",
        "Mass",
        "Jmom",
        "OffsetByType",
        "BlackholeMass",
        "LengthByType",
        "FirstPos",
        "MassCenterPosition",
        "BlackholeAccretionRate",
        "MinID",
        "MassByType",
        "MassCenterVelocity",
        "StarFormationRate"
    ]


def test_get_dm_244():
    response = client.get("/pig/244/dm")
    utils.common_positive_tests(response)
    pig_244 = response.json()
    assert pig_244["ptype"] == "dm"
    assert pig_244["subdirs"] == [
        "ID",
        "Generation",
        "Position",
        "GroupID",
        "Velocity",
        "Potential"
    ]


def test_get_gas_251():
    response = client.get("/pig/251/gas")
    utils.common_positive_tests(response)
    pig_251 = response.json()
    assert pig_251["ptype"] == "gas"
    assert pig_251["subdirs"] == [
        "JUV",
        "Mass",
        "Density",
        "Potential",
        "ElectronAbundance",
        "Pressure",
        "SmoothingLength",
        "H2Fraction",
        "Position",
        "GroupID",
        "InternalEnergy",
        "StarFormationRate",
        "EgyWtDensity",
        "Entropy",
        "ID",
        "Generation",
        "Metallicity",
        "NeutralHydrogenFraction",
        "Velocity"
    ]


def test_get_star_271():
    response = client.get("/pig/271/star")
    utils.common_positive_tests(response)
    pig_271 = response.json()
    assert pig_271["ptype"] == "star"
    assert pig_271["subdirs"] == [
        "Generation",
        "StarFormationTime",
        "ID",
        "Potential",
        "GroupID",
        "Velocity",
        "Mass",
        "Metallicity",
        "Position"
    ]
