#!/usr/bin/env python3
#-*-utf-8-*-
import argparse
import re

parser = argparse.ArgumentParser(description = "\nThis python script is used to summarize base info including A/T/G/C/GC content with a given window slide", add_help = False, usage = "\n python3 stat_window.py -i [input.fasta] -o [stat.txt] -w [window size] \n python3 seq_split.py --input [input.fasta] --output [stat.txt] --window [window size]")
required = parser.add_argument_group("Required options")
optional = parser.add_argument_group("Optional options")
required.add_argument("-i", "--input", metavar = "[input.fasta]", help = "input file format: fasta", required = True)
required.add_argument("-o", "--output", metavar = "[stat.txt]", help = "output file format: fasta", required = True)
required.add_argument("-w", "--window", metavar = "[window size]", help = "window size to check", required = True)
optional.add_argument("-h", "--help", action = "help", help = "help.info")
args = parser.parse_args()
#read input file
genome_file = {}
with open(args.input,"r") as fi:
	for line in fi:
		line = line.strip()
		if line.startswith(">"):
			seq_id = line.split(">")[1]
			genome_file[seq_id] = ''
		else:
			genome_file[seq_id] +=line
#summarize base info :A/T/C/G/GC content
with open(args.output,"w") as fo:
	print("Seq_id\tstart\tend\tA\tT\tC\tG\tGC",file = fo)
	for k,v in genome_file.items():
		start = list(range(0,len(v)-int(args.window),int(args.window)))
		end = list(range(int(args.window),len(v),int(args.window)))
	if end == []:
		start.append(0)
		end.append(len(v))
	elif end[-1] < len(v):
		start.append(start[-1] + int(args.window))
		end.append(len(v))
	for i in range(0,len(start)):
		split_seq = v[start[i]:end[i]]
		split_len = end[i] - start[i]
		print(f'{seq_id}\t{start[i] + 1}\t{end[i]}', file = fo, end = '\t')
		print(str(round(100 * len(re.findall('[Aa]', split_seq)) / split_len, 2)), file = fo, end = '\t')
		print(str(round(100 * len(re.findall('[Tt]', split_seq)) / split_len, 2)), file = fo, end = '\t')
		print(str(round(100 * len(re.findall('[Gg]', split_seq)) / split_len, 2)), file = fo, end = '\t')
		print(str(round(100 * len(re.findall('[Cc]', split_seq)) / split_len, 2)), file = fo, end = '\t')
		print(str(round(100 * len(re.findall('[GCgc]', split_seq)) / split_len, 2)), file = fo)
		
