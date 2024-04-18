#!/bin/bash
#SBATCH --job-name=da_Li
#SBATCH --nodes=1
#SBATCH --ntasks=72
#SBATCH --cpus-per-task=1
#SBATCH --mem=0
#SBATCH --time=5:30:00
#SBATCH --exclusive
#SBATCH --qos=serial

export OMP_NUM_THREADS=1
#sourceand load all the important modules
#module load ...
#source ...

for i in 8 1024 8192 65536 ; 
do 
	../run_profiling.sh $i 2> timing-$i.log 
done 

wait
