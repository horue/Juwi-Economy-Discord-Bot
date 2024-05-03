import discord
from discord.ext import commands
import sqlite3
import requests
from key import bot_key

## Bot Configurations ##


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = 'b!', case_insensitive = True, activity=discord.CustomActivity(name="Use 'b!help' for help"), status=discord.Status.online, intents=intents)


## SQLite3 Configurations ##


connection=sqlite3.connect("eco_xrz.db")
cursor=connection.cursor()


## Bot Commands ##


@bot.event
async def on_ready():
  print('{0.user} is online.' . format(bot))



@bot.command()
async def helpbank(ctx):
  await ctx.send('Help for economy commands goes here.')

@bot.command()
async def bankid(ctx):
  id = ctx.message.guild.id
  await ctx.send(id)


bot.run(bot_key)