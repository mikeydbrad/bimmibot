import discord
import json

from discord.ext import commands

# find the .json, store the contents, close it
json_file = open("config.json")
config = json.load(json_file)
json_file.close()

intents = discord.Intents.default()
intents.message_content = True

# set prefix to whats in the config.json file
# set intents
bot = commands.Bot(
    command_prefix=(config['prefix']),
    intents=intents
)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    
    await bot.load_extension('fun.8ball')
    await bot.load_extension('fun.cat')
    await bot.load_extension('fun.dog')
    # await bot.load_extension('fun.insult')
    # await bot.load_extension('fun.roll')

    await bot.load_extension('utility.poll')
    # await bot.load_extension('utility.role')
    await bot.load_extension('utility.trivia')

# @bot.event
# async def on_error(event, *args, **kwargs):
#   with open('error.log', 'a') as f:
#     if event == 'on_message':
#       f.write(f'Unhandled message: {args[0]}\n')
#     else:
#       raise

bot.run(config['token'])