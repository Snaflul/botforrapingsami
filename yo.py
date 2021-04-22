import discord
from discord.ext import commands
from datetime import date
from datetime import timedelta
import datetime


# requires discord.py

client = discord.Client(command)
sami = 692494831410217022
lastMessageDates = []


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print(datetime.datetime.utcnow())
    print(discord.__version__)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Yin's code"))


@client.event
async def on_message(message):
    if message.author.bot: return
    if message.author.id != sami: return
    global lastMessageDates
    if len(lastMessageDates) < 1:
        lastMessageDates.append(message.created_at)
        return
    elif lastMessageDates[0] < (datetime.datetime.utcnow() - timedelta(hours = 24)):
        lastMessageDates.pop(0)
        lastMessageDates.append(message.created_at)
        return
    else:
        await message.delete()
        print("Message deleted")
    
        
client.run('token', client = True)
