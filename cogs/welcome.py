import asyncio, discord, json, os, platform, random, sqlite3, sys

# discord imports
from discord import Interaction
from discord import slash_command, Option
from discord.ext import tasks, commands
from discord.ext.commands import Bot
from discord.ext.commands import Context

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message_id = 1086103847820349540 # Replace with the ID of the message you want to monitor for reactions
        role_ids = {
            '🎮' : 1097594591655510047, #Gamers
            '🔒' : 1088876423474855956, #ISB
            '🤓' : 1088872151421038673 #n3rd-h3rd3rs
        }

        if payload.message_id == message_id and str(payload.emoji) in role_ids:
            guild = self.bot.get_guild(payload.guild_id)
            member = payload.member or await guild.fetch_member(payload.user_id)
            role_id = role_ids[str(payload.emoji)]
            role = discord.utils.get(guild.roles, id=role_id)
            if role is not None and member is not None:
                await member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        message_id = 1086103847820349540 # Replace with the ID of the message you want to monitor for reactions
        role_ids = {
            '🎮' : 1097594591655510047, #Gamers
            '🔒' : 1088876423474855956, #ISB
            '🤓' : 1088872151421038673 #n3rd-h3rd3rs
        }

        if payload.message_id == message_id and str(payload.emoji) in role_ids:
            guild = self.bot.get_guild(payload.guild_id)
            member = payload.member or await guild.fetch_member(payload.user_id)
            role_id = role_ids[str(payload.emoji)]
            role = discord.utils.get(guild.roles, id=role_id)
            if role is not None and member is not None:
                await member.remove_roles(role)


def setup(bot):
    bot.add_cog(Welcome(bot))
