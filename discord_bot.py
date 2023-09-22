from discord_client import client
from environment import get_env
from Discord_events import *


def start_discord_bot():
    client.run(get_env().DISCORD_BOT_TOKEN)


async def send_message():
    channel = client.get_channel(786028610653651007)
    await channel.send(f'Test')

