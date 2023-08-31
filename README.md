# fasterStringTie

Presenting fasterStringTie that is significantly (3 times) faster than the original StringTie.

### Overview

The original StringTie tool, developed by Pertea M, Pertea GM, Antonescu CM, Chang TC, Mendell JT & Salzberg SL, revolutionized transcriptome reconstruction from RNA-seq data with its remarkable speed and accuracy (Nature Biotechnology 2015, doi:10.1038/nbt.3122). However, one glaring issue with StringTie is its underutilization of computational resources, specifically threads, cores, and processors, even when provided as parameters.

### The Problem

For instance, during the initial transcriptome assembly, StringTie often fails to harness the full potential of available threads or cores, even when specified using the "-p" parameter. This limitation becomes particularly pronounced when dealing with a large number of samples, as discussed by the authors themselves in their paper (http://dx.doi.org/10.1038/nprot.2016.095) and reported as issues on their GitHub repository (https://github.com/gpertea/stringtie/issues/2).

Despite creating BASH or Python loop structures (which is a common practice for bioinformatics researchers), this suboptimal resource utilization results in a linear processing flow, where one sample patiently waits in a queue for the preceding one to complete analysis—a process that can consume significant time due to the failure to leverage all available computing resources.

### The Solution

To address this issue, I present the fasterStringTie Python package. This tool resolves the problem by accepting a set of BAM files as input for transcriptome assembly. It then efficiently distributes these BAM files across multiple cores and threads on your machine simultaneously, employing multiprocessing and subprocesses. This parallelization approach ensures that most of your machine's resources are dedicated to the transcriptome assembly task, significantly enhancing efficiency.

However, it's important to note that fasterStringTie is designed to cap resource consumption at a maximum of 75% of CPU resources, ensuring stability and preventing system overload.

### Installation and Usage

pip install fasterStringTie

usage: python -m fasterStringTie [-h] [-i INPUT_DIR] [-o OUTPUT_DIR] [-r REFERENCE]
                          accessions_file

Faster Transcriptome Assembly of BAM files using StringTie.

positional arguments:
  accessions_file       Path to the accessions.txt file

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_DIR, --input_dir INPUT_DIR
                        Directory where the BAM files are located
  -o OUTPUT_DIR, --output_dir OUTPUT_DIR
                        Output directory
  -r REFERENCE, --reference REFERENCE
                        Path to the reference GTF file

Example run: python -m fasterStringTie accessions.txt -i /media/waqar/hdd/easeRNAseq/E-MTAB-8412_colorectal_border/mapping/bam_sorted -o ~/Desktop/test-string -r /opt/Homo_sapiens.gtf

Contributions and Feedback

Your contributions and feedback are invaluable. If you encounter issues or have suggestions for improvement, please don't hesitate to get in touch. waqar@biocode.ltd

License

This project is open-source and released under the MIT License.

Thank you for choosing fasterStringTie to supercharge your transcriptome assembly process!