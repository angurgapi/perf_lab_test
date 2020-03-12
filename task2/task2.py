#!/usr/bin/python3
import sys

with open (sys.argv[1], 'r') as rect_file:
	rect = rect_file.read().strip()
	rect_coords = rect.split('\n')
	rect_x = []
	rect_y = []
	for coord in rect_coords:
		rect_x.append(float(coord.split()[0]))
		rect_y.append(float(coord.split()[1]))

with open (sys.argv[2], 'r') as spots_file:
	spots = spots_file.read().strip()
	spots_coords = spots.split('\n')
	

def inside_rect(spot, rect_x, rect_y):	
	spot_x = float(spot.split()[0])
	spot_y = float(spot.split()[1])
	ans=0
	for i in range(4):
		if (((rect_y[i]<=spot_y and spot_y<rect_y[i-1]) or (rect_y[i-1]<=spot_y and spot_y<rect_y[i])) and \
			(spot_x > (rect_x[i-1] - rect_x[i]) * (spot_y - rect_y[i]) / (rect_y[i-1] - rect_y[i]) + rect_x[i])):
			ans = 1 - ans   
	return ans

def on_borders(spot, rect_x, rect_y):
	spot_x = float(spot.split()[0])
	spot_y = float(spot.split()[1])
	if rect_x[0]==rect_x[1] and rect_x[2]==rect_x[3] or rect_y[0]==rect_y[3] and rect_y[1]==rect_y[2]:
		if spot_x in rect_x and max(rect_y)>spot_y>min(rect_y) or spot_y in rect_y and max(rect_x)>spot_x>min(rect_x):
			return True
	else:
		for i in range(4):
			if (spot_x-rect_x[i])/(rect_x[i+1]-rect_x[i])==(spot_y-rect_y[i])/(rect_y[i+1]-rect_y[i]):
				return True

for spot in spots_coords:
	if spot in rect_coords:
		print(0)
	elif on_borders(spot, rect_x, rect_y)==True:
		print(1)
	elif inside_rect(spot, rect_x, rect_y)==True:
		print(2)
	else:
		print(3)

