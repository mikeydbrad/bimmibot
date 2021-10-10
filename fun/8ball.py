from discord.ext import commands
import random

@commands.command(
  name='8ball',
  brief='Fate decides your query',
  help='Fate decides your query')
async def eightball(ctx):
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
  await ctx.send(random.choice(options))

def setup(bot):
  bot.add_command(eightball)