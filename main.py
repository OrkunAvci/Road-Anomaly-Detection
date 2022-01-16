import numpy
from skimage import data, io, filters
import cv2 as cv
import math
import pprint

import input
import process_image as pi

for i in range(7):
	img = input.get_next()
	img = pi.process(img)
	io.imshow(img)
	io.show()
