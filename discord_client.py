import discord
import asyncio

from environment import get_env


intents = discord.Intents.default()
intents.members = True
intents.guilds = True

client = discord.Client(intents=intents)