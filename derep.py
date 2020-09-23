#!/usr/bin/env python3 
#-*-coding : utf-8 -*-
import argparse
parser = argparse.ArgumentParser(description = "\nThis python script is used to extrac the first line among all the line with same start", add_help = False, usage = "\n python3 derep.py -i [input] -o [output] \n python3 seq_split.py --input [input] --output [output]")
required = parser.add_argument_group("Required options")
optional = parser.add_argument_group("Optional options")
required.add_argument("-i", "--input", metavar = "[input]", help = "input file", required = True)
required.add_argument("-o", "--output", metavar = "[output.fasta]", help = "output file", required = True)
optional.add_argument("-h", "--help", action = "help", help = "help.info")
args = parser.parse_args()
#read input file
output_dict = {}
with open (args.input, "r") as fi:
	for line in fi:
		start = line.split('\t')[0]
		if start not in output_dict.keys():
			output_dict[start] = line
		else:
			continue
with open (args.output, "w") as fo:
	for k,v in output_dict.items():
		print(k, file = fo)
		print(v, file = fo)
