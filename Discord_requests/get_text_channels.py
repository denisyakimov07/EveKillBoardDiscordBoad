from discord_client import client


async def get_text_channels(guild_id):
    server_guid = client.get_guild(guild_id)
    return [{TextChannel.id: TextChannel.name} for TextChannel in server_guid.text_channels]




