import discord

from discord_client import client

@client.tree.command(name='Get admin credentials')
async def get_admin_credentials(interaction: discord.Interaction):
    await interaction.response.send_message('Test74879878987')