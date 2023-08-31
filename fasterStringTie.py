import os
import subprocess
import multiprocessing
import datetime
import argparse

current_datetime = datetime.datetime.now()
current_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

# Check if StringTie is installed
try:
    subprocess.run(["stringtie", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
except subprocess.CalledProcessError:
    print("Error: StringTie is not installed. Please install StringTie and make sure it's in your PATH.")
    exit(1)

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Faster Transcriptome Assembly of BAM files using StringTie.")
parser.add_argument("accessions_file", help="Path to the accessions.txt file")
parser.add_argument("-i", "--input_dir", help="Directory where the BAM files are located")
parser.add_argument("-o", "--output_dir", help="Output directory")
parser.add_argument("-r", "--reference", help="Path to the reference GTF file")
args = parser.parse_args()

accessions_file = args.accessions_file
input_dir = args.input_dir
output_dir = args.output_dir
reference = args.reference

def process_accession(accession):
    command = (
        f"stringtie {cores} {reference} "
        f"{os.path.join(input_dir, accession)}.bam -o {os.path.join(output_dir, accession)}.gtf"
    )
    print(f"{accession} ....running....")
    os.system(command)

if __name__ == "__main__":
    with open(accessions_file, "r") as file:
        accessions = file.read().split()


    cores = " -p 8 "

    num_cores = multiprocessing.cpu_count()
    max_cores_to_use = int(num_cores * 0.75)  # Limit to 75% of available cores

    with multiprocessing.Pool(processes=max_cores_to_use) as pool:
        pool.map(process_accession, accessions)

    
    print("Started at: " + current_datetime)
    current_datetime = datetime.datetime.now()
    endtime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print("Finised at: " + endtime)
    print("All done")
