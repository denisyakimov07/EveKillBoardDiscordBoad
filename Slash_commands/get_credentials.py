from discord_client import client


@client.slash_command(name="first_slash", guild_ids=[786028610653651004]) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_slash(ctx):
    await ctx.respond("You executed the slash command!")



