#!/bin/bash
#SBATCH --job-name=da_Li
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=72
#SBATCH --cpus-per-task=1
#SBATCH --mem=0
#SBATCH --time=12:30:00
#SBATCH --exclusive
#SBATCH --qos=serial

module load gcc/11.3.0  openmpi/4.1.3
source /home/tisi/ipi-paper-test/venv-cpu/bin/activate  
rm /tmp/ipi_driver
export OMP_NUM_THREADS=1
echo 'OMP_NUM_THREADS='$OMP_NUM_THREADS
export TF_INTER_OP_PARALLELISM_THREADS=1
export TF_INTRA_OP_PARALLELISM_THREADS=1

IPI=/home/tisi/ipi-paper-test/i-pi-main-3.0-beta2/bin/i-pi
#IPI=/home/tisi/ipi-paper-test/venv-cpu/bin/i-pi
srun -n 1 --exclusive python -u $IPI ../input_xml.xml &> log.ipi &
sleep 15

for i in $(seq 32);
do
echo 'run deepmd number '$i
#srun -n ${SLURM_CPUS_PER_TASK} dp_ipi ../water.json >dp$i.out &
srun -n 1 --exclusive /home/tisi/ipi-paper-test/lammps-labcosmo_jed/src/lmp_mpi -in ../input-ipi-lammps.lammps >dp$i.out &
sleep 2 
done

wait
