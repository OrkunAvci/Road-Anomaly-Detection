import socket
import pickle
import time
import os

import input

target_ip = "127.0.0.1"
port = 6666

def get_obj(conn):
	with conn :
		data = []
		received = conn.recv(4096)
		while received :
			data.append(received)
			received = conn.recv(4096)
	data = b"".join(data)
	data = pickle.loads(data)
	return data

for i in range(3):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((target_ip, port))
	print("Connected.")
	image = input.get_next()
	img_bytes = pickle.dumps(image)

	print("ID:", i)
	print("Size: " + str(len(bytes(len(img_bytes)))))
	print("Sending...")
	s.sendall(img_bytes)
	print("Sent.")
	print("---------------------------")
	time.sleep(1)
	s.close()
	os.system("pause")
