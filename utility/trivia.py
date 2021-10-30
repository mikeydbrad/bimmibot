from discord.ext import commands

@commands.command(
  brief='Adds reactions for voting yes/no/maybe',
  help='Adds reactions for voting yes/no/maybe'
)
async def trivia(ctx):
  # code here
  await ctx.message.add_reaction('🇦')
  await ctx.message.add_reaction('🇧')
  await ctx.message.add_reaction('🇨')
  await ctx.message.add_reaction('🇩')
  await ctx.message.add_reaction('🇪')
  await ctx.message.add_reaction('🇫')
  await ctx.message.add_reaction('🇬')

def setup(bot):
  bot.add_command(trivia)