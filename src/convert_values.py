#In order to convert from the Hough space to the actual image as well as the reverse,
#the following two functions were written. Value referes to the actual image value
# while index refers to the Hough space value.

def value_to_index (value, size, lb, up):
	rangesize = (up-lb)
	offset = (value - lb)
	index = (offset/float(rangesize))*size
	return index

def index_to_value (index, size, lb, up):
	rangesize = (up-lb)
	value = (index/float(size))*rangesize +lb
	return value
