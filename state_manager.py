import numpy as np
from skimage import io

states = {}

def new_state(id: str) -> None:
	states[id] = {
		"id": id,
		"next_option": 1,
		"background": np.ndarray([]),
		"crash_flag": [0, 0, 0]
	}

def detect(id: str, img) -> None:
	clean_img = img - states[id]["background"]
	#   Do magic

	#   Set flags and state

	#   Done
	io.imshow(clean_img)
	io.show()
