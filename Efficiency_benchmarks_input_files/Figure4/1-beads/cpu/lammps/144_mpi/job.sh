#!/bin/bash
#SBATCH --job-name=da_Li
#SBATCH --nodes=2
#SBATCH --ntasks=144
#SBATCH --cpus-per-task=1
#SBATCH --mem=0
#SBATCH --time=5:30:00
#SBATCH --exclusive
#SBATCH --qos=serial

module load gcc/11.3.0  openmpi/4.1.3
source /home/tisi/ipi-paper-test/venv-cpu/bin/activate  
rm /tmp/ipi_driver
export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK}
echo 'OMP_NUM_THREADS='$OMP_NUM_THREADS

srun -N 2 -n 144 --exclusive lmp -in ../input-lammps.lammps >dp.out &

wait
