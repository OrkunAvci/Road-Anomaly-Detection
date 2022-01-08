import cv2 as cv

img_config = {
	"gauss": (5, 5),
	"threshold": 17
}

def process(image):
	out = cv.GaussianBlur(image, img_config["gauss"], 0)
	out = cv.Laplacian(out, cv.CV_8U)
	out = cv.adaptiveThreshold(out, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, img_config["threshold"], 2)
	out = cv.convertScaleAbs(out)
	return out
