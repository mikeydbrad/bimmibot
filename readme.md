run bot with "py bot.py"
# bimmibot - discord.py

https://github.com/mikeydbrad/bimmibot

Utilized [these docs](https://discordpy.readthedocs.io/en/latest/index.html#) as a general 
guide for the basic layout and setup of the bot.

Check the [issues](https://github.com/mikeydbrad/bimmibot/issues) 
labelled `to-do` for things that are in development. Feel free to suggest your own via the `enhancement` label!

Referenced the following:
 - [linuxboi bot.py](https://github.com/TrackRunny/LinuxBoi/blob/master/LinuxBoi.py)
 - [linuxboi example cog file](https://github.com/TrackRunny/LinuxBoi/blob/master/cogs/Fun.py)
 - TODO: reference [this template](https://github.com/MoonlightCapital/discord-py-template) for further improvements
 - [collection of bots](https://github.com/topics/discord-py-bot)

## config.json setup
```json
{
  "prefix": "<prefix>",
  "token": "<your bot token>",
  "ownerID": "<your discord owner id>",
  "apiKeys": {
    "api": "<key>"
  },
  "server": {
    "<gamename>": {
      "<subdirectory1>": "<serverpath>"
    }
  }
}
```

## command template
```python
from discord.ext import commands

@commands.command(
  brief='',
  help=''
)
async def command_name(ctx):
  # code here
  await ctx.send(response)

def setup(bot):
  bot.add_command(command_name)
```

## python modules needed
```
py -3 -m pip install -U discord.py

$ pip install _____
requests
```

# useful links

[Discord.py Documentation](https://discordpy.readthedocs.io/en/latest/index.html#)  
[Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#links)
