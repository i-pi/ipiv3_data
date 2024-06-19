#!/bin/bash
#SBATCH --job-name=da_Li
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=2
#SBATCH --time=00:30:00
#SBATCH --exclusive
#SBATCH --partition=gpu
#SBATCH --qos=gpu
#SBATCH --gres=gpu:2

module load gcc/11.3.0 cuda/11.8.0 openmpi/4.1.3-cuda cudnn
source /home/tisi/ipi-paper-test/venv-gpu-cuda-direct/bin/activate
rm /tmp/ipi_driver
export OMP_NUM_THREADS=1 #
echo 'OMP_NUM_THREADS='
export TF_INTRA_OP_PARALLELISM_THREADS=1
export TF_INTER_OP_PARALLELISM_THREADS=1

srun -n 4 --exclusive lmp -in ../input-lammps.lammps >dp.out &

wait
