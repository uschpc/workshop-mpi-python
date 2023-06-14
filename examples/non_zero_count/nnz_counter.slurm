#!/bin/bash
#SBATCH --ntasks=4
#SBATCH --partition=gpu
#SBATCH --reservation=bootcamp
#SBATCH --account=hpcsuppt_613
#SBATCH --mem-per-cpu=2GB
#SBATCH --time=00:10:00

module load usc
module load python

mpirun python3 nnz_counter.py
