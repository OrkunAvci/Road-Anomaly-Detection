import socket
import pickle

import input

target_ip = "127.0.0.1"
port = 6666

for i in range(4):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((target_ip, port))
	print("Connected.")
	image = input.get_next()
	img_bytes = pickle.dumps(image)

	print("Size: " + str(len(bytes(len(img_bytes)))))
	print("Sending...")
	s.sendall(img_bytes)
	print("Sent.")
