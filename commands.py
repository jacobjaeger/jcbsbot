"""
Copyright (C) 2018  jcb#1317
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import discord
import asyncio
import async_timeout
import wikipedia


async def initdump(res):
    global resources
    resources = res
    global prefix
    prefix = resources["core"]["prefix"]
    global colors
    colors = (resources["core"]["signature_color"], resources["core"]["error_color"])


async def send(client, channel, embed):
    try:
        await client.send_message(channel, embed=embed)
    except discord.errors.Forbidden:
        pass


async def help_command(client, message):
    split = message.content.split(" ")
    if len(split) == 1:
        helplist = ", ".join(list(resources["commands"].keys()))
        helplist = prefix + helplist
        em = discord.Embed(title=resources["messages"]["help_text"].format(prefix, prefix), description=helplist,
                           color=colors[0])
        em.set_author(name=resources["messages"]["help_header"].format(client.user.name),
                      icon_url=client.user.avatar_url)
    elif len(split) == 2:
        spec_header = resources["messages"]["spec_help_header"].format(prefix, split[1])
        try:
            em = discord.Embed(title=spec_header, description=resources["commands"][split[1]][0].format(prefix),
                               color=colors[0])
        except KeyError:
            em = discord.Embed(title=spec_header,
                               description=resources["messages"]["help_error"].format(prefix + split[1]),
                               color=colors[1])
    else:
        desc = resources["messages"]["invalid_arguments"].format("'" + prefix + "help' or '" + prefix + "help wiki'")
        em = discord.Embed(title="Error", description=desc, color=colors[1])
    await send(client, message.channel, em)


async def wiki(client, message):
    if len(message.content) > len(prefix) + len("wiki") + 1:
        try:
            cur_req = wikipedia.page(message.content[len(prefix) + len("wiki") - 1:])
            content = ""
            if len(cur_req.summary) >= 400:
                content = cur_req.summary[:400] + "..."
            else:
                content = cur_req.summary
            em = discord.Embed(title=cur_req.title, description=content, color=colors[0])
        except wikipedia.exceptions.DisambiguationError as e:
            em = discord.Embed(description=str(e))
    await send(client, message.channel, em)


async def setstatus(client, message):
    if message.author.id == resources["core"]["bot_owner_id"] and len(message.content) > len(prefix) + 7:
        await client.change_presence(game=discord.Game(name=(message.content[9:])))
    else:
        await send(client, message.channel, discord.Embed(title=resources["messages"]["wrong_perms"], color=colors[1]))


async def purge(client, message):
    mc = False
    for i in message.author.roles:
        if i.permissions.manage_channels:
            mc = True
        elif i.permissions.administrator:
            mc = True
    if mc and len(message.content) > len(prefix) + 6:
        try:
            int(message.content[len(prefix) + 6:])
            await client.purge_from(message.channel, limit=int(message.content[len(prefix) + 6:]))
        except discord.errors.Forbidden:
            em = discord.Embed(title=resources["messages"]["self_wrong_perms"].format("'Manage Messages'"),
                               color=colors[1])
            await send(client, message.channel, em)
    elif mc:
        em = discord.Embed(title=resources["messages"]["invalid_arguments"].format("'" + prefix + "clear 50'"), color=colors[1])
        await send(client, message.channel, em)
    elif len(message.content) > len(prefix) + 6:
        await send(client, message.channel, discord.Embed(resources["messages"]["wrong_perms"]))
