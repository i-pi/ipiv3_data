#!/bin/bash
#SBATCH --job-name=da_Li
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=3
#SBATCH --time=00:30:00
#SBATCH --exclusive
#SBATCH --partition=gpu
#SBATCH --mem=0
#SBATCH --qos=gpu
#SBATCH --gres=gpu:2

module load gcc/11.3.0 cuda/11.8.0 openmpi/4.1.3-cuda cudnn
source /home/tisi/ipi-paper-test/venv-gpu-cuda-direct/bin/activate
rm /tmp/ipi_driver
export OMP_NUM_THREADS=1 #${SLURM_CPUS_PER_TASK}
echo 'OMP_NUM_THREADS='$OMP_NUM_THREADS
export TF_INTRA_OP_PARALLELISM_THREADS=1
export TF_INTER_OP_PARALLELISM_THREADS=1

IPI=/home/tisi/ipi-paper-test/i-pi-main-3.0/bin/i-pi
#IPI=/home/tisi/ipi-paper-test/venv-cpu/bin/i-pi
#srun -n 1 --exclusive python -u $IPI ../input_xml.xml &> log.ipi &
python -u $IPI ../input_xml.xml &> log.ipi &
sleep 15

for i in 1 ;
do
echo 'run deepmd number '$i
#srun -n ${SLURM_CPUS_PER_TASK} dp_ipi ../water.json >dp$i.out &
srun -N 4 -n 8 --exclusive lmp -in ../input-ipi-lammps.lammps >dp.out &
sleep 2
done

wait
