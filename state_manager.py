import numpy as np
from skimage import io

states = {}

def new_state(id: str) -> None:
	states[id] = {
		"id": id,
		"next_option": 1,
		"background": np.ndarray([]),
		"flags": [0, 0, 0]
	}

def process(img, mult, s_x, s_y):
	part = [[cell for cell in row[s_y * mult : (s_y + 1) * mult]] for row in img[s_x * mult : (s_x + 1) * mult]]
	out = {
		"avg" : sum([sum(row) for row in part]) / (mult * mult),
		"x" : s_x,
		"y" : s_y
	}
	return out

def detect(id: str, img) -> None:
	clean_img = img - states[id]["background"]
	#   Do magic
	mult = 12
	out = [[process(clean_img, mult, i, j) for j in range(int(img.shape[1] / mult))] for i in range(int(img.shape[0] / mult))]
	here = []
	for row in out :
		for cell in row :
			if cell["avg"] != 0 :
				here.append(cell)
	here = sorted(here, key = lambda item : item["avg"])
	print("Relevant cell number: ", len(here), "\tAvg : %.2f" % (sum([cell["avg"] for cell in here]) / len(here)))
	print("X Avg : %.2f" % (sum([cell["x"] for cell in here]) / len(here)))
	print("Y Avg : %.2f" % (sum([cell["y"] for cell in here]) / len(here)))

	#   Set flags and state

	#   Done
	io.imshow(clean_img)
	io.show()
