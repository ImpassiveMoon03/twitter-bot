import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = 'twt')

@client.event
async def on_ready():
  print('Logged in!')
  await client.change_presence(
    status = discord.Status.online,
    activity = discord.Game('Twitter')
  )

for filename in os.listdir('./cogs'):
  if filename.endswith(".py"):
    client.load_extension(f"cogs.{filename[:-3]}")

# Log the bot in
client.run(os.environ.get('TOKEN'))