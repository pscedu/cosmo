PIG_BASE_DIR = '/bluetides3/'

WEB_URL = "http://bluetides.psc.edu/"

BASE_API_URL = "http://bluetides-api.psc.edu/"
BASE_DATA_SHARING_PORTAL_URL = "http://bluetides-portal.psc.edu/"
BASE_ORIGINAL_BLUETIDES_URL = "http://bluetides-project.org/"
DATA_STRUCTURE = BASE_API_URL + "data-structure/"
API_REFERENCE = BASE_API_URL + "api-reference/"
API_TUTORIAL = BASE_API_URL + "tutorial/"

#  metadata for tags
tags_metadata = [
    {
        "name": "pig",
        "description": "Get the snapshot info of PIG folders.",
    },
    {
        "name": "lengthbytype",
        "description": "Get the lengthbytype of particles.",
    },
    {
        "name": "particle",
        "description": "Get particle data.",
    },
    {
        "name": "advanced",
        "description": "Searching criterion by field and bulk queries for halo data.",
    },
]


        
# 404 response description
response_404 = {}
response_404["pig_id"] = \
    {
        "description": "PIG folder does not exist",
        "detail": "PIG_{id} folder does not exist, and should be in ['PIG_208', 'PIG_230', 'PIG_237', 'PIG_216', 'PIG_265', 'PIG_244', 'PIG_271', 'PIG_258', 'PIG_222', 'PIG_251', 'PIG_184', 'PIG_197']."
    }

response_404["ptype"] = \
    {
        "description": "Particle type does not exist",
        "detail": "{ptype} does not exist, should be in ['gas', 'dm', 'star', 'bh']."
    }

response_404["group_id"] = \
    {
        "description": "group_id out of range",
        "detail": "group_id out of range, should be in [1,max_group_size]."
    }

response_404["halo_id"] = \
    {
        "description": "halo_id out of range",
        "detail": "halo_id out of range, should be in [1,max_halo_size]."
    }

response_404["haloid_list"] = \
    {
        "description": "haloid_list is empty",
        "detail": "ID list is empty. Please input a valid one."
    }

response_404["type_id"] = \
    {
        "description": "type_id out of range",
        "detail": "type_id out of range, should be in [0,6)."
    }

response_404["ptype"] = \
    {
        "description": "ptype does not exist",
        "detail": "ptype does not exist, should be in ['gas', 'dm', 'star', 'bh']."
    }

response_404["feature"] = \
    {
        "description": "feature does not exist",
        "detail": "feature does not exist."
    }

response_404["criterion"] = \
    {
        "description": "Search criterion does not exist",
        "detail": "Search criterion does not exist, should be in ['bh_mass', 'gas_mass', 'dm_mass', 'star_mass', 'bh_mdot']."
    }

def construct_response_404(error_list):
    response = {
        "description": "",
        "content": {
            "application/json": {
                "example": {
                    "detail": ""},
                "schema": {
                    "$ref": "#/components/schemas/HTTPValidationError"}
            }
        }
    }
    for error in error_list:
        if response["description"] == "":
            response["description"] += response_404[error]["description"]
        else:
            response["description"] += " | " + response_404[error]["description"]
        if response["content"]["application/json"]["example"]["detail"] == "":
            response["content"]["application/json"]["example"]["detail"] += response_404[error]["detail"]
        else:
            response["content"]["application/json"]["example"]["detail"] += " Or " + response_404[error]["detail"]
    return response

response_404["read_snapshot_info"] = construct_response_404(["pig_id"])
response_404["read_snapshot_type_info"] = construct_response_404(["pig_id", "ptype"])
response_404["read_lbt_file"] = construct_response_404(["pig_id", "group_id"])
response_404["read_lbt_by_haloid_list"] = construct_response_404(["pig_id", "haloid_list", "halo_id"])
response_404["read_lbht"] = construct_response_404(["pig_id", "halo_id", "type_id"])
response_404["read_haloid_by_criterion"] = construct_response_404(["pig_id", "ptype", "feature"])
response_404["read_particle_data_by_criterion"] = construct_response_404(["pig_id", "ptype", "feature", "criterion", ])
response_404["read_fofgroup_data"] = construct_response_404(["pig_id", "feature", "group_id"])
response_404["read_fofgroup_data_all"] = construct_response_404(["pig_id", "feature"])
response_404["read_particle_data_by_groupid"] = construct_response_404(["pig_id", "ptype", "feature", "group_id"])
response_404["read_particle_data_by_post_groupid_list"] = construct_response_404(["pig_id", "ptype", "feature", "haloid_list"])

# 200 response description
response_200 = {}
def construct_response_200(description, example, model):
    response = {
        "description": description,
        "content": {
                "application/json": {
                    "example": example,
                    "schema": {
                        "$ref": "#/components/schemas/" + model
                    }
                }
            }
    }
    return response

response_200["read_pig"] = \
    {
        "description": "Successful Response - Snapshot info requested by pig ID",
    }

response_200["read_snapshot_info"] = \
    construct_response_200(
        "Successful Response - Particle info requested by pig ID",
        {
            "id": 251,
            "subdirs": [
                    "fofgroup",
                    "gas",
                    "dm",
                    "star",
                    "bh"
                ],
            "num_gas": 19358022252,
            "num_dm": 21165203462,
            "num_star": 587619843,
            "num_bh": 235967
        },
        "Snapshot")

response_200["read_snapshot_fof_info"] = \
    construct_response_200(
        "Successful Response - FoFGroup info requested by pig ID",
        {
            "id": 251,
            "fof_subdirs": [
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
        },
        "SnapshotFOFGroup")

response_200["read_snapshot_type_info"] = \
    construct_response_200(
        "Successful Response - Particle feature requested by pig ID and type",
        {
            "id": 251,
            "type": "dm",
            "subdirs": [
                "GroupID",
                "Velocity",
                "ID",
                "Potential",
                "Generation",
                "Position"
            ]
        },
        "SnapshotParticle")

response_200["read_lbt_file"] = \
    construct_response_200(
        "Successful Response - Lengthbytype data requested by pig ID and halo number",
        {
            "id": 251,
            "num": 1,
            "length_by_type": [
                [
                446499,
                507723,
                0,
                0,
                561897,
                7
                ]
            ]
        },
        "LengthbytypeN")

response_200["read_lbt_by_haloid_list"] = \
    construct_response_200(
        "Successful Response - Lengthbytype data requested by pig ID and list of halo IDs",
        {
            "id": 251,
            "haloid_lbt": {
                "1": [
                700225,
                0,
                0,
                0,
                1,
                0
                ],
                "2": [
                239021,
                247773,
                0,
                0,
                173607,
                8
                ]
            }
            },
        "LengthbytypeHaloList")

response_200["read_lbht"] = \
    construct_response_200(
        "Successful Response - Lengthbytype data requested by pig ID, halo ID, and type ID",
        {
            "id": 251,
            "halo_id": 10,
            "type_id": 1,
            "length": 121770
        },
        "LengthbytypeHaloIDTypeID")

response_200["read_fofgroup_data"] = \
    construct_response_200(
        "Successful Response - FOFGroup feature data requested by pig ID, feature, and group ID",
        {
        "id": 251,
        "halo_id": 10,
        "feature": "MassByType",
        "fofgroup_massbytype": "[28.026689529418945, 166.1539764404297, 0.0, 0.0, 5.827902793884277, 0.022659240290522575]"
        },
        "FOFGroup")


response_200["read_particle_data_by_groupid"] = \
    construct_response_200(
        "Successful Response - Particle feature data requested by pig ID, feature, and group ID",
        {
        "id": 271,
        "star_generation": "[1, 3, 1, 1, 1, 1, 1]"
        },
        "Particle")


response_200["read_particle_data_by_post_groupid_list"] = \
    construct_response_200(
        "Successful Response - Particle feature data requested by pig ID, feature, and group ID",
        {
        "id": 251,
        "ptype": "bh",
        "feature": "Generation",
        "bh_generation": {
            "1": "[1, 1, 1, 1, 1, 2, 1]",
            "2": "[]",
            "3": "[1, 1, 1, 1, 2, 1, 2, 1]"
        }
        },
        "Particle")

response_200["read_haloid_by_criterion"] = \
    construct_response_200(
        "Successful Response - Halo IDs of particles matching some searching criterion requested by pig ID, fofgroup feature, particle type, and min/max range",
        {
        "id": 251,
        "feature": "MassByType",
        "ptype": "bh",
        "min_range": 5e-3,
        "max_range": 1e-2,
        "IDlist": '[[6, 8, 12, 17, 23, 31, 33, 34, 38, 41, 43, 45, 46, 54, 57, 66, 67, 69, 70, 71, 74, 76, 90, 92, 94, 100, 104, 106, 117, 121, 122, 125, 130, 131, 132, 134, 137, 141, 145, 146, 149, 159, 160, 162, 163, 165, 169, 171, 174, 177, 180, 181, 185, 192, 193, 194, 196, 198, 200, 209, 218, 224, 229, 232, 238, 242, 246, 252, 254, 256, 258, 266, 269, 270, 273, 281, 292, 304, 311, 315, 318, 320, 324, 333, 336, 340, 348, 349, 363, 366, 372, 373, 393, 394, 396, 402, 406, 432, 438, 445, 455, 463, 464, 471, 474, 487, 510, 513, 519, 525, 534, 547, 548, 550, 553, 557, 564, 581, 584, 589, 592, 595, 604, 634, 640, 643, 645, 666, 678, 692, 696, 700, 709, 711, 718, 720, 744, 765, 792, 794, 807, 827, 831, 841, 850, 866, 868, 873, 889, 890, 911, 919, 920, 921, 937, 938, 953, 966, 997, 1008, 1025, 1032, 1034, 1047, 1068, 1104, 1124, 1152, 1170, 1175, 1188, 1191, 1199, 1201, 1228, 1230, 1249, 1252, 1260, 1287, 1296, 1304, 1312, 1316, 1317, 1325, 1333, 1346, 1379, 1380, 1439, 1448, 1453, 1465, 1473, 1491, 1492, 1502, 1524, 1528, 1534, 1550, 1562, 1592, 1603, 1619, 1625, 1632, 1636, 1701, 1730, 1740, 1745, 1773, 1785, 1857, 1890, 1936, 1938, 1946, 1993, 2046, 2071, 2136, 2199, 2206, 2241, 2331, 2350, 2483, 2607, 2671, 2694, 2701, 2749, 2794, 2976, 3011, 3170, 3214, 3259, 3269, 3318, 3353, 3388, 3469, 3686, 3740, 3750, 3906, 4185, 4304, 4338, 4678, 4681, 5230, 5408, 5947, 5986, 6054, 6293, 6884, 7624, 8788, 686170]]'
        },
        "Particle")