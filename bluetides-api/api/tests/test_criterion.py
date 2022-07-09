import json

from fastapi.testclient import TestClient

from ..main import app
from . import utils

client = TestClient(app)


# def test_criterion_positive_bhmass_271():
#     response = client.get("/pig/271/search/bh/BlackholeMass/bh_mass", params={"min_range": 5e-3, "max_range": 1e-2})
#     utils.common_positive_tests(response)
#     idlist = response.json().keys()
#     idlist = sorted([int(i) for i in idlist])
#     idlist = [str(i) for i in idlist]
#     assert idlist[:10] == [str(i) for i in [0, 2, 7, 8, 11, 14, 18, 19, 29, 34]]
#     data = json.loads(response.json()[idlist[10]])
#     assert type(data) is list
#     assert len(data) == 5
#     assert abs(data[2] - 4.1642028e-04) < 1e-10


# def test_criterion_positive_bhmass_251():
#     response = client.get("/pig/251/search/gas/Position/bh_mass", params={"min_range": 1e-2, "max_range": 5e-2})
#     utils.common_positive_tests(response)
#     idlist = response.json().keys()
#     idlist = sorted([int(i) for i in idlist])
#     idlist = [str(i) for i in idlist]
#     assert idlist[:10] == [str(i) for i in [0, 2, 3, 7, 9, 10, 11, 13, 14, 15]]
#     data = json.loads(response.json()[idlist[10]])
#     assert type(data) is list
#     assert len(data) == 87054
#     assert data[50] == [53527.46364022932, 331483.58928109781, 90276.19566488444]

# def test_criterion_positive_gasmass_271():
#     response = client.get("/pig/271/search/bh/BlackholeAccretionRate/gas_mass",params={"min_range":5e-3,"max_range":1e-2})
#     utils.common_positive_tests(response)
#     idlist = response.json().keys()
#     idlist = sorted([int(i) for i in idlist])
#     idlist = [str(i) for i in idlist]
#     assert idlist[:10] == [str(i) for i in [0,2,7,8,11,14,18,19,29,34]]
#     data = json.loads(response.json()[idlist[10]])
#     assert type(data) is list
#     assert len(data) == 5
#     assert abs(data[2] - 4.1642028e-04) < 1e-10


# def test_criterion_positive_gasmass_251():
#     response = client.get("/pig/251/search/star/StarFormationTime/gas_mass",params={"min_range":1e-2,"max_range":5e-2})
#     utils.common_positive_tests(response)
#     idlist = response.json().keys()
#     idlist = sorted([int(i) for i in idlist])
#     idlist = [str(i) for i in idlist]
#     assert idlist[:10] == [str(i) for i in [0, 2, 3, 7, 9, 10, 11, 13, 14, 15]]
#     data = json.loads(response.json()[idlist[10]])
#     assert type(data) is list
#     assert len(data) == 87054
#     assert data[50] == [53527.46364022932, 331483.58928109781 ,  90276.19566488444]
