import discord
import uuid
from discord.ext import commands

from DB.create_session_url import create_new_session

from config import ADMIN_ROLE

client = commands.Bot()
from Discord_requests.get_text_channels import get_text_channels
@client.slash_command(name="get_admin", guild_ids=[786028610653651004])
async def get_credentials(ctx: discord.commands.context.ApplicationContext):
    if ADMIN_ROLE in [role_name.name for role_name in ctx.user.roles]:
        url_token = uuid.uuid4().hex
        create_new_session(ctx.guild, url_token)
        await ctx.user.send(f"https://botadmin.denisdns.com/?s={ctx.guild.id}&t={url_token}")
        await ctx.send('New URL generated')
    else:
        await ctx.user.send(f"User has no role {ADMIN_ROLE}")

    await get_text_channels(786028610653651004)










