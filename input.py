# Dummy file
import cv2 as cv

dummy = {
	"path": "./resources/Senerio_3/",
	"file_no": 0,
	"file_extension": ".jpg",
	"max_frame": 6
}

def get_next():
	file = dummy["path"] + str(dummy["file_no"]) + dummy["file_extension"]
	dummy["file_no"] += 1
	dummy["file_no"] %= dummy["max_frame"]
	return cv.imread(file, 0)
