import asyncio, discord, json, os, platform, random, sqlite3, sys

# discord imports
from discord import Interaction
from discord import slash_command, Option
from discord.ext import tasks, commands
from discord.ext.commands import Bot
from discord.ext.commands import Context

class Greetings(commands.Cog): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    #@commands.command() # creates a prefixed command
    #async def hello(self, ctx): # all methods now must have both self and ctx parameters
        #await ctx.send('Hello!')

    @slash_command(name = "hello", description = "Say hello to the bot")
    async def hello(self, ctx):
        await ctx.respond("Hey!")
    
    @slash_command(name = "goodbye", description = "Say goodbye to the bot") # we can also add application commands
    async def goodbye(self, ctx):
        await ctx.respond('Goodbye {}!'.format(ctx.author))

    @slash_command(name = 'greet', description = "Greet a user")
    async def greet(self, ctx, member: discord.Member):
        await ctx.respond(f'{ctx.author.mention} says hello to {member.mention}!')

    @commands.Cog.listener() # we can add event listeners to our cog
    async def on_member_join(self, member): # this is called when a member joins the server
    # you must enable the proper intents
    # to access this event.
    # See the Popular-Topics/Intents page for more info
        await member.send('Welcome to n3rdsh!t!')

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Greetings(bot)) # add the cog to the bot