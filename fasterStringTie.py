import os
import multiprocessing

def process_accession(accession):
    command = (
        f"{inst_dir}{cores}-G {reference} "
        f"{input_dir}{accession}_dedup.bam -o {output_dir}{accession}.gtf"
    )
    print(f"{command} ....running....")
    os.system(command)

if __name__ == "__main__":
    file = open("accessions.txt")
    accessions = file.read().split()

    inst_dir = "stringtie"
    reference = "/opt/Homo_sapiens.GRCh38.108.gtf"
    input_dir = "/media/waqar/hdd/easeRNAseq/E-MTAB-8412_colorectal_border/mapping/bam_sorted/"
    output_dir = "/home/waqar/Desktop/test-string/"

    cores = " -p 12 "

    num_cores = multiprocessing.cpu_count()
    max_cores_to_use = int(num_cores * 0.75)  # Limit to 75% of available cores

    with multiprocessing.Pool(processes=max_cores_to_use) as pool:
        pool.map(process_accession, accessions)

    print("All done")
