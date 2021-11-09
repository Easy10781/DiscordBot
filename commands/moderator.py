import discord
from discord.ext import commands

import utils

from localization.messages import *

__all__ = ['ban', 'kick', 'mute']

bot = utils.get_client()

guild: discord.Guild = bot.get_guild(907498568510738482)
roles: list[discord.Role] = [discord.utils.get(guild.roles, id=907499800285573161)]
mod_role: discord.Role = discord.utils.get(guild.roles, id=907499800285573161)
mute_role: discord.Role = discord.utils.get(guild.roles, id=907499702822510602)


@bot.command()
async def ban(ctx: commands.Context, username, reason):
    if not utils.is_allowed(ctx, roles):
        await ctx.channel.send(text_for_not_allowed_using)
        return
    member = discord.utils.get(guild.members, name=username)
    if not member:
        await ctx.channel.send(text_for_not_found.render(USERNAME=username))
        return
    elif mod_role in member.roles:
        await ctx.channel.send(text_for_mod_ban)
    await ctx.channel.send(text_for_ban.render(USERNAME=username, MOD_USERNAME=ctx.author.name, REASON=reason))
    await member.ban()


@bot.command()
async def kick(ctx: commands.Context, username, reason):
    if not utils.is_allowed(ctx, roles):
        await ctx.channel.send(text_for_not_allowed_using)
        return
    member: discord.Member = discord.utils.get(guild.members, name=username)
    if not member:
        await ctx.channel.send(text_for_not_found.render(USERNAME=username))
        return None
    elif mod_role in member.roles:
        await ctx.channel.send(text_for_mod_kick)
    await ctx.channel.send(text_for_kick.render(USERNAME=username, MOD_USERNAME=ctx.author.name, REASON=reason))
    await member.kick()


@bot.command()
async def mute(ctx: commands.Context, username, reason):
    if not utils.is_allowed(ctx, roles):
        await ctx.channel.send(text_for_not_allowed_using)
        return
    member: discord.Member = discord.utils.get(guild.members, name=username)
    if not member:
        await ctx.channel.send(text_for_not_found.render(USERNAME=username))
        return None
    elif mod_role in member.roles:
        await ctx.channel.send(text_for_mod_mute)
    await ctx.channel.send(text_for_mute.render(USERNAME=username, MOD_USERNAME=ctx.author.name, REASON=reason))
    await member.add_roles(mute_role)


@bot.command()
async def unmute(ctx: commands.Context, username, *reason):
    if not reason:
        reason = "Не описана"
    else:
        reason = ' '.join(reason)
    if not utils.is_allowed(ctx, roles):
        await ctx.channel.send(text_for_not_allowed_using)
        return
    member: discord.Member = discord.utils.get(guild.members, name=username)
    if not member:
        await ctx.channel.send(text_for_not_found.render(USERNAME=username))
        return
    elif mute_role not in member.roles:
        await ctx.channel.send(text_for_not_muted_unmuting)
        return
    await ctx.channel.send(text_for_unmute.render(USERNAME=username, MOD_USERNAME=ctx.author.name, REASON=reason))
    await member.remove_roles(mute_role)
