import asyncio
import discord
import async_timeout
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
        await (cmds[basic_cmd][1])(client, message)


client.run(token)
