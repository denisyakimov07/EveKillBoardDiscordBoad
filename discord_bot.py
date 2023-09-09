from discord_events import *

from discord_client import client
from environment import get_env



def start_discord_bot():
    client.run(get_env().DISCORD_BOT_TOKEN)
