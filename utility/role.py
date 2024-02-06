from discord.ext import commands


# TODO revisit this command - do we still want it/is it relevant
class RoleCog(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  @commands.command(
    brief='',
    help=''
  )
  async def role(self, ctx, user : self.Member, *, role : self.Role):
    if role.position > ctx.author.top_role.position: #if the role is above users top role it sends error
      return await ctx.send('**:x: | That role is above your top role!**') 
    if role in user.roles:
        await user.remove_roles(role) #removes the role if user already has
        await ctx.send(f"Removed {role} from {user.mention}")
    else:
        await user.add_roles(role) #adds role if not already has it
        await ctx.send(f"Added {role} to {user.mention}") 

async def setup(bot):
  await bot.add_cog(RoleCog(bot))