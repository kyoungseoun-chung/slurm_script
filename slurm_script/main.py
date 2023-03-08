#!/usr/bin/env python3
import argparse
import tempfile
import subprocess

from slurm_script import __version__

SLURM_ARGS = argparse.ArgumentParser(
    prog="slurm_script/sjob",
    description="python interface to generate and run slurm command.",
)
SLURM_ARGS.add_argument(
    "-n", "--nproc", help="Number of processors to run the job.", type=int
)

SLURM_ARGS.add_argument("-j", "--job_name", help="Name of the job.", type=str)

SLURM_ARGS.add_argument(
    "-t", "--time", help="Maximum runtime [hours:minutes:second].", type=str
)

SLURM_ARGS.add_argument("-m", "--mem_per_cpu", help="Memory per core [MB].", type=str)

SLURM_ARGS.add_argument("-c", "--command", help="Program command.", nargs="+", type=str)

SLURM_ARGS.add_argument(
    "-mail",
    "--mail_type",
    help="Email notification at either BEGIN, END, or FAIL.",
    type=str,
)
SLURM_ARGS.add_argument("-nt", "--ntasks", help="Number of tasks.", type=int)
SLURM_ARGS.add_argument(
    "-cnt", "--cpus_per_task", help="Number of cpus per task.", type=str
)
SLURM_ARGS.add_argument(
    "-a", "--additional_cmd", help="Additional commands.", nargs="+", type=str
)

args_to_slurm_flag = {
    "nproc": " -n ",
    "job_name": " --job-name=",
    "time": " --time=",
    "mem_per_cpu": " --mem-per-cpu=",
    "output": " --output=",
    "command": " ",
    "mail_type": " --mail-type=",
    "ntasks": " --ntasks=",
    "cpus_per_task": " --cpus-per-task=",
}

bash_header = "#!/bin/bash\n\n"
prefix = "#SBATCH"


def main() -> None:

    print(f"slurm_script version: {__version__}")
    argv = SLURM_ARGS.parse_args()

    template = bash_header
    for ar in vars(argv):
        val = getattr(argv, ar)
        if val is not None and ar != "command" and ar != "additional_cmd":
            template += prefix + args_to_slurm_flag[ar] + str(val) + "\n"

    template += "\n"
    # Place additional command in between sbatch parameter and mpirun command
    if argv.additional_cmd is not None:
        template += " ".join(argv.additional_cmd) + "\n"

    if argv.command is not None:
        run_command = " ".join(argv.command)
        template += "\nmpirun" + args_to_slurm_flag["command"] + run_command
    else:
        raise ValueError("No command provided.")

    # Report
    print("")
    print("Preview of the generated script:")
    print("--------------------------------")
    print(template)
    print("--------------------------------")

    run_flag = input("Do you want to run the script? [y/n] ")
    if run_flag.lower() == "y" or run_flag == "":
        with tempfile.NamedTemporaryFile(mode="r+", suffix=".sh") as temp_file:
            temp_file.write(template)
            temp_file.flush()
            subprocess.run(["sbatch", temp_file.name])
    else:
        print("Finished without running the script.")
