# kadaie_1.py
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

from kadai.kadaie_1_main import kadaie_1


def main():
    parser = ArgumentParser(
        formatter_class=ArgumentDefaultsHelpFormatter,
        description="Count sequences in a FASTA file shorter than or equal to a given length.",
    )
    parser.add_argument(
        "-i",
        "--input1",
        help="FASTA file name",
        type=str,
        required=True,
    )
    parser.add_argument(
        "-l",
        "--input2",
        help="sequence length",
        type=int,
        required=True,
    )
    args = parser.parse_args()
    kadaie_1(args.input1, args.input2)


if __name__ == "__main__":
    main()
