import socket
import pickle
import time
import os
import asyncio

import input

target_ip = "127.0.0.1"
port = 6666

async def tcp_echo_client():
    reader, writer = await asyncio.open_connection(target_ip, port)

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    message = data.decode()
    print(f'Send: {message!r}')
    writer.write(data)
    await writer.drain()

    print('Close the connection')
    writer.close()
    await writer.wait_closed()

asyncio.run(tcp_echo_client())