#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
#jk	yin
'''
This is a script for spliting sequence from a fasta file
'''
import sys
def usage():
        print('Usage: python3 split_merged_fa.py [fasta_file] [pair1_file] [pair2_file]')
def main():
	pair1 = open(sys.argv[2],"w")
	pair2 = open(sys.argv[3],"w")
	dic1 = {}
	dic2 = {}
	read_num = 0
	fi = open(sys.argv[1],"r")
	fi_all = fi.readlines()
	fi.seek(0)
	for line in fi:
		if line.startswith(">"):
			read_num += 1
			line_new = line.strip()
			seq_line = 2*read_num - 1
			if read_num % 2 == 0:
				dic2[line_new] = fi_all[seq_line].strip()
			else:
				dic1[line_new] = fi_all[seq_line].strip()
	for p1 in dic1:
		pair1.write(p1 + "\n")
		pair1.write(dic1[p1] + "\n")
	for p2 in dic2:
		pair2.write(p2 + "\n")
		pair2.write(dic2[p2] + "\n")
	pair1.close()
	pair2.close()
	fi.close()
try:
	main()
except	IndexError:
	usage()
