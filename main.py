import threading

from discord_bot import start_discord_bot
from discord_client import client
from http_server import app

# from zboard_websocket import start_websockets_thread



if __name__ == '__main__':
    client.loop.create_task(app.run_task())
    start_discord_bot()


