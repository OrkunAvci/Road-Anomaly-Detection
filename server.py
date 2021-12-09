import socket
from skimage import io
import pickle

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
		data = []
		received = conn.recv(4096)
		while received:
			data.append(received)
			received = conn.recv(4096)

	data = b"".join(data)
	print(data)
	img = pickle.loads(data)
	io.imshow(img)
	io.show()
