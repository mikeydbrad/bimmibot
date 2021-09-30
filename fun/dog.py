from discord.ext import commands

import json
import requests

@commands.command()
async def dog(ctx):
  json_file = open("config.json")
  config = json.load(json_file)
  json_file.close()

  url = 'https://api.thedogapi.com/v1/images/search'
  url = url + '?api_key=' + config['apiKeys']['dogapi']

  for i in requests.get(url).json():
    result = i["url"]

  await ctx.send(result)

def setup(bot):
  bot.add_command(dog)