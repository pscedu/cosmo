# command: mpirun -np 4 python parallel.py
import sys
import os
import mpi4py.MPI as MPI
import numpy as np
import bigfile
import pickle
import time
import bigmpi4py as BM

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
    path = "/bluetides3/PIG_251/FOFGroups/OffsetByType"
    if comm_rank == 0:
        pig = bigfile.File("/bluetides3/PIG_251/")
    pig = BM.bcast(pig if comm_rank == 0 else None, comm)
    t1 = time.time()
    num_data = pig.open('FOFGroups/OffsetByType/').size
    local_data_offset = np.linspace(0, num_data, comm_size +1).astype('int')
    len_local = local_data_offset[comm_rank + 1] - local_data_offset[comm_rank]
    sys.stderr.write("%d/%d processor gets %d/%d data \n" %(comm_rank, comm_size, len_local, num_data))
    
    local_data = pig.open('FOFGroups/OffsetByType/')[local_data_offset[comm_rank]:local_data_offset[comm_rank+1]]
    t2 = time.time()

    pig.close()
    print('Time to fetch data is : %.2f s'%(t2-t1))
