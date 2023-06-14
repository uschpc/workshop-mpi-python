from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
ntotal = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()

np.random.seed(10)
A = np.random.rand(8,8)

ilist           = np.random.randint(0,7,10)
jlist           = np.random.randint(0,7,10)

A[ilist,jlist] = 0

npi=int(2)
npj=int(ntotal/npi)

rank_i=rank//npi
rank_j=rank%npi

ni,nj=A.shape

chunk_size_i=int(ni/npi)
chunk_size_j=int(nj/npj)

A_tmp=A[rank_i*chunk_size_i:(rank_i+1)*chunk_size_i,
        rank_j*chunk_size_j:(rank_j+1)*chunk_size_j]
nz_local =len(np.where(A_tmp==0)[0])

print(f'Rank {rank}: I found {nz_local} non-zero elements in my portion!')

if rank !=0:
    comm.send(nz_local,dest=0,tag=7)

if rank==0:
  nz_list=np.zeros((ntotal,),int)

  nz_list[0]=nz_local

  for i in range(1,ntotal):
    nz_list[i]=comm.recv(source=i,tag=7)

if rank==0:
  nz_global=sum(nz_list)

if rank==0:
  print(f'Rank {rank}: We all found {nz_global} non-zero elements in total')

