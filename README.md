# jcbsbot
## About
### ATTENTION: This Version of the Bot is deprecated! The new version is no longer open source! It will soon be hosted 24/7!
This Bot is a little project by me (jcb#1317). It is a highly costumizable Discord Bot. You can easily add your own commands.
## Setup
### Dependencies
Python 3.5+ and the corresponding `discord.py` version

### Initial Setup

   * Go to dump.py
   * On line 21, in the core dict, set `"token"` to your bot token
   * On line 22, set `"prefix"` to what you want to use as your bot prefix
   * On line 23, set `"bot_owner_id"` to your own ID
   * On line 24, set `"bot_owner_name"` to your own discord name

### Adding Commands

   * In `commands.py`, add the command coroutine. It should take three parameters, `client`, `message` and `basic_cmd`
   * In `dump.py`, in the `cmds` dictionary, add an entry with the command name (without prefix) as the key and a tuple with the description for the help command and the coroutine as the value

### Example:

If your prefix was `!` and you wanted to add a command that replies to `!ping` with `Pong`, you would have to add a coroutine in `commands.py` that looked like this: `async def ping(client, message, basic_cmd): await client.send_message(message.channel, "Pong")`. Then, you would have to add an entry in the `cmds` dictionary with the key `ping` and the value `("Replies with pong", c.ping)`. And now you're all set
