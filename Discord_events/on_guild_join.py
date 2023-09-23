from config import ADMIN_ROLE
from discord_client import client
from loguru import logger
@client.event
async def on_guild_join(guild):
    if ADMIN_ROLE in [role_name.name for role_name in guild.fetch_roles()]:
        logger.info(f"Role {ADMIN_ROLE} exist")
    else:
        await guild.create_role(name=ADMIN_ROLE)
        logger.info(f"Role {ADMIN_ROLE} created")


