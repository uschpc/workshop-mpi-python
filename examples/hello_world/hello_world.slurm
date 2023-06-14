#!/bin/bash
#SBATCH --ntasks=4
#SBATCH --partition=gpu
#SBATCH --reservation=bootcamp
#SBATCH --account=hpcsuppt_613
#SBATCH --mem-per-cpu=2GB

module load usc
module load python

mpirun python3 hello_world_mpi.py

