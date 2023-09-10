import asyncio

from quart import Quart, request
from  Discord_events import *
from discord_client import client
from environment import get_env

app = Quart(__name__)

@app.route('/webhook', methods=['POST'])
async def myJSON():
    channel = client.get_channel(786028610653651007)
    if request.is_json:
        data = await request.get_json()
        print(data)
        await channel.send(data.get('zkb').get('url'))
        return 'json received', 200
    else:
        return 'Failed - Not a JSON', 400