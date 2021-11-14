import socket
import numpy
from skimage import io
from io import BytesIO
import numpy as np

def array_to_bytes(x: np.ndarray) -> bytes:
    np_bytes = BytesIO()
    np.save(np_bytes, x, allow_pickle=True)
    return np_bytes.getvalue()

def bytes_to_array(b: bytes) -> np.ndarray:
    np_bytes = BytesIO(b)
    print(np_bytes)
    return np.load(np_bytes, allow_pickle=True)

self_ip = "127.0.0.1"
port = 6666

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	print("Socket Ready.")
	s.bind((self_ip,port))
	print("Bound.")
	print("Listening...")
	s.listen()

	conn, addr = s.accept()
	print("Connected by", addr)

	with conn:
		data = conn.recv(65536)
		print(data)
		conn.sendall(data)
		img = bytes_to_array(data)
		io.imshow(img)
		io.show()
