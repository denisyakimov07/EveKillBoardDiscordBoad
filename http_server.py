from quart import Quart, request

from Discord_requests.get_text_channels import get_text_channels
from discord_client import client


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

@app.route('/server_text_channels/<int:server_id>', methods=['GET'])
async def server_text_channels(server_id):
    return f"{ await get_text_channels(server_id) }"
