import asyncio, discord, json, os, platform, random, sqlite3, sys
from dotenv import load_dotenv
from pathlib import Path
from keep_alive import keep_alive

# discord imports
from discord import Interaction
from discord.ext import tasks, commands
from discord.ext.commands import Bot
from discord.ext.commands import Context


'''
access env variables such as TOKEN, PERMISSIONS, APP ID, or OWNERS
'''

load_dotenv() # load all the variables from the env file

intents = discord.Intents.all()
intents.members = True
intents.messages = True

'''
debug guilds needs to be added in place of line 12 IF slash commands need to be limited to certain groups
This is a good options for testing new/beta commands.
'''
#bot = discord.Bot(debug_guilds=[...])
bot = discord.Bot()

# TODO why do we need a DB?
#def init_db():
    #with closing(connect_db()) as db:
        #with open("database/schema.sql", "r") as f:
            #db.cursor().executescript(f.read())
        #db.commit()


def connect_db():
    return sqlite3.connect("database/database.db")

# TODO remove config references from cogs
#bot.config = config 
bot.db = connect_db()


@bot.event
async def on_ready():
    """
    The code in this even is executed when the bot is ready
    """
    print("-------------------")
    print(f"Logged in as {bot.user.name}")
    print(f"discord.py API version: {discord.__version__}")
    print(f"Python version: {platform.python_version()}")
    print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    print("-------------------")
    #await bot.change_presence(activity=discord.Game('With the API'))
    status_task.start() #thot it needed to be called

@tasks.loop(minutes=10.0)
async def status_task():
    """
    Setup the game status task of the bot
    """
    statuses = ["ball", "with himself", 'doge-porn.com', 'with flee shampoo', 'catch the tail', 'shit on the neighbors lawn']
    await bot.wait_until_ready()
    await bot.change_presence(activity=discord.Game(random.choice(statuses)))

#@bot.slash_command(name = "hello", description = "Say hello to the bot")
#async def hello(ctx):
    #await ctx.respond("Hey!")

# TODO what is this?
@bot.event
async def on_command_completion(context: Context) -> None:
    """
    The code in this event is executed every time a normal command has been *successfully* executed
    :param context: The context of the command that has been executed.
    """
    full_command_name = context.command.qualified_name
    split = full_command_name.split(" ")
    executed_command = str(split[0])
    if context.guild is not None:
        print(
            f"Executed {executed_command} command in {context.guild.name} (ID: {context.guild.id}) by {context.author} (ID: {context.author.id})")
    else:
        print(f"Executed {executed_command} command by {context.author} (ID: {context.author.id}) in DMs")

async def load_cogs() -> None:
    """
    The code in this function is executed whenever the bot will start.
    """
    for file in os.listdir(f"./cogs"):
        if file.endswith(".py") and file != "helpers.py":
            extension = file[:-3]
            #extension = os.path.splitext(file)[0]
            try:
                bot.load_extension(f"cogs.{extension}")
                print(f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension {extension}\n{exception}")

#TODO logging when anyone plays a game, start and stop.
#init_db()
asyncio.run(load_cogs())
# keep_alive() # prevents shutdown while running in app services
bot.run(os.getenv('TOKEN')) # run the bot with the token
