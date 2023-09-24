from discord_client import client
from loguru import logger


@client.event
async def on_ready():
    try:
        # print(f'We have logged in as {client.user}')
        # channel = client.get_channel(786028610653651007)
        # # await channel.send(f'Test')
        # logger.info(f"{type(channel)}")
        # servers = list(client.guilds)
        # for server in servers:
        #     add_server_config(int(server.id))
        # # await tree.sync(guild=discord.Object(id=786028610653651004))
        print("ready")

    except:
        print('WTF')
