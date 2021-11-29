import discord
import json

from discord.ext import commands

bot = discord.Client()

# find the .json, store the contents, close it
json_file = open("config.json")
config = json.load(json_file)
json_file.close()

# set prefix to whats in the config.json file
bot = commands.Bot(command_prefix=config['prefix'])

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

# load each invidivual command
bot.load_extension('fun.8ball')
bot.load_extension('fun.cat')
bot.load_extension('fun.dog')
bot.load_extension('utility.poll')
bot.load_extension('utility.trivia')
bot.load_extension('utility.role')

# check if any commands apply
@bot.event
async def on_message(message):
  # TODO add a check if the message starts with commandprefix
  await bot.process_commands(message)

@bot.event
async def on_error(event, *args, **kwargs):
  with open('error.log', 'a') as f:
    if event == 'on_message':
      f.write(f'Unhandled message: {args[0]}\n')
    else:
      raise

bot.run(config['token'])