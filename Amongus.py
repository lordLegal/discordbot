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

@client.command()
async def code(ctx, code, *, member):
    await ctx.channel.purge(limit=1)
    await ctx.send.member(code)



client.run(os.environ['DISCORD_TOKEN'])