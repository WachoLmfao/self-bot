import discord
import time
from random import randint

TOKEN = "TOKEN_HERE" 


client = discord.Client()
client = commands.Bot(command_prefix="change_the_prefix_here") #change the prefix in here

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
    
 #Do stuff here 
    
client.run(TOKEN)
