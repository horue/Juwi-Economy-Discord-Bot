import discord
from discord.ext import commands
import sqlite3
import requests
from key import bot_key

## Bot Configurations ##

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = 'b!', case_insensitive = True, activity=discord.CustomActivity(name="Use 'b!help' for help"), status=discord.Status.online, intents=intents)



## Bot Commands ##


@bot.event
async def on_ready():
  print('{0.user} is online.' . format(bot))



@bot.command()
async def helpbank(ctx):
  await ctx.send('Help for economy commands goes here.')

@bot.command()
async def bank(ctx):
  await ctx.sendo('-')


bot.run(bot_key)