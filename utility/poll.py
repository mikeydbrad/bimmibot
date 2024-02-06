from discord.ext import commands
from discord.utils import get

class PollCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(
    brief='Adds reactions for voting yes/no/maybe',
    help='Adds reactions for voting yes/no/maybe'
  )
  async def poll(self, ctx, *args):
    print(args)
    for x in args:
      # supposed to capture emojis in msg to use as custom reaction emojis
      # TODO doesn't work
      emoji = get(ctx.message.guild.emojis, name=x)
      if emoji != None:
        await ctx.message.add_reaction(emoji)
      else:
        await ctx.message.add_reaction('👍')
        await ctx.message.add_reaction('👎')
        await ctx.message.add_reaction('🤷')

async def setup(bot):
  await bot.add_cog(PollCog(bot))