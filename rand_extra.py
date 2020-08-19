#!/usr/bin/env python
#jk	yin
#2020.01
def main():
	import random
	import sys
	f1 = open(sys.argv[3],"r")
	d1 = {}
	for line1 in f1:
		if line1.startswith("@"):
			name1 = line1.strip()
			d1[name1] = ""
		elif line1.startswith("+"):
			continue
		else:
			d1[name1] += line1
	random.seed(sys.argv[1])
	lt = list(d1.items())
	lnew = []
	seqnum = 0
	flag = 1
	ls = []
	while flag:
		num = random.randint(0,len(lt)-1)
		if num not in ls:
			ls.append(num)
			lnew.append(lt[num])
			seqnum += 1
		if seqnum == sys.argv[2]:
			flag = 0
	with open(sys.argv[5],"w") as fn1:
		for k in lnew:
			fn1.write(k[0]+"\n"+k[1])
	f2 = open(sys.argv[4],"r")
	d2 = {}
	for line2 in f2:
		if line2.startswith("@"):
			name2 = line2.strip()
			d2[name2] = ""
		elif line2.startswith("+"):
			continue
		else:
			d2[name2] += line2
	with open(sys.argv[6],"w") as fn2:
		for j in lnew:
			for key in d2.keys():
				if key.split()[0] == j[0].split()[0]:
					fn2.write(key+"\n")
					fn2.write(d2[key])
	f1.close()
	f2.close()
main()
