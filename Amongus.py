import discord
from discord import Member
import random
from discord.ext import commands, tasks
import time

client = commands.Bot(command_prefix = '.')
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Skalave von Autismus .help '))

@client.command()
async def code(ctx, code):
    await ctx.channel.purge(limit=1)


client.run("NzYyMDE5MDkzMzI2NTk0MDc4.X3jDlQ.Ssjo9lzTfR9p2MuWpsAwHfzDq70")