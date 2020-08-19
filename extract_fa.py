# -*- coding: utf-8 -*-
'''
#This is a script for extracting sequence from a fasta file
'''
import sys
def usage():
	print('Usage: python3 script.py [fasta_file] [idlist_file] [outfile_name]')
def main():
	fo = open(sys.argv[3],"w")
	dic = {}
	with open(sys.argv[1],"r") as fi:
		for line in fi:
			if line.startswith(">"):
				name = line.strip().split()[0][1:]
				dic[name] = "" 
			else:
				dic[name] += line.replace("\n","")
	with open(sys.argv[2],"r") as listf:
		for i in listf:
			i = i.strip()
			for key in dic:
				if key == i:
					fo.write(">" + key + "\n")
					fo.write(dic[key] + "\n")
	fo.close()
try:
	main()
except IndexError:
	usage()
	
