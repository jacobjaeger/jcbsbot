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

import asyncio
import discord
import dump
import commands

client = discord.Client()
resources = dump.res
prefix = resources["core"]["prefix"]
token = resources["core"]["token"]
cmds = resources["commands"]

@client.event
async def on_ready():
    print("Bot is ready as {0} ({1})".format((client.user.name + "#" + client.user.discriminator), client.user.id))
    await commands.initdump(resources)

@client.event
async def on_message(message):
    global cmds
    global prefix
    c = message.content
    try:
        basic_cmd = c.split(" ")[0][len(prefix):]
    except:
        basic_cmd = None
    if c.startswith(prefix) and basic_cmd in list(cmds.keys()):
        await (cmds[basic_cmd][1])(client, message, basic_cmd)


client.run(token)
