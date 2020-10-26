import discord
from discord import Member
import random
from discord.ext import commands, tasks
import time
import os
import sqlite3

client = commands.Bot(command_prefix = '.')
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Skalave von  .help '))
    print("Bot is ready")

@client.command(pass_context = True)
async def dm(ctx, member : discord.Member, *, content: str):
    await ctx.send(member, content)



client.run(os.environ['DISCORD_TOKEN'])