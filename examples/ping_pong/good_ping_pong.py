from mpi4py import MPI
import sys,time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
world_size = MPI.COMM_WORLD.Get_size()

if world_size !=2:
    print("Only two can play")
    sys.exit(1)

print(f'Rank {rank} starting up...')

counter = 0
max_counter = 10 


if rank == 0:
    partner = 1
    print(f'Rank {rank}: sending message {counter} to rank {partner}')
    comm.send(counter,dest=partner)
if rank == 1:
    partner = 0

while counter < max_counter:
    time.sleep(1)
    counter=comm.recv(source=partner)
    print(f'Rank {rank}: Got message {counter} from rank {partner}')

    print(f'Rank {rank}: sending message {counter} to rank {partner}')
    comm.send(counter,dest=partner)
    counter = counter + 1
