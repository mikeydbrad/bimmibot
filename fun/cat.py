from discord.ext import commands

import json
import requests

class CatCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(
    brief='Shows a random cat image or gif',
    help='Uses the https://api.thecatapi.com to supply you a cat to make you feel better :)'
  )
  async def cat(self, ctx):
    json_file = open("config.json")
    config = json.load(json_file)
    json_file.close()

    url = 'https://api.thecatapi.com/v1/images/search'
    url = url + '?api_key=' + config['apiKeys']['catapi']

    for i in requests.get(url).json():
      result = i["url"]

    await ctx.send(result)

async def setup(bot):
  await bot.add_cog(CatCog(bot))