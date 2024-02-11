from discord.ext import commands

import random
import json
import requests

class Fun(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(aliases=["8ball"])
  async def eightball(self, ctx):
    options = [
      # affirmative responses
      'It is certain.',
      'It is decidedly so.',
      'Without a doubt.',
      'Yes - definitely.',
      'You may rely on it.',
      'As I see it, yes.',
      'Most likely.',
      'Outlook good.',
      'Yes.',
      'Signs point to yes.',
      # non-committal responses
      'Reply hazy, try again.',
      'Ask again later.',
      'Better not tell you now.',
      'Cannot predict now.',
      'Concentrate and ask again.',
      # negative responses
      'Don\'t count on it.',
      'My reply is no.',
      'My sources say no.',
      'Outlook not so good.',
      'Very doubtful.',
    ]
    choice = random.choice(options)
    await ctx.send(choice)

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

  @commands.command(
    brief='Shows a random dog image or gif',
    help='Uses the https://api.thedogapi.com to supply you a dog to make you feel better :)'
  )
  async def dog(self, ctx):
    json_file = open("config.json")
    config = json.load(json_file)
    json_file.close()

    url = 'https://api.thedogapi.com/v1/images/search'
    url = url + '?api_key=' + config['apiKeys']['dogapi']

    for i in requests.get(url).json():
      result = i["url"]

    await ctx.send(result)

async def setup(bot):
  await bot.add_cog(Fun(bot))