#!/usr/bin/env python3
#jk	yin
#2020.05
import argparse
parser = argparse.ArgumentParser(description = "\nThis python script is used to extract sequence from genome in a fasta format file",add_help = False,usage = "\n python3 extract_genome.py -i [input.fasta] -o [output.fasta] -l [list.txt]\npython3 --i [input.fasta] --output [output.fasta] --list [list.txt]")
required = parser.add_argument_group("Required options")
optional = parser.add_argument_group("Optional options")
required.add_argument("-i", "--input", metavar = "[input.fasta]", help = "input file format: fasta",required = True)
required.add_argument("-o", "--output", metavar = "output.fasta", help = "output file format: fasta", required = True)
required.add_argument("-l", "--list", metavar = "list.txt", help = "seq_name\tpre_seq_id\torigin\tend\t(+/-) strand",required = True)
optional.add_argument("--detail", action = "store_true", help = "if this parameter been given, print the info of extracted seq", required = False)
optional.add_argument("-h", "--help", action = "help", help = "help info")
args = parser.parse_args()
#read input
genome = {}
with open(args.input, "r") as input_file:
	for line in input_file:
		line = line.strip()
		if line.startswith(">"):
			seq_id = line.split()[0]
			genome[seq_id] = ""
		else:
			genome[seq_id] += line
#read list
list_dict = {}
with open(args.list,"r") as input_list:
	for line in input_list:
		line = line.strip().split("\t")
		list_dict[line[0]] = [line[1], int(line[2]) - 1, int(line[3]) - 1,line[4]]
#rev_seq function
def rev_seq(seq):
	base_dict = {"A":"T","C":"G","T":"A","G":"C","a":"t","g":"c","t":"a","c":"g"}
	pre_seq_reversed = list(reversed(seq))
	seq_reversed_list = [base_dick[k] for k in pre_seq_reversed]
	seq_reveresed = "".join(seq_reversed_list)
	return(seq_reversed)
#extract sequence and then output
with open(args.output,"w") as output_file:
	for k,v in list_dict.items():
		if args.detail:
			print(">" + k, "[" + v[0],v[1] + 1, v[2] + 1, v[3] + "]", file = output_file)
		else:
			print(">" + k, file = output_file)
	seq = genome[">"+v[0]][v[1]:v[2]]
	if v[3] == "+":
		print(seq, file = output_file)
	elif v[3] == "-":
		print(rev_seq(seq),file = output_file)


