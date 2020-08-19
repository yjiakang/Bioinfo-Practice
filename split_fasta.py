#!/usr/bin/env python
#jk	yin
#2020.2
import sys
def usage():
	print("please input [file_to_split] [seq_per_file]]")
def main():
	i = 1
	fileseqnum = 0
	ls = []
	fi =  open(sys.argv[1],"r")
	for line in fi:
		if line.startswith(">"):
			fileseqnum += 1
	seqperfile = fileseqnum//4
	if fileseqnum % 4 == 0:
		for num in range(4):
			file_name = str(i)+".fa"
			out = open(file_name,"w")
			ls.append(file_name)
			i += 1
			out.close()
	else:
		for num in range(5):
			file_name = str(i)+".fa"
			out = open(file_name,"w")
			ls.append(file_name)
			i += 1
			out.close()
	filenum = 0
	seqnum = 0
	limit = 0
	fi.seek(0)
	for l in fi:
		fo = open(ls[filenum],"a")
		if l.startswith(">"):
			seqnum += 1
		if seqnum <= (limit+seqperfile):
			fo.write(l)
		else:
			fo.close()
			limit += seqperfile
			filenum += 1
			fo = open(ls[filenum],"a")
			fo.write(l)
	fi.close()
try:
	main()
except:
	usage()
