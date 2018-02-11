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

import commands as c

core = {
    "token": "", # Your Bot Token here
    "prefix": "", # Your Bot prefix here
    "bot_owner_id": "", # Your ID here
    "bot_owner_name": "", # Your Name here
    "signature_color": 0x000080,
    "error_color": 0xFF0000
}

mes = {
    "help_text": "The bot prefix for this bot is {0}. To get help on specific bot commands, use {1}help <command>",
    "help_header": "{} Help",
    "spec_help_header": "Help for {0}{1}",
    "help_error": "The command '{}' doesn't exist",
    "invalid_arguments": ":x: Invalid Arguments provided. Try something like {}",
    "wrong_perms": ":x: You cannot do this",
    "self_wrong_perms": ":x: I do not have the permissions to do this. I need {}",
    "wiki_not_found": "The page ***{}*** doesn't exist",
    "8ball_answers": ("Yes", "No", "Maybe", "I don't know"),
    "info": "Bot based on jcbsbot by jcb#1317 https://github.com/jcb1317/jcbsbot"
}

cmds = {
    "help": (
        "Basic Help command. Use {0}help to get an overview of all commands and {0}help <command> to get help on a specific command",
        c.help_command),
    "wiki": ("Get information from a wikipedia page", c.wiki),
    "status": ("Change the bot's status (Bot Owner only)", c.setstatus),
    "clear": ("Clear the last n message of the channel", c.purge),
    "8ball": ("Get the answer to your questions", c.eightball),
    "info": ("Get information about this bot", c.bot_info)
}

res = {"core": core, "messages": mes, "commands": cmds}
