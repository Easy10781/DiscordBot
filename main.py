import discord.ext.commands

import utils
from localization.messages import *

client = discord.ext.commands.Bot(command_prefix='.')
utils.init_client(client)

# utils.set_language('eng')


@client.event
async def on_ready():
    print(text_on_ready)
    utils.init_commands()


client.run('ODk0OTIxNzEyNzI5MjE5MTc4.YVxCyw.NG0g3LbE743XQUgfWkO852bt4P8')
