import asyncio
import threading

import websockets

import json
from discord_client import client


async def send_receive_loop():
    print('socket ready')
    uri = 'wss://zkillboard.com/websocket/'  # Replace with the actual WebSocket server URI
    with websockets.connect(uri) as websocket:
        # Send a message to the server
        message = '{"action":"sub","channel":"killstream"}'
        await websocket.send(message)
        # Listen for messages indefinitely
        while True:
            response: str = await websocket.recv()
            print(f"{response}")
            converted = json.loads(response)
            print(converted)
            # channel = client.get_channel(786028610653651007)
            # await channel.send(converted)

def wrap_async_func():
    asyncio.run(send_receive_loop())

_thread = threading.Thread(target=wrap_async_func)
_thread.start()

# def start_websockets_thread():
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     loop.run_until_complete(send_receive_loop())
#     loop.close()



# start_websockets_thread()
