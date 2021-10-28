import discord.ext.commands

from localization.models import Message

__all__ = ['init_client', 'init_commands', 'get_client', 'is_allowed', 'new_message']


# class for data
class _Data:
    client: discord.ext.commands.Bot
    messages: list[Message] = []


# Initializing class _Data
_data = _Data()


def init_client(client):
    """
    Saves bot into a class _Data.
    To get bot call utils.get_client func

    :param client:
    """

    if not isinstance(client, discord.ext.commands.Bot):
        raise TypeError('Expected type Bot, got %s' % type(client).__name__)
    _data.client = client


def init_commands():
    """
    Includes commands
    """

    import commands
    del commands


def set_language(lang):
    """
    Sets a localization language

    :param lang:
    :return:
    """
    for _lang in _data.messages:
        _lang.default_lang = lang


def get_client():
    """
    Gets client from class _Data.
    If client not found in class _Data
    this function returns None

    :return Bot | None:
    """
    return _data.client


def is_allowed(ctx: discord.ext.commands.Context, roles: list[discord.Role]):
    """
    Checks if the command is allowed for the given roles

    :param ctx:
    :param roles:
    """

    role = None
    for i in roles:
        role = discord.utils.get(ctx.author.roles, id=i.id)
    if not role:
        return False
    else:
        return True


def new_message(msg) -> Message:
    """
    Creates a new message object and saves into a class _Data

    :param msg:
    :returns Message:
    """
    _msg = Message(msg)
    _data.messages.append(_msg)

    return _msg
#