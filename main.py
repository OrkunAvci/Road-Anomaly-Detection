import numpy
from skimage import data, io, filters
import cv2 as cv

import input
import process_image as pi

for i in range(4):
	img = input.get_next()
	io.imshow(img)
	io.show()
	p_img = pi.process(img)
	io.imshow(p_img)
	io.show()
