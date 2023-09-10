import discord
import asyncio
from quart import Quart, request
from environment import get_env

app = Quart(__name__)
intents = discord.Intents.default()
intents.members = True
intents.guilds = True

client = discord.Client(intents=intents)

# Setup for Discord bot
@app.before_serving
async def before_serving():
    loop = asyncio.get_event_loop()
    await client.login(get_env().DISCORD_BOT_TOKEN)
    loop.create_task(client.connect())

#Setup for webhook to receive POST and send it to Discord bot
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


if __name__ == '__main__':
    app.run()