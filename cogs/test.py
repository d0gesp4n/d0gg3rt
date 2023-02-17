import asyncio, discord, json, os, platform, random, sqlite3, sys

from .helpers import ADMIN_ROLES, permission_check

# discord imports
from discord import Interaction
from discord import slash_command, Option
from discord.ext import tasks, commands
from discord.ext.commands import Bot
from discord.ext.commands import Context

#ADMIN_ROLES = ['sys admins', 'Overlord']


  #if ADMIN_ROLES in 
  #return user_roles

class Test(commands.Cog): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

  def __init__(self, bot): # this is a special method that is called when the cog is loaded
    self.bot = bot

    #@commands.command() # creates a prefixed command
    #async def hello(self, ctx): # all methods now must have both self and ctx parameters
        #await ctx.send('Hello!')
  
  @slash_command(name='testfunc')
  async def testfunc(self, ctx):
    perm_check = permission_check(self, ctx, ctx.author, ADMIN_ROLES)
    await ctx.respond(f'{perm_check}')

     

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Test(bot)) # add the cog to the bot