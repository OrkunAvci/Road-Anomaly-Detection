import time
import asyncio
import struct
import cv2 as cv
import numpy as np

import input

target_ip = "127.0.0.1"
port = 8888
ID = 1

async def get_int(reader, writer) -> int:
	data = await reader.read(4)
	integer = struct.unpack("<L", data)[0]
	writer.write(b"ok")
	await writer.drain()
	return integer

async def send_int(reader, writer, value: int):
	writer.write(struct.pack("<L", value))
	await writer.drain()
	await reader.read(2)

async def send_img(reader, writer):
	img = input.get_next()
	shape = img.shape

	await send_int(reader, writer, shape[0])
	await send_int(reader, writer, shape[1])

	string_img = img.astype(np.uint8, order = "C").tobytes()
	print(f"Sending image. Size: {len(string_img)} bytes.")
	writer.write(string_img)
	await writer.drain()
	await reader.read(2)

async def main_handler():
	reader, writer = await asyncio.open_connection(target_ip, port)

	while True:
		option = await get_int(reader, writer)
		print("Option: ", option)
		if option == 0:     #   Exit signal
			break
		elif option == 1 :  #   New image signal
			await send_img(reader, writer)
		elif option == 2 :  #   Clear error signal
			print("Kill the LED.")
		elif option == 3 :  #   Error signal
			print("Some anomaly detected")
		# ...

	print("Close the connection")
	writer.close()
	await writer.wait_closed()

if __name__ == "__main__":
	asyncio.run(main_handler())