import discord
from discord.ext import commands


client = commands.Bot()

@client.slash_command(name="get_admin", guild_ids=[786028610653651004])

async def get_credentials(ctx: discord.commands.context.ApplicationContext):
    if 'Eve_Killboard' in [role_name.name for role_name in ctx.user.roles]:
        await ctx.user.send("Eve_Killboard")
    else:
        await ctx.user.send("has no role Eve_Killboard")











