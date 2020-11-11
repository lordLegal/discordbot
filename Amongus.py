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
async def code(ctx, members):
    await ctx.send.author("Hallo")

@client.command()
async def Hey(ctx):
    embed=discord.Embed(title="Your Bot", color=0xba1c1c)
    embed.add_field(name="Hey", value="This is my Bot It But I can also do some for you", inline=False)
    embed.set_footer(text="by Retox")
    await ctx.send(embed=embed)
    
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=1)
    await ctx.channel.purge(limit=amount)


client.run(os.environ['DISCORD_TOKEN'])