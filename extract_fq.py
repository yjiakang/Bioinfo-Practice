# -*- coding: utf-8 -*-
'''
This is a script for extracting sequence from a fasta file
'''
import sys
import os
def usage():
	print('Usage: python3 script.py [fasta_file] [idlist_file] [outfile_name]')
def main():
	fo = open("new.fq","w+")
	dic = {}
	with open(sys.argv[1],"r") as fi:
		for line in fi:
			if line.startswith("@"):
				name = line.strip()
				dic[name] = "" 
			elif line.startswith("+"):
				continue
			else:
				dic[name] += line
	with open(sys.argv[2],"r") as listf:
		for i in listf:
			i = i.strip()
			for key in dic:
				if key == i:
					fo.write(">" + key + "\n")
					fo.write(dic[key] + "\n")
	fo.seek(0)
	f2 = open(sys.argv[3],"w")
	for line in fo:
		line = line.strip()
		if len(line) != 0:
			f2.write(line)
			f2.write("\n")
	fo.close()
	f2.close()
	os.remove("new.fq")
try:
	main()
except IndexError:
	usage()
	
