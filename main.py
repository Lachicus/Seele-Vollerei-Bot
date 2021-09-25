import discord
import youtube_dl
from discord.ext import commands
from discord.voice_client import VoiceClient

import os
import time
import asyncio
from host.keep_alive import keep_alive


client = commands.Bot(command_prefix='.')
client.remove_command("help")
botKEY = os.environ.get("TOKEN")

async def on_ready(self):
    print('Observer-cog is Active')
    
@client.command()
async def load(ctx, extension):
  admin = "Lach#0816"
  author_temp = str(ctx.author)

  if author_temp == admin:
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f"{str(extension)}-cog has been turned-on")
  else:
    await ctx.channel.send("`Sorry you don't have the permission`")


@client.command()
async def unload(ctx, extension):
  admin = "Lach#0816"
  author_temp = str(ctx.author)

  if author_temp == admin:
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f"{str(extension)}-cog has been turned-off")
  else:
    await ctx.channel.send("`Sorry you don't have the permission`")

@client.command()
async def restart(ctx, extension):
  admin = "Lach#0816"
  author_temp = str(ctx.author)

  if author_temp == admin:
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f"{str(extension)}-cog restarting")
    await asyncio.sleep(2)
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f"{str(extension)}-cog has turned-on")
  else: 
    await ctx.channel.send("`Sorry you don't have the permission`")

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if str(message.author) == "Tsukasa#9908":
    if message.content.startswith("Seele: Command Reboot"):
        for filename in os.listdir('./cogs'):
          await message.channel.send(f"```apache\n{str(filename[:-3])}-Cogs: rebooting```")
          if filename.endswith('.py'):
            client.unload_extension(f'cogs.{filename[:-3]}')
  
  await client.process_commands(message)


for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')


keep_alive()
client.run(botKEY)