import discord
from discord.ext import commands

import utils

from localization.messages import *
import commands.message as message

__all__ = ['ban', 'kick', 'mute']

bot = utils.get_client()

guild: discord.Guild = bot.get_guild(894404289160691772)
roles: list[discord.Role] = [discord.utils.get(guild.roles, id=894405176604115044)]


@bot.command()
async def ban(ctx: commands.Context, username, reason):
    if not await utils.is_allowed(ctx, roles):
        await ctx.channel.send(text_for_not_allowed_using)
        return
    member = discord.utils.get(guild.members, nick=username)
    if not member:
        await ctx.channel.send(text_for_not_found.render(USERNAME=username))
        return
    await ctx.channel.send(text_for_ban % (ctx.author, username, reason))
    await member.ban()


@bot.command()
async def unban(ctx: commands.Context, username, reason):
    if not await utils.is_allowed(ctx, roles):
        await ctx.channel.send(text_for_not_allowed_using)
        return
    member = discord.utils.get(guild.members, nick=username)
    if not member:
        await ctx.channel.send(text_for_not_found.render(USERNAME=username))
        return None
    await ctx.channel.send(text_for_unban.render(USERNAME=username, MOD_USERNAME=ctx.author.name, REASON=reason))
    await member.unban()


@bot.command()
async def kick(ctx: commands.Context, username, reason):
    if not utils.is_allowed(ctx, roles):
        await ctx.channel.send(text_for_not_allowed_using)
        return
    member: discord.Member = discord.utils.get(guild.members, nick=username)
    mod_role: discord.Role = discord.utils.get(guild.roles, id=894405176604115044)
    if not member:
        await ctx.channel.send(text_for_not_found.render(USERNAME=username))
        return None
    elif mod_role in member.roles:

    await ctx.channel.send(text_for_kick.render(USERNAME=username, MOD_USERNAME=ctx.author.name, REASON=reason))
    await member.kick()


@bot.command()
async def mute(ctx: commands.Context, username, reason):
    if not await utils.is_allowed(ctx, roles):
        await ctx.channel.send(text_for_not_allowed_using)
        return
    member: discord.Member = discord.utils.get(guild.members, nick=username)
    if not member:
        await ctx.channel.send(text_for_not_found.render(USERNAME=username))
        return None
    await ctx.channel.send(text_for_mute.render(USERNAME=username, MOD_USERNAME=ctx.author.name, REASON=reason))
    await member.add_roles(discord.utils.get(guild.roles, id=895116019071340554))


@bot.command()
async def unmute(ctx: commands.Context, username, reason):
    if not await utils.is_allowed(ctx, roles):
        await ctx.channel.send(text_for_not_allowed_using)
        return
    member: discord.Member = discord.utils.get(guild.members, nick=username)
    if not member:
        await ctx.channel.send(text_for_not_found.render(USERNAME=username))
        return None
    await ctx.channel.send(text_for_unban.render(USERNAME=username, MOD_USERNAME=ctx.author.name, REASON=reason))
    await member.remove_roles(discord.utils.get(guild.roles, id=895116019071340554))
