from discord.ext import commands

class TriviaCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def trivia(self, ctx):
    await ctx.message.add_reaction('🇦')
    await ctx.message.add_reaction('🇧')
    await ctx.message.add_reaction('🇨')
    await ctx.message.add_reaction('🇩')
    await ctx.message.add_reaction('🇪')
    await ctx.message.add_reaction('🇫')
    await ctx.message.add_reaction('🇬')

async def setup(bot):
  await bot.add_cog(TriviaCog(bot))