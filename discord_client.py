import discord

intents = discord.Intents.default()
intents.members = True
intents.guilds = True

client = discord.Client(intents=intents)