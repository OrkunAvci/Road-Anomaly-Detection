import process_image as pi
import time
import asyncio
import logging
import struct
import numpy
from skimage import io

self_ip = "0.0.0.0"
port = 6666

async def handle_echo(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"Connection from {addr!r} at {time.ctime(time.time())}")

    data = await reader.read(4)
    print("First:", data)
    first = struct.unpack("<L", data)[0]
    print(f"Received {first} from {addr!r} at {time.time()}")
    writer.write(b"ok")

    data = await reader.read(4)
    print("Second:", data)
    second = struct.unpack("<L", data)[0]
    print(f"Received {second} from {addr!r} at {time.time()}")
    writer.write(b"ok")

    shape = (first, second)
    print(f"Received {shape} from {addr!r} at {time.time()}")

    data = await reader.read(128)
    size = struct.unpack("<L", data)[0]
    print(f"Received {size} from {addr!r} at {time.time()}")
    writer.write(b"ok")

    img_size = size
    read = await reader.read(size)
    while size:
        data += read
        size -= len(read)
        read = await reader.read(size)
    print(len(data))
    img = numpy.frombuffer(data, dtype='uint8', count = img_size)
    img = img.reshape(shape, order="C")
    print(img)
    io.imshow(img)
    io.show()
    print("Close the connection")
    writer.close()

async def main():
    server = await asyncio.start_server(handle_echo, self_ip, port)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()

logging.basicConfig(level=logging.DEBUG)
asyncio.run(main(), debug = True)