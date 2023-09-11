import asyncio
from  Discord_events import *
from discord_client import client
from environment import get_env
from http_server import app


@app.before_serving
async def before_serving():
    loop = asyncio.get_event_loop()
    await client.login(get_env().DISCORD_BOT_TOKEN)
    loop.create_task(client.connect())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


