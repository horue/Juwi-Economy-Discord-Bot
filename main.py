import discord
from discord.ext import commands
import sqlite3
import requests
import re
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


@bot.command(aliases=['w'])
async def wallet(ctx, user=""):
  server = ctx.message.guild.id
  if user == '':
    user = ctx.message.author.id
  else:
    id = re.search(r'<@(\d+)>', user)
    user = id.group(1)
    print(user)
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
      await ctx.send(f'Wallet: ${w[0]}\nBank: ${b[0]}')
  except sqlite3.Error as e:
    await ctx.send(f'Error. {e}')


@bot.command()
async def add(ctx,user, value):
  value = value
  author = ctx.message.author
  server = ctx.message.guild.id
  user = ctx.message.author.id
  server = str(server)
  try:
      cursor.execute(f"""SELECT * FROM "{server}" WHERE UID = '{user}'""")
      r = cursor.fetchone()
      if not r:
        await ctx.send(f"Invalid. {author} does not have a wallet yet.")
      elif r:
        cursor.execute(f"""UPDATE "{server}" SET Wallet = Wallet + {value} WHERE UID = '{user}'""")
        connection.commit()
        await ctx.send(f"{value} added to {user}'s account.")
  except sqlite3.Error as e:
    await ctx.send(f'Error: {e}')


@bot.command()
async def take(ctx, user, value):
  value = value
  author = ctx.message.author
  server = ctx.message.guild.id
  user = ctx.message.author.id
  server = str(server)
  try:
    if author != user:
      await ctx.send("You can't use someone else's bank account.")
  except:
    await ctx.send('Error.')





bot.run(bot_key)