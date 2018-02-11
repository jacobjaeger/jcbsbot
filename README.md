# jcbsbot
## About
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

   * In `commands.py`, add the command coroutine. It should take two parameters, `client` and `message`
   * In `dump.py`, in the `cmds` dictionary, add an entry with the command name (without prefix) as the key and a tuple with the description for the help command and the coroutine as the value

