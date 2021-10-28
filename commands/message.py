import discord
from discord.ext import commands

import utils

__all__ = ['print_embed']

bot = utils.get_client()
guild: discord.Guild = bot.get_guild(894404289160691772)
roles: list[discord.Role] = [discord.utils.get(guild.roles, id=894405176604115044)]


@bot.command(name='embed')
async def print_embed(ctx: commands.Context, title, description, r_color, g_color, b_color):
    if not utils.is_allowed(ctx, roles):
        await ctx.channel.send('Только модераторы могут использовать эту команду')
    color = discord.Colour.from_rgb(int(r_color), int(g_color), int(b_color))
    embed = discord.Embed(title=title, description=description, color=color)
    await ctx.channel.send(embed=embed)

