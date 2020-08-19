#!/usr/bin/env python
#-*-utf-8-*-
#jk	yin
#2020.08
import argparse
parser = argparse.ArgumentParser(description = "\nThis python script is used to parse the go-basic.obo file into tab delimited table", add_help = False, usage = "\n python3 parse_go.py -i [go-basic.obo] -o [go.txt] \n python3 parse_go.py --input [go-basic.obo] --output [go.txt]")
required = parser.add_argument_group("Required options")
optional = parser.add_argument_group("Optional options")
required.add_argument("-i", "--input", metavar = "[go-basic.obo]", help = "input file format: go_obo", required = True)
required.add_argument("-o", "--output", metavar = "[stat.txt]", help = "output file format: tab delimited table", required = True)
optional.add_argument("-h", "--help", action = "help", help = "help.info")
args = parser.parse_args()
genome_file = {}
with open(args.input,"r") as fi:
    with open(args.output,"w") as fo:
        print("GO\tDescription\tLevel",file = fo)
        for line in fi:
            if line.startswith("id"):
                print(''.join(line.split(" ")[1]).strip(), file = fo, end = '\t')
            elif line.startswith("name:",0,5):
                print(' '.join(line.split(" ")[1:]).strip(), file = fo, end = '\t')
            elif line.startswith("namespace",0,9):
                print(line.split(" ")[1].strip(), file = fo)

