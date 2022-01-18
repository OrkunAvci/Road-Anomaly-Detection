import process_image as pi
import time
import asyncio
import logging
import struct
import numpy
from skimage import io

self_ip = "0.0.0.0"
port = 8888

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

async def get_img(reader, writer):
	addr = writer.get_extra_info('peername')

	shape = (await get_int(reader, writer), await get_int(reader, writer))
	print(f"Constructed shape {shape} on {time.ctime(time.time())}")

	size = (shape[0] * shape[1])
	img_size = size
	data = bytearray()
	read = await reader.read(size)
	while size :
		data += read
		size -= len(read)
		read = await reader.read(size)
	writer.write(b"ok")
	await writer.drain()
	print(f"Done reading {len(data)} bytes.")

	flat_img = numpy.frombuffer(data, dtype = 'uint8', count = img_size)
	img = flat_img.reshape(shape, order = "C")
	print(f"Built the image from {addr!r} on {time.ctime(time.time())}")
	return img

async def handle_request(reader, writer):
	addr = writer.get_extra_info('peername')
	print(f"Connection from {addr!r} at {time.ctime(time.time())}")

	option = await get_int(reader, writer)
	print("Option is ", option)
	if option == 1:
		img = await get_img(reader, writer)
	elif option == 2:
		print("Party!")
	#...

	print("Close the connection")
	writer.close()

async def main():
	server = await asyncio.start_server(handle_request, self_ip, port)

	addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
	print(f'Serving on {addrs}')

	async with server:
		await server.serve_forever()

if __name__ == "__main__":
	logging.basicConfig(level = logging.DEBUG)
	asyncio.run(main(), debug = True)