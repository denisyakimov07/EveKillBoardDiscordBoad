# import threading
# from flask import Flask
from quart import Quart
from discord_bot import send_message
from discord_client import client
#
# app = Flask(__name__)
#
# @app.route('/massage', methods=['POST'])
# async def discord_massage_webhook():
#     print('test')
#     channel = client.get_channel(786028610653651007)
#     await send_message()
#     return {'code': 200}
#
#
#
# def start_server():
#     app.run()
#
#
# def start_server_thread():
#     api_server_thread = threading.Thread(target=start_server, args=())
#     api_server_thread.start()


app = Quart(__name__)

@app.route('/massage', methods=['POST'])
async def discord_massage_webhook():
    await send_message()
    return {'code': 200}
