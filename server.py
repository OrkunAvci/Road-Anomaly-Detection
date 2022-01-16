import socket
import pickle
import process_image as pi
import time
import os

self_ip = "127.0.0.1"
port = 6666

def process(img, mult, s_x, s_y, prev):
	part = [[cell for cell in row[s_y * mult : (s_y + 1) * mult]] for row in img[s_x * mult : (s_x + 1) * mult]]
	out = {
		"avg" : sum([sum(row) for row in part]) / (mult * mult),
		"x" : s_x,
		"y" : s_y,
		#"out_of_bounds" : False,
		"previous_state" : prev
	}
	return out

def do_something(img, prev):
	mult = 12
	out = [[process(img, mult, i, j, prev) for j in range(int(img.shape[1] / mult))] for i in
	       range(int(img.shape[0] / mult))]
	print("Original cell number: ", sum([len(row) for row in out]), "\tAvg : %.2f"%(sum([sum([cell["avg"] for cell in row]) for row in out]) / sum([len(row) for row in out])))
	here = []
	for row in out :
		for cell in row :
			if cell["avg"] != 0.0 :
				here.append(cell)
	print("Non-zero cell number: ", len(here), "\tAvg : %.2f"%(sum([cell["avg"] for cell in here]) / len(here)))
	here = [cell for cell in here if cell["avg"] > 15.0]
	here = sorted(here, key = lambda item : item["avg"])
	print("Relevant cell number: ", len(here), "\tAvg : %.2f"%(sum([cell["avg"] for cell in here]) / len(here)))
	print("X Avg : %.2f"%(sum([cell["x"] for cell in here]) / len(here)))
	print("Y Avg : %.2f"%(sum([cell["y"] for cell in here]) / len(here)))
	return here

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

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	print("Socket Ready.")
	s.bind((self_ip,port))
	print("Bound.")
	print("Listening...")
	s.listen(10)

	conn, addr = s.accept()
	print("Connected by", addr)
	background = get_obj(conn)
	background = pi.process(background)
	print("Background ready.")
	print("---------------------------")

	prev = None
	for i in range(2):
		print("Awaiting connection...")
		conn, addr = s.accept()
		print("Connected by", addr)
		print("ID: ", i + 1)
		start = time.time()
		img = get_obj(conn)
		print("Processing...")
		img = pi.process(img)
		img = img - background
		prev = do_something(img, prev)
		print("Time : %.2f"%(time.time() - start))
		print("---------------------------")
		conn.close()

print("Anomaly detected: Offroad crash!")
os.system("pause")