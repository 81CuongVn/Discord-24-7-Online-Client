import discord
import os
import keep_alive

from discord.ext import commands

client = commands.Bot(command_prefix='YJ!', self_bot=True)

# <!-- Import Your Self Bot Commands <3 --> 

async def on_ready():
  client.remove_command('help')
  await client.change_presence(status=discord.Status.online, activity=discord.Game("Your's Jarvis"))

keep_alive.keep_alive()
client.run(os.getenv("TOKEN"), bot=False)

## <!-- 🚀 Please follow on GitHub to stay tuned with us for more Exciting future Updates like this. | © 2022 — Made By Your's Jarvis #2431 with ♥ -->