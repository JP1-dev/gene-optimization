import codon_optimization
import sequence_validation
import argparse
import os

MAX_SEQ_LENGTH = 1000000000000

parser = argparse.ArgumentParser(prog="gene-optimizer", description="tool to optimize a DNA-sequence")

parser.add_argument(
    "--origin",
    action="store",
    type=str,
    required=False,
    help="the organism where the input DNA comes from"
)

parser.add_argument(
    "--destination",
    action="store",
    type=str,
    required=False,
    help="the organism, for which the DNA should be optimized"
)

parser.add_argument(
    "--i",
    action="store",
    type=str,
    required=True,
    help="input file containing the DNA-sequence"
)

parser.add_argument(
    "--o",
    action="store",
    type=str,
    required=False,
    help="the optimized DNA is written to the output file"
)

args = parser.parse_args()

validator = sequence_validation.SeqValidator("DNA", True, True, MAX_SEQ_LENGTH)

optimizer = codon_optimization.CodonOptimizer("homo_sapiens", "escherichia_coli_K12")

if args.origin and args.destination:
    optimizer.change_organisms(args.origin, args.destination)

elif args.origin is None and args.destination:
    optimizer.change_organisms("homo_sapiens", args.destination)

elif args.origin and args.destination is None:
    optimizer.change_organisms(args.origin, "escherichia_coli_K12")

print(f"configuration: {optimizer.origin_name} ---> {optimizer.target_name}")

if not os.path.exists(args.i):
    raise FileNotFoundError(args.i)

lst = []

print("reading input file...")
with open(args.i, 'r') as file:
    for line in file:
        if line[0] == '>' or line[0] == ' ':
            continue
        lst.append(line)


inputSeq = "".join(lst).replace(" ", "").replace("\n", "")
print("input Sequence read!")
# print(inputSeq)

isValid = validator.validate(inputSeq)
if not isValid:
    raise Exception("file doesn't contain valid DNA")

print("DNA is valid!")

print("optimizing DNA...")
optimizedSeq = optimizer.optimize(inputSeq, isDNA=True, returnDNA=True)
print("DNA optimized!")

output = "out.fa"
if args.o:
    output = args.o

with open(output, 'w') as file:
    file.write(optimizedSeq)

print(f"optimization successful! result was written to {output}")

