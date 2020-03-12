#!/usr/bin/python3
import os,sys

path = sys.argv[1]
files = os.listdir(path)
all_files = []
for i in range(5):
	full_path = path + '/' + files[i]
	with open(full_path, 'r') as item:
		all_files.append(item.read())

all_lists = []
for cd in all_files:
	all_lists.append(list(map(float, cd.strip().split('\n'))))

totals = []
for i in range(16):
	sum_cd = 0
	for j in range(5):
		sum_cd += all_lists[j][i]
	totals.append(sum_cd)

for element in totals:
	if element==max(totals):
		print(totals.index(element)+1)
		break

