from mpi4py import MPI
import bigmpi4py as BM
import numpy as np

comm = MPI.COMM_WORLD
size, rank = comm.Get_size(), comm.Get_rank()
arr, df, lst = None, None, None
if rank == 0:
    arr = np.random.rand(2 ** 26, 10)
    # df = pd.DataFrame(arr)
    lst = [arr, arr, arr]

scatter_arr = BM.scatter(arr, comm)
# scatter_df = BM.scatter(df, comm)
scatter_lst = BM.scatter(lst, comm)
bcast_lst = BM.bcast(lst, comm)

gather_arr = BM.gather(arr, comm)
print(gather_arr[0][:])