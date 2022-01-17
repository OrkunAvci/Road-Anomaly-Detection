import socket
import pickle
import process_image as pi
import time
import os
import asyncio

self_ip = "127.0.0.1"
port = 6666

async def handle_echo(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"Connection from {addr!r}")
    message = input()
    data = message.encode()

    print(f"Send: {message!r}")
    writer.write(data)
    await writer.drain()

    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    print(f"Received {message!r} from {addr!r}")

    print("Close the connection")
    writer.close()

async def main():
    server = await asyncio.start_server(handle_echo, self_ip, port)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()

asyncio.run(main())