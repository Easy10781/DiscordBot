import discord.ext.commands

import utils
from localization.messages import *

client = discord.ext.commands.Bot(command_prefix='.')
utils.init_client(client)


@client.event
async def on_ready():
    print(text_on_ready)
    utils.init_commands()


# client.run(BOT_TOKEN)
#