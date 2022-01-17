import time
import asyncio
import struct
import cv2 as cv
import numpy as np

import input

target_ip = "127.0.0.1"
port = 6666

async def tcp_echo_client():
	reader, writer = await asyncio.open_connection(target_ip, port)

	img = input.get_next()
	shape = img.shape
	print(shape)

	writer.write(struct.pack("<L", shape[0]))
	await writer.drain()
	await reader.read(2)

	writer.write(struct.pack("<L", shape[1]))
	await writer.drain()
	await reader.read(2)

	string_img = img.astype(np.uint8, order="C").tobytes()
	size = struct.pack('<L', len(string_img))
	writer.write(size)
	await writer.drain()
	await reader.read(2)

	writer.write(string_img)
	await writer.drain()

	print("Close the connection")
	writer.close()
	await writer.wait_closed()

asyncio.run(tcp_echo_client())