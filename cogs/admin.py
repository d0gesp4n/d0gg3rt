import asyncio, discord, json, os, platform, random, sqlite3, sys

from .helpers import ADMIN_ROLES, permission_check

# discord imports
from discord import Interaction
from discord import slash_command, Option
from discord.ext import tasks, commands
from discord.ext.commands import Bot
from discord.ext.commands import Context

class Admin(commands.Cog): # create a class for our cog that inherits from commands.Cog
# this class is used to create a cog, which is a module that can be added to the bot
  def __init__(self, bot): # this is a special method that is called when the cog is loaded
    self.bot = bot
  
  @slash_command(name='reload', hidden=True)
  async def reload(self, ctx, module : str):
    """Reloads a module."""
    user_perms = permission_check(self, ctx, ctx.author, ADMIN_ROLES)
    if user_perms == True:
      try:
        self.bot.unload_extension(module)
        self.bot.load_extension(module)
      except Exception as e:
        await ctx.respond('\N{PISTOL}')
        await ctx.respond('{}: {}'.format(type(e).__name__, e))
      else:
        await ctx.respond('\N{OK HAND SIGN}' + ' {} module reloaded'.format(module.split('.')[1]))
    else:
      await ctx.respond(f'{ctx.author} does not have permissions to run this command')
  
  @slash_command(name='load', hidden=True)
  async def load(self, ctx, module : str):
    """Loads a new module"""
    user_perms = permission_check(self, ctx, ctx.author, ADMIN_ROLES)
    if user_perms == True:
      try:
        self.bot.load_extension(module)
      except Exception as e:
        await ctx.respond('\N{PISTOL}')
        await ctx.respond('{}: {}'.format(type(e).__name__, e))
      else:
        await ctx.respond('\N{OK HAND SIGN}' + ' {} module loaded'.format(module.split('.')[1]))
    else:
      await ctx.respond(f'{ctx.author} does not have permissions to run this command')
      
  @slash_command(name='remodvemodule', hidden=True)
  async def removemodule(self, ctx, module : str):
    """Unloads an active module"""
    user_perms = permission_check(self, ctx, ctx.author, ADMIN_ROLES)
    if user_perms == True:
      try:
        self.bot.unload_extension(module)
      except Exception as e:
        await ctx.respond('\N{PISTOL}')
        await ctx.respond('{}: {}'.format(type(e).__name__, e))      
      else:
        await ctx.respond('\N{OK HAND SIGN}' + ' {} haz bean unloaded'.format(module.split('.')[1]))
    else:
      await ctx.respond(f'{ctx.author} does not have permissions to run this command')
  
  @slash_command(name='listuserroles', hidden=True)
  async def listuserroles(self, ctx, member: discord.Member):
    """List Roles for a specified user"""
    #author = member
    user_perms = permission_check(self, ctx, ctx.author, ADMIN_ROLES)
    if user_perms == True:
      user_roles = ", ".join([str(r.name) for r in member.roles])
      await ctx.respond(f'{member} : {user_roles}')
    else:
      await ctx.respond(f'{ctx.author} does not have permissions to run this command')
  
  @slash_command(name='listroles')  
  async def listroles(self, ctx):
    """List roles and IDs for Server"""
    user_perms = permission_check(self, ctx, ctx.author, ADMIN_ROLES)
    if user_perms == True:
      server_roles = []
      for r in ctx.guild.roles:
        current_role = [str(r.name), str(r.id)]
        server_roles.append(current_role)
      
      await ctx.respond('{}'.format(server_roles))
    else:
      await ctx.respond(f'{ctx.author} does not have permissions to run this command')
      
      
def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Admin(bot)) # add the cog to the bot