#!/usr/bin/env python
#-*-utf-8-*-
#jk	yin
#2020.07
import argparse
import re
parser = argparse.ArgumentParser(description = "\nThis python script is used to summarize base info including A/T/G/C/GC/N content", add_help = False, usage = "\n python3 stat_hg19.py -i [input.fasta] -o [stat.txt] \n python3 seq_split.py --input [input.fasta] --output [stat.txt]")
required = parser.add_argument_group("Required options")
optional = parser.add_argument_group("Optional options")
required.add_argument("-i", "--input", metavar = "[input.fasta]", help = "input file format: fasta", required = True)
required.add_argument("-o", "--output", metavar = "[stat.txt]", help = "output file format: fasta", required = True)
optional.add_argument("-h", "--help", action = "help", help = "help.info")
args = parser.parse_args()
genome_file = {}
with open(args.input,"r") as fi:
        for line in fi:
                line = line.strip()
                if line.startswith(">"):
                        seq_id = line.split(">")[1]
                        genome_file[seq_id] = ''
                else:
                        genome_file[seq_id] +=line
#summarize base info :A/T/C/G/GC/N content
with open(args.output,"w") as fo:
        print("Chrome\tstart\tend\tA\tT\tC\tG\tGC\tN",file = fo)
        for k,v in genome_file.items():
            print(k, file = fo, end = '\t')
            print(100 * (len(re.findall('[Aa]', v)) / len(v)), file = fo, end = '\t')
            print(100 * (len(re.findall('[Tt]', v)) / len(v)), file = fo, end = '\t')
            print(100 * (len(re.findall('[Gg]', v)) / len(v)), file = fo, end = '\t')
            print(100 * (len(re.findall('[Cc]', v)) / len(v)), file = fo, end = '\t')
            print(100 * (len(re.findall('[GCgc]', v)) / len(v)), file = fo, end = '\t')
            print(100 * (len(re.findall('[Nn]', v)) / len(v)), file = fo)
