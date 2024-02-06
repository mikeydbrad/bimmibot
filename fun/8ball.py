from discord.ext import commands
import random

class EightBallCog(commands.Cog):
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

async def setup(bot):
  await bot.add_cog(EightBallCog(bot))