#!/usr/bin/python3
import sys
import math
import numpy as np

def perc_90(nums):
	perc = np.percentile(nums,90)
	return '{:.2f}'.format(perc)

def median(nums):
	if len(nums)%2==0:
		mid_val_1 = int(nums[int(len(nums)/2) - 1])
		mid_val_2 = int(nums[int(len(nums)/2)])
		median = (mid_val_2+mid_val_1)/2		
	else:
		median =  int(nums[int((len(nums_list)-1)/2)])
	return '{:.2f}'.format(median)
def avg(nums):
	avg = sum(nums)/len(nums)
	return '{:.2f}'.format(avg)


with open (sys.argv[1], 'r') as nums:
	nums_list = list(map(int, nums.read().split()))
	nums_list.sort()
	data = (perc_90(nums_list)+'\n'+ median(nums_list)+'\n'+ '{:.2f}'.format(max(nums_list))+
		'\n'+ '{:.2f}'.format(min(nums_list))+'\n'+ avg(nums_list))
	print(data)		

