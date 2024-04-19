#!/bin/bash
#SBATCH --job-name=da_Li
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=72
#SBATCH --cpus-per-task=1
#SBATCH --mem=0
#SBATCH --time=00:30:00
#SBATCH --exclusive
#SBATCH --qos=serial

module load gcc/11.3.0  openmpi/4.1.3
source /home/tisi/ipi-paper-test/venv-cpu/bin/activate  
rm /tmp/ipi_driver
export OMP_NUM_THREADS=1
echo 'OMP_NUM_THREADS='$OMP_NUM_THREADS
export TF_INTER_OP_PARALLELISM_THREADS=1
export TF_INTRA_OP_PARALLELISM_THREADS=1

IPI_ADDRESS=$(hostname)  # fetches the hostname i-PI will run on
IPI_INPUT=../input_internet_xml.xml
echo "Running on $IPI_ADDRESS"
IPI_PORT=$(grep '<port>' $IPI_INPUT | sed 's/[^>]*>[[:space:]]*//; s/[[:space:]]*<.*//')
DRIVER_INPUT=../input-ipi-inet-lammps.lammps
IPI_UUID=$(uuidgen)

sed "s/address>[^<].*</address> $IPI_ADDRESS </" $IPI_INPUT > ${IPI_INPUT}-${IPI_UUID}
## You may have to adjust the input if the address name is used also
## for something else
sed "s/HOSTNAME/$IPI_ADDRESS/;" $DRIVER_INPUT > ${DRIVER_INPUT}-${IPI_UUID}

IPI=/home/tisi/ipi-paper-test/i-pi-main-3.0/bin/i-pi
#IPI=/home/tisi/ipi-paper-test/venv-cpu/bin/i-pi
#srun -n 1 --exclusive python -u $IPI ../input_xml.xml &> log.ipi &
python -u $IPI ${IPI_INPUT}-${IPI_UUID} &> log.ipi &
sleep 15

for i in $(seq 16);
do
echo 'run deepmd number '$i
#srun -n ${SLURM_CPUS_PER_TASK} dp_ipi ../water.json >dp$i.out &
srun -N 1 -n 8 --exclusive lmp -in ${DRIVER_INPUT}-${IPI_UUID} >dp$i.out &
sleep 2
done


wait
