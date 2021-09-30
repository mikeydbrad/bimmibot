from discord.ext import commands

@commands.command()
async def ball(ctx):
  await ctx.send("something")

def setup(bot):
  bot.add_command(ball)