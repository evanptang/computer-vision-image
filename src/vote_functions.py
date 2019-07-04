import convert_values
import math
import auxiliary_functions

#The following functions utilize this idea of translating images to parameter spaces
#where each point in the image space translates to a series of votes in the parameter space.

def vote_slope (x, y, voting):
	for mi in range (2000):
		m = convert_values.index_to_value(mi, 2000, -10, 10)
		b = -1* (m * x) + y
		bi = convert_values.value_to_index (b, 2001, -1000, 1000)
		if bi-int(bi)>=0.5:
			int_bi = int(bi)+1
		else:
			int_bi = int(bi)
		if int_bi >= 0 and int_bi <2000:
			voting[mi][int_bi] = voting[mi][int_bi]  + 1


def vote_normal (x, y, voting):
	pi = 3.14159
	for theta_i in range(1800):
		theta = convert_values.index_to_value(theta_i, 1800, 0 , pi)
		roh = x*math.cos(theta)+y*math.sin(theta)
		roh_i = convert_values.value_to_index(roh, 1800, -900, 900)
		if roh_i-int(roh_i)>=0.5:
			int_roh_i = int(roh_i)+1
		else:
			int_roh_i = int(roh_i)
		if int_roh_i >= 0 and int_roh_i < 1800:
			voting[theta_i][int_roh_i] = voting[theta_i][int_roh_i] + 1

def vote_circle (x, y, r, vs):
	sx = x - r
	sy = y - r
	for i in range(r):
		for j in range(r):
			d = auxiliary_functions.distance (sx+i, sy+j, x, y)
			if d == r:
				vote_circle_check_bounds(sx+i, sy+j, vs)
			elif d<r:
				break

def vote_circle_check_bounds(x, y, vs):
	if x >=0 and x<=639 and y>=0 and y<=479:
		vs[x][y] = vs[x][y] +1
