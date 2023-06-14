#!/bin/bash
#SBATCH --ntasks=4
#SBATCH --partition=gpu
#SBATCH --reservation=bootcamp
#SBATCH --account=hpcsuppt_613
#SBATCH --mem-per-cpu=2GB

module load usc
module load python

mpirun -n 2 python3 send_test.py

