import discord
import os

from discord.ext import commands

bot = discord.Client()
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

bot.load_extension('fun.8ball')

@bot.event
async def on_message(message):
  await bot.process_commands(message)
  if message.author == bot.user:
    return # enures we don't respond to self

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

  #if message.content.startswirth(bot.command_prefix + '8ball'):
    
        
@bot.event
async def on_error(event, *args, **kwargs):
  with open('err.log', 'a') as f:
    if event == 'on_message':
      f.write(f'Unhandled message: {args[0]}\n')
    else:
      raise


# loading .env file for the TOKEN key
from dotenv import load_dotenv
load_dotenv()

bot.run(os.getenv('TOKEN'))