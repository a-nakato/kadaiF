# kadaie_1_main.py
import gzip

from Bio import SeqIO


def kadaie_1(input1: str, input2: int) -> None:
    fastafile = input1

    with gzip.open(fastafile, "rt") as handle:
        allrecords = 0
        count = 0
        for record in SeqIO.parse(handle, "fasta"):
            allrecords += 1
            if len(record.seq) <= input2:
                count += 1
        percent = (count / allrecords) * 100
        print(percent)
