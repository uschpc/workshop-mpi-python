#!/bin/bash
#SBATCH --ntasks=4
#SBATCH --partition=gpu
#SBATCH --reservation=bootcamp
#SBATCH --account=hpcsuppt_613
#SBATCH --mem-per-cpu=2GB

module load usc

python_bin=/apps/spack/2406/apps/linux-rocky8-x86_64_v3/gcc-13.3.0/python-3.11.9-x74mtjf/bin/python
mpirun $python_bin hello_world_mpi.py

