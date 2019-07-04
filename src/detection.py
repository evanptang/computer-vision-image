import common
import math
import edge_detection
import convert_values
import vote_functions
import auxiliary_functions

#This file contains all the detection functions. For the sake of clarity, I have
#removed all helper functions and placed them in their respective files

#There are three functions that are written here.
#	-detect_slope_intercept
#	-detect_normal
#	-detect_circles

#They all take in the same parameter image as defined as a BMP file converted into
#a multidimensional array. Each pixel of this array has 3 values accessible (The RGB Value).

#Each function utilizes its own vote function. Documentations of those vote functions
#as well as the actual functions is contained within vote_functions.py


#This function is specific to detecting and returning the best fit line in slope intercept
#form. It votes in the Hough Space Vote Box defined as in between 2000 and 2000.

#The function returns the slope and intercept value in the self defined data structure line
def detect_slope_intercept(image, x_range, y_range):
	vote_box = [[0 for col in range(2000)] for row in range(2000)]
	for x in range(x_range):
		for y in range(y_range):
			if image[0][y][x] == 0 and image[1][y][x]==0 and image[2][y][x] == 0:
				vote_functions.vote_slope(x,y,vote_box)
	data = auxiliary_functions.find_largest(vote_box, 2000)
	line=common.Line()
	line.m=convert_values.index_to_value(data[0],2000,-10,10)
	line.b=convert_values.index_to_value(data[1],2001,-1000,1000)
	return line

#This function detects the best approximation of the line in the image based on
#polar format. It operates extremely similar to detect_slope_intercept with the
#exception of the vote function.

#The function returns the R and Theta value in the self defined data structure line
def detect_normal(image, x_range, y_range):
	vote_box = [[0 for col in range(1800)] for row in range(1800)]
	for x in range(x_range):
		for y in range(y_range):
			if image[0][y][x] == 0 and image[1][y][x]==0 and image[2][y][x] == 0:
				vote_functions.vote_normal(x,y,vote_box)
	line=common.Line()
	data = auxiliary_functions.find_largest(vote_box, 1800)
	line.r=convert_values.index_to_value(data[1],1800,-900,900)
	line.theta=convert_values.index_to_value(data[0],1800,0,3.14159)
	return line

#This function detects the number of circles present in the picture.
#In order for this function to work,the size of the radius must be previously known.
# Additionally it can only return one radius size at a time.

#The function returns the number circles of that size.
def detect_circles(image, radius, x_range, y_range):
	#initializing a vote space of the same size of the image
	vote=[[0 for col in range(y_range)] for row in range(x_range)]
	edge_image = edge_detection.edge_only(image)
	for x in range(x_range):
		for y in range(y_range):
			if edge_image[y][x] == 1:
				vote_functions.vote_circle(x, y, radius ,vote)
	max_vote = auxiliary_functions.maximum_value(vote, x_range, y_range)
	counter = 0
	for i in range(x_range):
		for j in range(y_range):
			if vote[i][j] == max_vote:
				counter = counter+1
	return counter
