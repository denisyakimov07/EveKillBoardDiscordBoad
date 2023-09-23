from config import ADMIN_ROLE
from discord_client import client
from loguru import logger
@client.event
async def on_guild_join(guild):
    roles_list = await guild.fetch_roles()
    if ADMIN_ROLE in [role.name for role in roles_list]:
        logger.info(f"Role {ADMIN_ROLE} exist guild.id {guild.id}")
    else:
        await guild.create_role(name=ADMIN_ROLE)
        logger.info(f"Role {ADMIN_ROLE} created guild.id  {guild.id}")


