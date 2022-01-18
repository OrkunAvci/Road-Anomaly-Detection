# Dummy file
import cv2 as cv
import os

dummy = {
	"path": "./resources/Scenario_1/",
	"file_no": 0,
	"file_extension": ".jpg"
}
dummy["max_frame"] = len([name for name in os.listdir(dummy["path"]) if os.path.isfile(os.path.join(dummy["path"], name)) if name.endswith(dummy["file_extension"])])

def get_next():
	file = dummy["path"] + str(dummy["file_no"]) + dummy["file_extension"]
	dummy["file_no"] += 1
	dummy["file_no"] %= dummy["max_frame"]
	return cv.imread(file, 0)
