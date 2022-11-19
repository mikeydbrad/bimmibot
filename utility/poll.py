from discord.ext import commands
from discord.utils import get

@commands.command(
  brief='Adds reactions for voting yes/no/maybe',
  help='Adds reactions for voting yes/no/maybe'
)
async def poll(ctx, *args):
  # code here
  print(args)
  for x in args:
    print(x)
    emoji = get(ctx.message.guild.emojis, name=x)
    if emoji != None:
      await ctx.message.add_reaction(emoji)
    else:
      await ctx.message.add_reaction('👍')
      await ctx.message.add_reaction('👎')
      await ctx.message.add_reaction('🤷')

  print(args)
  for x in args:
    print(x)
    await ctx.message.add_reaction(x)
#    else:
#      await ctx.message.add_reaction('👍')
#      await ctx.message.add_reaction('👎')
#      await ctx.message.add_reaction('🤷')

def setup(bot):
  bot.add_command(poll)