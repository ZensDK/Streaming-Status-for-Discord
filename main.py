import discord
from discord.ext import commands
import asyncio
from webserver import keep_alive
import os
my_secret = os.environ['Token']

prefix = ">"

keep_alive()

bot = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity = discord.Streaming(name = "Stream Subject" , url = "https://twitch.tv/username"))
    print("Logging Succesful!")
  
bot.run(os.getenv('Token'), bot=False)
