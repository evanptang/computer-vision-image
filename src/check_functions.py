import read_file
import detection
import auxiliary_functions

#this file simply calls the responsible functions and then outputs the results.
#Each of these files operates in the same fashion by reading the image, detecting the
#object and then printing the results.

def check_slopeintercept ( title, filename):
	success=True
	image=read_file.readBmp(filename)
	line = detection.detect_slope_intercept(image, 640, 480)
	print(title + " slope intercept results:")
	print("m: " + str(line.m))
	print("b: " + str(line.b))
	print("y = " + str(line.m) +"x + " + str(line.b))
	print
	return success

def check_normal (title, filename):
	success=True
	image=read_file.readBmp(filename)
	line = detection.detect_normal(image, 640, 480)
	print(title + " normal intercept results:")
	print("theta: " + str(line.theta))
	print("r: " + str(line.r))
	print("x*cos(" +str(line.theta) +") + y*sin(" + str(line.theta) + ") = " + str(line.r))
	print
	return success

def check_circles ( title, filename):
	success=True
	image=read_file.readBmp(filename)
	circles = detection.detect_circles(image,30,640,480)
	print(title + " normal intercept results:")
	print("detected: " + str(circles) + " circles")
	print
	return success
