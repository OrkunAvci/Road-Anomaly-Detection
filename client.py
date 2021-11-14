import socket
import cv2 as cv
from io import BytesIO
import numpy as np

def array_to_bytes(x: np.ndarray) -> bytes:
    np_bytes = BytesIO()
    np.save(np_bytes, x, allow_pickle=True)
    return np_bytes.getvalue()

def bytes_to_array(b: bytes) -> np.ndarray:
    np_bytes = BytesIO(b)
    return np.load(np_bytes, allow_pickle=True)

target_ip = "127.0.0.1"
port = 6666
image = cv.imread("./resources/dog.pgm", 0)
print(image)
print()

print(array_to_bytes(image))
print()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target_ip, port))

s.sendall(array_to_bytes(image))
res = s.recv(65536)

print(repr(res))
