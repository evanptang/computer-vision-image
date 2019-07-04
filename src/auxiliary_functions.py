import math

#The following functions are not complex. They simply go through the respective voting
#spaces and return the largest values. Nevertheless, I found that it would be neglectful
#to leave out documentation for this section.

#Find Largest is used in detect_normal and detect_slope_intercept for detection.py
#It takes in the voting space as well as the size of the voting space and returns the
#coordinate on the voting space with the largest amount of votes.

#Note that the function expects that the size will will be square.
def find_largest (voting, size):
	y_max = -1
	x_max = -1
	max_vote = -1
	for y in range(size):
		for x in range(size):
			if voting[y][x] > max_vote:
				max_vote = voting[y][x]
				y_max = y
				x_max = x
	return [y_max,x_max]

#Maximum Value is used in detect_circles of detection. It takes a voting space
#and searches for maximum value in that range. It then returns the maximum value
def maximum_value(vs, x_range, y_range):
	max_vote = -1
	for x in range(x_range):
		for y in range(y_range):
			if vs[x][y] > max_vote:
				max_vote = vs[x][y]
	return max_vote

#distance finds the cartesian coordiate distance between two points, (xi, yi) and
# (x, y). It is used in the voting fuction for circles (vote_circle) in vote_functions

#distance then returns that value as an integer.
def distance(xi, yi, x, y):
	ret_val =  int(math.sqrt(math.pow(abs(xi-x),2) + math.pow(abs(yi-y),2)))
	return ret_val
