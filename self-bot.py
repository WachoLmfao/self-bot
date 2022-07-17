import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix="1") #this is self-bots prefix, feel free to change it anytime

async def status_task():
    while True:
     await bot.change_presence(activity=discord.Game('Counter-Strike Global Offensive'))
     await asyncio.sleep(2)
     await bot.change_presence(activity=discord.Game('Minecraft'))
     await asyncio.sleep(2)
     await bot.change_presence(activity=discord.Game('Among Us'))
     await asyncio.sleep(2)
     await bot.change_presence(activity=discord.Game('The LEGO® Movie™ - Videogame'))
     await asyncio.sleep(2)
     await bot.change_presence(activity=discord.Game('Grand Theft Auto V'))
     await asyncio.sleep(2)
     await bot.change_presence(activity=discord.Game('Forza Horizon 5'))
     await asyncio.sleep(2)
     await bot.change_presence(activity=discord.Game('Grand Theft Auto IV'))
     await asyncio.sleep(2)
     await bot.change_presence(activity=discord.Game('Spider-Man 3'))
    
    #this command right here, changes your game every 2 seconds

@bot.event
async def on_ready():
    print("Bot is ready!") #this prints "Bot is ready!" when its on
    bot.loop.create_task(status_task()) #and this loops the status_task
    

@bot.event
async def on_message_delete(message):
  print(f"Message deleted: {message.content} by {message.author}") #When a message is deleted, it prints its content and author

bot.run("TOKEN_HERE") #and place your self bots token here

#also type "pip install -U discord.py-self" in the console before launching it !
