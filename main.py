#SETUP TUT: 

import os
import discord
import requests
from discord.ext import commands

prefix = "PREFIX HERE"
bot = commands.Bot(command_prefix=prefix)

@bot.command(aliases=["b", "bp", "bypass"])
async def unshorten(ctx, *, arg=""):
  if arg == "":
      await ctx.reply('LINK was not found!')
  else:
      r=requests.get('https://029aa9c3-ed8a-4500-aa93-0ac023829655.id.repl.co/?key=PUBLIC&url='+arg)
      a = ('%'+r.text)
      chunks = a.split(',')
      dest = chunks[0] 
      stripped = dest.split('"')
      embed = discord.Embed(color=discord.Color(65280))
      embed.add_field(name="Bypassed Link:", value=stripped[3], inline=False)
      embed.set_footer(text="Credits: Thebypasser.com")
      await ctx.reply("API: https://029aa9c3-ed8a-4500-aa93-0ac023829655.id.repl.co/", embed=embed)

bot.run("BOT TOKEN HERE")
