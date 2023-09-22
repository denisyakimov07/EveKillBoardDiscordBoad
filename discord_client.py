import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

client = commands.Bot()

@client.slash_command(name="get_admin", guild_ids=[786028610653651004]) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
@commands.has_any_role('user role', 'Moderators', 492212595072434186)
async def get_credentials(ctx: discord.commands.context.ApplicationContext):
    await ctx.user.send("You executed the slash command!")











