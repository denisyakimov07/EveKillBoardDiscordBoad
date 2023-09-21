import discord

from discord_client import client, tree


@tree.command(name='Eve bot')
async def get_admin_credentials(interaction: discord.Interaction):
    await interaction.response.send_message('Test74879878987')


@tree.command(name="commandname", description="My first application Command", guild=discord.Object(id=786028610653651004))
async def first_command(interaction):
    await interaction.response.send_message("Hello!")