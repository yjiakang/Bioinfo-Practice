#!/usr/bin/env python3
#-*-coding:utf-8-*-
#jk	yin
#2020.03
import argparse
parser = argparse.ArgumentParser(description = "\nThis python script is used to display sequence with designed length", add_help = False, usage = "\n python3 seq_split.py -i [input.fasta] -o [output.fasta] -l [length per line] \n python3 seq_split.py --input [input.fasta] --output [output.fasta] --length [length per line]")
required = parser.add_argument_group("Required options")
optional = parser.add_argument_group("Optional options")
required.add_argument("-i", "--input", metavar = "[input.fasta]", help = "input file format: fasta", required = True)
required.add_argument("-o", "--output", metavar = "[output.fasta]", help = "output file format: fasta", required = True)
required.add_argument("-l", "--length", metavar = "[length per line]", help = "length per line to display", required = True)
optional.add_argument("-h", "--help", action = "help", help = "help.info")
args = parser.parse_args()
#read input file
input_file = {}
with open(args.input,"r") as fi:
	for line in fi:
		line = line.strip()
		if line.startswith(">"):
			seq_id = line
			input_file[seq_id] = ''
		else:
			input_file[seq_id] += line

with open(args.output,"w") as fo:
	for k,v in input_file.items():
		print(k, file = fo)
		while len(v) > int(args.length):
			print(v[0:int(args.length)],file = fo)
			v = v[int(args.length):len(v)]
		print (v, file = fo)
		
