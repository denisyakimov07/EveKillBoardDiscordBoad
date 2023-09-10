from discord_client import client

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    channel = client.get_channel(786028610653651007)
    await channel.send(f'Test')
    print(type(channel))