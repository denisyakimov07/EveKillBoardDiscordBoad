from discord_client import client
from environment import get_env

def start_discord_bot():
    client.run(get_env().DISCORD_BOT_TOKEN)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    channel = client.get_channel(786028610653651007)
    # await channel.send(f'Test')
    print(type(channel))

async def send_message():
    channel = client.get_channel(786028610653651007)
    await channel.send(f'Test')
