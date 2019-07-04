import common
import struct, array

#The function readBmp takes a bmp image of size 640 by 480 and converts it into a 3D array
#with the RGB values encoded for each pixel (respectively from image[2][y][x] to
# image[0][y][x]).

#The function  then returns that 3D array. 
def readBmp(filename):
	image=[common.init_space(480,640) for x in range(3)]
	with open(filename, 'rb') as fd:
		header = fd.read(54)
		for y in range(479,-1,-1):
			row = list(bytearray(fd.read(640 * 3)))
			for x in range(640):
				index=x*3
				image[2][y][x]= row[index + 0]
				image[1][y][x]= row[index + 1]
				image[0][y][x]= row[index + 2]
	return image
