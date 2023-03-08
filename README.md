# `slurm_script` Python Slurm command generator

This package is designed to generate slurm script to submit `mpi` jobs to a cluster.

## Usage

```bash
slurm_script version: 0.1.2
usage: slurm_script [-h] [-n NPROC] [-j JOB_NAME] [-t TIME] [-m MEM_PER_CPU]
                    [-c COMMAND [COMMAND ...]]

python interface to generate and run slurm command.

options:
  -h, --help            show this help message and exit
  -n NPROC, --nproc NPROC
                        Number of processors to run the job.
  -j JOB_NAME, --job-name JOB_NAME
                        Name of the job.
  -t TIME, --time TIME  Maximum runtime [hours:minutes:second].
  -m MEM_PER_CPU, --mem-per-cpu MEM_PER_CPU
                        Memory per core [MB].
  -c COMMAND [COMMAND ...], --command COMMAND [COMMAND ...]
                        Program command.
```

## Example

```bash
$ sjob -n 10 -j test_run -t 10:00:00 -m 1024 -mail BEGIN,END,FAIL -nt 1 -cnt 10 -a module add python -c python test.py
slurm_script version: 0.1.6

Preview of the generated script:
--------------------------------
#!/bin/bash

#SBATCH -n 10
#SBATCH --job-name=test_run
#SBATCH --time=10:00:00
#SBATCH --mem-per-cpu=1024
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10

module add python

mpirun python test.py
--------------------------------
Do you want to run the script? [y/n] 
```
