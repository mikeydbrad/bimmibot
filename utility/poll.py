from discord.ext import commands

@commands.command()
async def poll(ctx):
  # code here
  await ctx.message.add_reaction('👍')
  await ctx.message.add_reaction('👎')
  await ctx.message.add_reaction('🤷')

def setup(bot):
  bot.add_command(poll)