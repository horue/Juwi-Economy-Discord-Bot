import discord
from discord.ext import commands
import sqlite3
from key import bot_key


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = 'b!', case_insensitive = True, activity=discord.CustomActivity(name="Use 'b!help' for help"), status=discord.Status.online, intents=intents)


@bot.event
async def on_ready():
  print('{0.user} is online.' . format(bot))


bot.run(bot_key)