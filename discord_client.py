import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.guilds = True

client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)