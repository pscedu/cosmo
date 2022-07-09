import json
import os
from json.encoder import JSONEncoder

import bigfile
import numpy
from fastapi import HTTPException

from . import constants


class NumpyArrayEncoder(JSONEncoder):
    """
    A class used to serialize numpy ndarray into json.
    """
    def default(self, obj):
        if isinstance(obj, numpy.integer):
            return int(obj)
        elif isinstance(obj, numpy.floating):
            return float(obj)
        elif isinstance(obj, numpy.ndarray):
            return obj.tolist()
        else:
            return super().default(obj)


def check_pig_id(pig_id: int):
    """
    Check if pig ID is in the existing pig directory.

    Parameters
    ----------
    pig_id : int
        ID of a PIG folder.

    Raises
    ------
    HTTPException
        If pig_id folder does not exist, return 404.
    """
    subdirectories = get_pig_folders()
    pig_folder = "PIG_" + str(pig_id)
    if pig_folder not in subdirectories:
        raise HTTPException(status_code=404, detail="PIG_{} folder does not exist, and should be in {}".format(pig_id, subdirectories))


def check_type_id_range(type_id: int):
    """
    Check if type_id is in [0, 6), the id range of particle type.

    Parameters
    ----------
    type_id : int
        ID of particle type.

    Raises
    ------
    HTTPException
        If type_id out of range, return 404.
    """
    if type_id < 0 or type_id >= 6:
        raise HTTPException(status_code=404, detail="type_id out of range, should be in [0,6)")


def check_group_id_range(pig, group_id: int):
    """
    Check if group_id is in range.

    Parameters
    ----------
    group_id : int
        ID of halo group.

    Raises
    ------
    HTTPException
        If group_id out of range, return 404.
    """
    total_group = pig.open('FOFGroups/LengthByType').size
    if group_id <= 0 or group_id > total_group:
        raise HTTPException(status_code=404, detail="group_id out of range, should be in [1,{}]".format(total_group))


def check_halo_id_range(pig, halo_id: int):
    """
    Check if halo_id is in range.

    Parameters
    ----------
    halo_id : int
        ID of a halo.

    Raises
    ------
    HTTPException
        If halo_id out of range, return 404.
    """
    total_halo = pig.open('FOFGroups/LengthByType').size
    if halo_id < 0 or halo_id >= total_halo:
        raise HTTPException(status_code=404, detail="halo_id out of range, should be in [0,{})".format(total_halo))


def check_type_name(ptype: str):
    """
    Check if type name in ['gas', 'dm', 'star', 'bh'].

    Parameters
    ----------
    ptype : star
        Particle type name.

    Raises
    ------
    HTTPException
        If particle type does not exist, return 404.
    """
    type_list = ['gas', 'dm', 'star', 'bh']
    if ptype not in type_list:
        raise HTTPException(status_code=404,
                            detail="ptype {} does not exist, should be in {}".format(ptype, type_list))


def check_query_list(id_list):
    """
    Check if query ID list is not empty.

    Parameters
    ----------
    id_list : List Object
        List of group IDs.

    Raises
    ------
    HTTPException
        If ID list is empty, return 404.
    """
    if id_list is None:
        raise HTTPException(status_code=404, detail="ID list is empty. Please input a valid one.")


def get_pig_folders():
    """
    Return the list of PIG folders.
    """
    subdirectories = []
    directory_contents = os.listdir(constants.PIG_BASE_DIR)
    for item in directory_contents:
        if item.startswith("PIG_"):
            subdirectories.append(item)
    return subdirectories


def get_pig_numhalo(sub_dir: str):
    """
    Return total number of halos in a PIG folder directory.

    Parameters
    ----------
    sub_dir : str
        Directory of a PIG folder.
    """
    pig_dir = constants.PIG_BASE_DIR + sub_dir + '/'
    pig = bigfile.File(pig_dir)
    Nhalo = pig['Header'].attrs['NumFOFGroupsTotal'][0]
    return Nhalo


def get_pig_redshift(sub_dir: str):
    """
    Return the redshift information(aka time info) in a PIG folder directory.

    Parameters
    ----------
    sub_dir : str
        Directory of a PIG folder.
    """
    pig_dir = constants.PIG_BASE_DIR + sub_dir + '/'
    pig = bigfile.File(pig_dir)
    scalefactor = pig['Header'].attrs['Time'][0]
    redshift = 1. / scalefactor - 1.
    return redshift


def get_pig_data(pig_id: int):
    """
    Return a particular PIG folder data in bigfile format.

    Parameters
    ----------
    pig_id : int
        ID of a PIG folder.
    """
    # data directory
    pig_dir = constants.PIG_BASE_DIR + "PIG_" + str(pig_id) + "/"
    pig = bigfile.File(pig_dir)
    return pig


def get_lbt_by_haloid(pig_id: int, halo_id: int):
    """
    Return lengthbytype data in json format.

    Parameters
    ----------
    pig_id : int
        ID of a PIG folder.
    halo_id : int
        ID of a halo.
    """
    check_pig_id(pig_id=pig_id)
    pig = get_pig_data(pig_id)
    check_halo_id_range(pig=pig, halo_id=halo_id)
    nhalo = pig.open('FOFGroups/LengthByType')[halo_id]
    numpy_array_type_data = numpy.array(nhalo)
    # encoded_numpy_type_data = json.dumps(numpy_array_type_data, cls=NumpyArrayEncoder)
    return numpy_array_type_data.tolist()


def get_part_subfield(pig_id: int, ptype: str):
    """
    Return list of features of a particle type in a particular PIG folder.

    Parameters
    ----------
    pig_id : int
        ID of a PIG folder.
    ptype : str
        Name of particle type.
    """
    check_pig_id(pig_id=pig_id)
    check_type_name(ptype)
    type_ind = {'gas': 0, 'dm': 1, 'star': 4, 'bh': 5}
    subdirectories = []
    directory_contents = os.listdir(constants.PIG_BASE_DIR + 'PIG_' + str(pig_id) + '/' + str(type_ind[ptype]))
    for item in directory_contents:
        subdirectories.append(item)
    return subdirectories


def get_fof_subfield(pig_id: int):
    """
    Return list of features of a fofgroup in a particular PIG folder.

    Parameters
    ----------
    pig_id : int
        ID of a PIG folder.
    """
    check_pig_id(pig_id=pig_id)
    subdirectories = []
    directory_contents = os.listdir(constants.PIG_BASE_DIR + 'PIG_' + str(pig_id) + '/FOFGroups')
    for item in directory_contents:
        subdirectories.append(item)
    return subdirectories


def check_feature(pig_id: int, ptype: str, feature: str):
    """
    Check if particle type and feature exist.

    Parameters
    ----------
    pig_id : int
        ID of a PIG folder.
    ptype : str
        Name of particle type.
    feature : str
        Feature of a particle.

    Raises
    ------
    HTTPException
        If particle type or feature does not exist, return 404.
    """
    type_list = ['gas', 'dm', 'star', 'bh']
    if ptype in type_list:
        subdirectories = get_part_subfield(pig_id=pig_id, ptype=ptype)
    elif ptype == 'fofgroup':
        subdirectories = get_fof_subfield(pig_id=pig_id)
    else:
        raise HTTPException(status_code=404,
                            detail="Particle type {} does not exist, should be in {}".format(ptype, type_list))
    if feature not in subdirectories:
        raise HTTPException(status_code=404,
                            detail="Feature {} does not exist, should be in {}".format(feature, subdirectories))


def check_criterion(criterion: str):
    """
    Check if criterion exists in ['bh_mass', 'gas_mass', 'dm_mass', 'star_mass', 'bh_mdot'].

    Parameters
    ----------
    criterion : str
        Searching criterion.

    Raises
    ------
    HTTPException
        If criterion does not exist, return 404.

    Note
    ----
    For now we only have limited criterions
    """
    criterion_list = ['bh_mass', 'gas_mass', 'dm_mass', 'star_mass', 'bh_mdot']
    if criterion not in criterion_list:
        raise HTTPException(status_code=404,
                            detail="Search criterion {} does not exist, should be in {}".format(criterion,
                                                                                                criterion_list))


def get_particle_data(pig_id: int, group_id: int, ptype: str, feature: str):
    """
    Return particle feature data in a particular PIG folder in json format.

    Parameters
    ----------
    pig_id : int
        ID of a PIG folder.
    group_id : int
        ID of a halo group.
    ptype : str
        Name of particle type.
    feature : str
        Feature of a particle.
    """
    check_pig_id(pig_id=pig_id)
    pig = get_pig_data(pig_id)

    check_group_id_range(pig=pig, group_id=group_id)
    obt = pig.open('FOFGroups/OffsetByType')[group_id-1:group_id+1]
    
    check_feature(pig_id=pig_id, ptype=ptype, feature=feature)
    type_ind = {'gas': 0, 'dm': 1, 'star': 4, 'bh': 5}
    ind = type_ind[ptype]

    path = str(ind) + '/' + feature
    data = pig.open(path)[obt[0][ind]:obt[1][ind]]
    numpy_array_data = numpy.array(data)
    encoded_numpy_data = json.dumps(numpy_array_data, cls=NumpyArrayEncoder)
    return encoded_numpy_data


def get_particle_data_criterion(pig_id: int, ptype: str,
                                feature: str, criterion: str,
                                min_range: float, max_range: float):
    """
    Return a dictionary of {groupid:data} for data of 'feature' type within
    the searching criterion.
    Current available criterions:
    gas_mass, dm_mass, star_mass, bh_mass, bh_mdot

    Parameters
    ----------
    pig_id : int
        ID of a PIG folder.
    ptype : str
        Name of particle type for queried data.
    feature : str
        Feature of the particle for the queried data.
    criterion: str
        Criterion for the search (gas_mass, dm_mass, star_mass, bh_mass, bh_mdot)
    min_range: float
        low limit for the search
    max_range: float
        upper limit for the search
    """
    check_pig_id(pig_id=pig_id)
    pig = get_pig_data(pig_id)
    check_criterion(criterion)
    check_feature(pig_id=pig_id, ptype=ptype, feature=feature)
    obt = pig.open('FOFGroups/OffsetByType')[:]

    type_ind = {'gas': 0, 'dm': 1, 'star': 4, 'bh': 5}
    ind = type_ind[ptype]
    path = str(ind) + '/' + feature

    if criterion == 'gas_mass':
        mbt = pig.open('FOFGroups/MassByType')[:]
        id_list = ((mbt[:, 0] >= min_range) & (mbt[:, 0] <= max_range)).nonzero()[0]
    elif criterion == 'dm_mass':
        mbt = pig.open('FOFGroups/MassByType')[:]
        id_list = ((mbt[:, 1] >= min_range) & (mbt[:, 1] <= max_range)).nonzero()[0]
    elif criterion == 'star_mass':
        mbt = pig.open('FOFGroups/MassByType')[:]
        id_list = ((mbt[:, 4] >= min_range) & (mbt[:, 4] <= max_range)).nonzero()[0]
    elif criterion == 'bh_mass':  # need to use individual BH mass instead of MBT
        bhm = pig.open('5/BlackholeMass')[:]
        index = (bhm >= min_range) & (bhm <= max_range)
        id_list = list(set(pig.open('5/GroupID')[:][index] - 1))
    elif criterion == 'bh_mdot':
        bhacc = pig.open('5/BlackholeAccretionRate')[:]
        index = (bhacc >= min_range) & (bhacc <= max_range)
        id_list = list(set(pig.open('5/GroupID')[:][index] - 1))
    data = {str(i): json.dumps(pig.open(path)[obt[i, ind]:obt[i + 1, ind]], cls=NumpyArrayEncoder) for i in id_list}
    return data


def get_fofgroup_data_all(pig_id: int, feature: str):
    """
    Return all fofgroup feature data in a particular PIG folder in json format.

    Parameters
    ----------
    pig_id : int
        ID of a PIG folder.
    feature : str
        Feature of a particle.
    """
    check_pig_id(pig_id=pig_id)
    pig = get_pig_data(pig_id)
    check_feature(pig_id=pig_id, ptype='fofgroup', feature=feature)
    data = pig.open('FOFGroups/' + feature)[:]
    numpy_array_data = numpy.array(data)
    encoded_numpy_data = json.dumps(numpy_array_data, cls=NumpyArrayEncoder)
    return encoded_numpy_data


def get_fofgroup_data(pig_id: int, group_id: int, feature: str):
    """
    Return fofgroup feature data in a particular PIG folder in json format.

    Parameters
    ----------
    pig_id : int
        ID of a PIG folder.
    group_id : int
        ID of a halo group.
    feature : str
        Feature of a particle.
    """
    check_pig_id(pig_id=pig_id)
    pig = get_pig_data(pig_id)
    check_group_id_range(pig=pig, group_id=group_id)
    check_feature(pig_id=pig_id, ptype='fofgroup', feature=feature)
    data = pig.open('FOFGroups/' + feature)[group_id - 1]
    numpy_array_data = numpy.array(data)
    encoded_numpy_data = json.dumps(numpy_array_data, cls=NumpyArrayEncoder)
    return encoded_numpy_data
