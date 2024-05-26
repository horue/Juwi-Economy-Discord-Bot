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


@bot.command()
async def wallet(ctx):
  server = ctx.message.guild.id
  user = ctx.message.author.id
  server = str(server)
  try:
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS "{server}" (UID BIGINT, Bank INTERGER, Wallet INTERGER)""")
    cursor.execute(f"""SELECT * FROM "{server}" WHERE UID = '{user}'""")
    r = cursor.fetchone()
    if not r:
      cursor.execute(f"""INSERT INTO "{server}" VALUES ('{user}', '0', '0')""")
      connection.commit()
      await ctx.send('Wallet created.')
    else:
      cursor.execute(f"""SELECT Wallet FROM "{server}" WHERE UID = {user}""")
      w=cursor.fetchone()
      cursor.execute(f"""SELECT Bank FROM "{server}" WHERE UID = {user}""")
      b=cursor.fetchone()
      connection.commit()
      await ctx.send(f'Wallet: {w[0]} e Bank: {b[0]}')
  except sqlite3.Error as e:
    await ctx.send(f'Error. {e}')



bot.run(bot_key)