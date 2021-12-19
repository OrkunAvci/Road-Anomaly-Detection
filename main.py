import numpy
from skimage import data, io, filters
import cv2 as cv




#  Dump
"""
#   Get image
image = cv.imread("./resources/dog.pgm", 0)
#image = ski_color.rgb2gray(data.rocket())
edges = filters.sobel(image)

#   Normalize
prev_max = edges.max()
limit = edges.mean()
top_arr = []
for row in edges:
	sub_arr = []
	for cell in row:
		if (cell / prev_max) > 0.01:
			sub_arr.append(cell / prev_max)
		else:
			sub_arr.append(0.0)
	top_arr.append(sub_arr)
edges = numpy.array(top_arr)

#   Output
print(edges.min(), edges.max(), edges.mean())
io.imshow(edges)
io.show()
"""
