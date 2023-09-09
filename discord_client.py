import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True


client = discord.Client(intents=intents)
