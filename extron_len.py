#!/usr/bin/env python3
#2020.8
#-*-utf-8-*-
import argparse
parser = argparse.ArgumentParser(description = '\nThis is a python3 script used to count the length of human genome extron', add_help = False, usage = '\npython3 extron_len.py -i [human_extron.txt]')
required = parser.add_argument_group('Required options')
optional = parser.add_argument_group('Optional options')
required.add_argument('-i', metavar = '[human_extron.txt]', help = 'input: extron can be downloaded at https://ftp.ncbi.nlm.nih.gov/pub/CCDS/current_human/CCDS.current.txt', required = True)
optional.add_argument('-h','--help', action = 'help', help = 'help.info')
args = parser.parse_args()
extron = {}
with open(args.i,'r') as f:
    next(f)
    for line in f:
        line = line.split('\t')
        if line[9] != '-':
            extron_cor = line[9].lstrip('[').rstrip(']').split(', ')
        for i in range(len(extron_cor)):
            start = extron_cor[i].split('-')[0]
            extron[start] = extron_cor[i].split('-')[1]
length = 0
for i,j in extron.items():
    length += int(j.strip("'")) - int(i.strip("'")) + 1
print(length)


