from mpi4py import MPI

max=10

ntotal = MPI.COMM_WORLD.Get_size()
myrank = MPI.COMM_WORLD.Get_rank()

np        = max//ntotal # Gives the quotient
remainder = max % ntotal


start=None
end=None

if ( myrank is ntotal-1):
    start=myrank*np
    end=(myrank+1)*np+remainder
else:
    start=myrank*np
    end=(myrank+1)*np
    
print( 'myrank=',myrank,' start =',start, ' end=',end)

for i in range(start,end+1):
    print('Rank ',myrank,': ',i)
