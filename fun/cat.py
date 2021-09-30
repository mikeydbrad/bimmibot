from discord.ext import commands

import json
import requests

@commands.command()
async def cat(ctx):
  json_file = open("config.json")
  config = json.load(json_file)
  json_file.close()

  url = 'https://api.thecatapi.com/v1/images/search'
  url = url + '?api_key=' + config['apiKeys']['catapi']

  for i in requests.get(url).json():
    result = i["url"]

  await ctx.send(result)

def setup(bot):
  bot.add_command(cat)