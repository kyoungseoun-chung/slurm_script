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
