import commands as c

core = {
    "token": "MzczMjUyMTA5NzUzMzg0OTYw.DNQB0Q._uf5eGMo0kKnyzN-XfTZdRsz5Yg",
    "prefix": "j!",
    "bot_owner_id": "351439713770536961",
    "bot_owner_name": "jcb#1317",
    "signature_color": 0x000080,
    "error_color": 0xFF0000
}

mes = {
    "help_text": "The bot prefix for this bot is {0}. To get help on specific bot commands, use {1}help <command>",
    "help_header": "{} Help",
    "spec_help_header": "Help for {0}{1}",
    "help_error": "The command '{}' doesn't exist",
    "invalid_arguments": ":x: Invalid Arguments provided. Try something like {}",
    "wrong_perms": ":x: You cannot do this"
}

cmds = {
    "help": (
        "Basic Help command. Use {0}help to get an overview of all commands and {0}help <command> to get help on a specific command",
        c.help_command),
    "wiki": ("Get information from a wikipedia page", c.wiki),
    "status": ("Change the bot's status (Bot Owner only)", c.setstatus)
}

res = {"core": core, "messages": mes, "commands": cmds}
