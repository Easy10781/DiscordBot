import sys

import discord.ext.commands

import utils
from localization.messages import *
import traceback


intents = discord.Intents(messages=True, guilds=True, members=True)
client = discord.ext.commands.Bot(command_prefix='.', intents=intents)
utils.init_client(client)


@client.event
async def on_ready():
    print(text_on_ready)
    utils.init_commands()


# client.run(YOUR TOKEN)
