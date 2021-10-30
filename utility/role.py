from discord.ext import commands

@commands.command(
  brief='',
  help=''
)
async def role(ctx):
  # code here
  await ctx.send(response)

def setup(bot):
  bot.add_command(role)