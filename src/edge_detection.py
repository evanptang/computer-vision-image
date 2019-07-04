import common

#There are probably more elegant ways to do edge detection but the following is a quick solution
#consisting of three functions, neighbor, edge_only and check_point

#edge_only takes the array consisting of every RGB value and returns an image of
#just the edges. The way this is done is quite rudimentary but the general gist is
#through detecting if the pixel is indeed alone
def edge_only(image):
	edge_image=common.init_space(480, 640)
	for x in range(640):
		for y in range(480):
			if image[0][y][x] != 255 and image[1][y][x] != 255 and image[2][y][x] != 255:
				if neighbor(x, y, image):
					edge_image[y][x] = 1
	return edge_image

#check_point is called in neighbor. If the poin is indeed black, the program returns False
def check_point (x, y, image):
	if image[0][y][x] == 0 and image[1][y][x] == 0 and image[2][y][x] == 0:
		return False
	else:
		return True
#Neighbor simply takes into account whether there are any neighboring pixels. If There
#are indeed neighboring pixel(s), the program returns False. Else, it returns True.

#Note that neighbor is hardcoded to consider all edge cases for a image 640x480.
#There is likely a more elegant solution. However, this was the most straightforward.
def neighbor(x,y, image):
	value = False
	if x<= 638 and x>=1 and y<=478 and y>=1:
		if check_point(x+1, y+1, image):
			value = True
		if check_point(x+1, y, image):
			value = True
		if check_point(x+1, y-1, image):
			value = True
		if check_point(x-1, y+1, image):
			value = True
		if check_point(x-1, y, image):
			value = True
		if check_point(x-1, y-1, image):
			value = True
		if check_point(x, y+1, image):
			value = True
		if check_point(x, y-1, image):
			value = True
	elif x== 639 and y<=478 and y>=1:
		if check_point(x-1, y+1, image):
			value = True
		if check_point(x-1, y, image):
			value = True
		if check_point(x-1, y-1, image):
			value = True
		if check_point(x, y+1, image):
			value = True
		if check_point(x, y-1, image):
			value = True
	elif x == 0 and y<=478 and y>=1:
		if check_point(x+1, y+1, image):
			value = True
		if check_point(x+1, y, image):
			value = True
		if check_point(x+1, y-1, image):
			value = True
		if check_point(x, y+1, image):
			value = True
		if check_point(x, y-1, image):
			value = True
	elif x==639 and y == 0:
		if check_point(x-1, y+1, image):
			value = True
		if check_point(x-1, y, image):
			value = True
		if check_point(x, y+1, image):
			value = True
	elif x==639 and y == 479:
		if check_point(x-1, y, image):
			value = True
		if check_point(x-1, y-1, image):
			value = True
		if check_point(x, y-1, image):
			value = True
	elif x==0 and y == 0:
		if check_point(x+1, y+1, image):
			value = True
		if check_point(x+1, y, image):
			value = True
		if check_point(x, y+1, image):
			value = True
	elif x==0 and y == 479:
		if check_point(x+1, y, image):
			value = True
		if check_point(x+1, y-1, image):
			value = True
		if check_point(x, y-1, image):
			value = True
	elif y==479:
		if check_point(x+1, y, image):
			value = True
		if check_point(x+1, y-1, image):
			value = True
		if check_point(x, y-1, image):
			value = True
		if check_point(x-1, y, image):
			value = True
		if check_point(x-1, y-1, image):
			value = True
	elif y==0:
		if check_point(x+1, y, image):
			value = True
		if check_point(x+1, y+1, image):
			value = True
		if check_point(x, y+1, image):
			value = True
		if check_point(x-1, y, image):
			value = True
		if check_point(x-1, y+1, image):
			value = True
	return value
