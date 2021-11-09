import sys

import discord.ext.commands

import utils
from localization.messages import *
import traceback


intents = discord.Intents(messages=True, guilds=True, members=True)
client = discord.ext.commands.Bot(command_prefix='.', intents=intents)
utils.init_client(client)

try:
    asd
except:
    print('asd')
    traceback.print_exc()

@client.event
async def on_ready():
    print(text_on_ready)
    utils.init_commands()


client.run("ODk0OTIxNzEyNzI5MjE5MTc4.YVxCyw.zfNGwIdMo6h0LIU-p9_eU-swU_E")
