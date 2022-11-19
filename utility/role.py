from discord.ext import commands

@commands.command(
  brief='',
  help=''
)
async def role(ctx, user : self.Member, *, role : self.Role):
  if role.position > ctx.author.top_role.position: #if the role is above users top role it sends error
    return await ctx.send('**:x: | That role is above your top role!**') 
  if role in user.roles:
      await user.remove_roles(role) #removes the role if user already has
      await ctx.send(f"Removed {role} from {user.mention}")
  else:
      await user.add_roles(role) #adds role if not already has it
      await ctx.send(f"Added {role} to {user.mention}") 

def setup(bot):
  bot.add_command(role)