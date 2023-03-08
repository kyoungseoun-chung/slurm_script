# `slurm_script` Python Slurm command generator

This package is designed to generate slurm script to submit `mpi` jobs to a cluster.

## Installation

You can install the package using `pip`.

```bash
python -m pip install slurm_script
```

## Usage

```bash
$ sjob --h
slurm_script version: 0.1.7
usage: slurm_script/sjob [-h] [-n NPROC] [-j JOB_NAME] [-t TIME] [-m MEM_PER_CPU] [-c COMMAND [COMMAND ...]] [-mail MAIL_TYPE]
                         [-nt NTASKS] [-cnt CPUS_PER_TASK] [-a ADDITIONAL_CMD [ADDITIONAL_CMD ...]]

python interface to generate and run slurm command.

options:
  -h, --help            show this help message and exit
  -n NPROC, --nproc NPROC
                        Number of processors to run the job.
  -j JOB_NAME, --job_name JOB_NAME
                        Name of the job.
  -t TIME, --time TIME  Maximum runtime [hours:minutes:second].
  -m MEM_PER_CPU, --mem_per_cpu MEM_PER_CPU
                        Memory per core [MB].
  -c COMMAND [COMMAND ...], --command COMMAND [COMMAND ...]
                        Program command.
  -mail MAIL_TYPE, --mail_type MAIL_TYPE
                        Email notification at either BEGIN, END, or FAIL.
  -nt NTASKS, --ntasks NTASKS
                        Number of tasks.
  -cnt CPUS_PER_TASK, --cpus_per_task CPUS_PER_TASK
                        Number of cpus per task.
  -a ADDITIONAL_CMD [ADDITIONAL_CMD ...], --additional_cmd ADDITIONAL_CMD [ADDITIONAL_CMD ...]
                        Additional commands.
```

## Note

It seems like due to a security reason, it is not possible to use `sjob` command directly from the cluster.
Therefore, you can use the following command instead

```bash
python -m slurm_script --h
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
