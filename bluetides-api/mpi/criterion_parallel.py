# command: mpirun -np 4 python parallel.py
import sys
import os
import mpi4py.MPI as MPI
import numpy as np
import bigfile
import time
import pickle

#
#  Global variables for MPI
#
 
# instance for invoking MPI relatedfunctions
comm = MPI.COMM_WORLD
# the node rank in the whole community
comm_rank = comm.Get_rank()
# the size of the whole community, i.e.,the total number of working nodes in the MPI cluster
comm_size = comm.Get_size()
 
if __name__ == '__main__':
    if comm_rank == 0:
        pig = bigfile.File("/bluetides3/PIG_251/")
    # broadcast bigfile pig data
    pig = comm.bcast(pig if comm_rank == 0 else None, root = 0)
    num_data = pig.open('FOFGroups/MassByType/').size
    local_data_offset = np.linspace(0, num_data, comm_size +1).astype('int')
    len_local = local_data_offset[comm_rank + 1] - local_data_offset[comm_rank]
    sys.stderr.write("%d/%d processor gets %d/%d data \n" %(comm_rank, comm_size, len_local, num_data))
    t1 = time.time()
    file1 = open("haloid_list.pkl", "ab") # File operation is just used to check if the result is correct. Can be deleted afterwards.
    # get halo id list matching certain criterion, in this example, find all halo ids whose massbytype value is between 1e-2 and 5e-3
    max_range = 1e-2
    min_range = 5e-3
    data = pig.open('FOFGroups/MassByType/')[local_data_offset[comm_rank]:local_data_offset[comm_rank+1]]
    data = data[:, 1]
    res = np.where((data <= max_range) & (data >= min_range))
    t2 = time.time()
    # load result data to pkl file and can use load_data.py to check if the result matches expectation
    if res != []:
        pickle.dump(np.array(res), file1)
    pig.close()
    file1.close()

    # gather data from all processors
    result = comm.allgather(res)
    result = np.hstack(result)
    file2 = open("haloid_list_gather.pkl", "ab") # File operation is just used to check if the result is correct. Can be deleted afterwards.
    if comm_rank == 0:   
        pickle.dump(np.array(result), file2)
    file2.close()
    print('Time to fetch data is : %.2f s'%(t2-t1))
