# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(str(client.user) + ' has connected to Discord!')

@client.event
async def on_member_join(member):
    member.send("All members of Rochester Student/Parent Help server must use their real first and last name as their nickname in order to post messages. You can send a message to any moderator to change your nickname.")

client.run(TOKEN)
