import socket
import cv2 as cv
import pickle

target_ip = "127.0.0.1"
port = 6666
image = cv.imread("./resources/icon.png", 0)
print(image)

img_bytes = pickle.dumps(image)

print(img_bytes)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target_ip, port))
print("Connected.")

print("Sending...")
s.sendall(img_bytes)

