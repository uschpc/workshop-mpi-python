from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

print(f'Rank {rank} starting up...')

data = None

if rank == 0:
    print(f'Rank {rank}: Sending data to rank 1 ')
    comm.send(412,dest=1)

if rank == 1:
    print(f'Rank {rank}: Waiting for data from rank 1 ')
    data=comm.recv(source=0)
    print(f'Rank {rank}: Got data {data} from rank 1')

print(f'Rank {rank}: shutting down with data={data}.')
