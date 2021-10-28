import discord
import youtube_dl
from discord.ext import commands
from discord.voice_client import VoiceClient

import os
import time
import asyncio
import shutil 

from host.keep_alive import keep_alive

client = commands.Bot(command_prefix='.')
client.remove_command("help")
botKEY = os.environ.get("TOKEN")

# Media
seele_icon = "https://cdn.discordapp.com/attachments/827750533091164212/888979263376748554/2144a219bf596033a533fe27159ddbb9_5411164789189210907.jpg"

async def on_ready(self):
    print('Seele Vollerei is Online')
    
@client.command()
async def load(ctx, extension):
  admin = "Lach#0816"
  author_temp = str(ctx.author)

  if author_temp == admin:
    shutil.move(f"./unloaded-cogs/{extension}.py", "./cogs/") 
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f"{str(extension)}-cog has been turned-on")
  else:
    await ctx.channel.send("`Sorry you don't have the permission`")

## dir-dest ./unloaded-cogs/
## dir-source ./cogs/
@client.command()
async def unload(ctx, extension):
  admin = "Lach#0816"
  author_temp = str(ctx.author)

  if author_temp == admin:
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f"{str(extension)}-cog has been turned-off")
    shutil.move(f"./cogs/{extension}.py", "./unloaded-cogs/") 
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

@client.command()
async def cogs(ctx):
  try:
      embed = discord.Embed(
            title="Seele Vollerei Discord Impact Cogs",
            url="https://Seele-Bot.rafaellachica.repl.co",
            description=" ",
            color=discord.Color.blue())
      embed.set_thumbnail(url=seele_icon)
      embed.set_author(name="Sebastian Lachicus", url="https://Seele-Bot.rafaellachica.repl.co", icon_url=seele_icon)
      embed.add_field(name=f"[ ONLINE COGS ]",value="list of active cogs",inline=False)

      for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
          embed.add_field(name=f"{filename}",value=" Status: Working",inline=True)

      embed.add_field(name=f"[ OFFLINE COGS ]",value="list of all inactive cogs",inline=False)

      for filename in os.listdir('./unloaded-cogs'):
        if filename.endswith('.py'):
          embed.add_field(name=f"{filename}",value=" Status: Maintenance",inline=True)
      await ctx.send(embed=embed)

  except:

    embed = discord.Embed(
          title="Seele Vollerei Loaded Cogs",
          url="https://Seele-Bot.rafaellachica.repl.co",
          description="Active Bot-Commands",
          color=discord.Color.blue())
    embed.set_thumbnail(url=seele_icon)
    embed.set_author(name="Sebastian Lachicus", url="https://Seele-Bot.rafaellachica.repl.co", icon_url=seele_icon)
    embed.add_field(name=f"[ ONLINE COGS ]",value="list of active cogs",inline=True)

    for filename in os.listdir('./cogs'):
      if filename.endswith('.py'):
          embed.add_field(name=f"{filename}",value=" Status: Working",inline=True)
    
    embed.add_field(name=f"[ OFFLINE COGS ]",value="list of inactive cogs",inline=True)
  
    await ctx.send(embed=embed)


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if str(message.author) == "Tsukasa#9908":
    if message.content.startswith("Seele: Command Reboot"):
        for filename in os.listdir('./cogs'):
          await message.channel.send(f"```diff\n-{str(filename[:-3])}-Cogs: rebooting```")
          if filename.endswith('.py'):
            client.unload_extension(f'cogs.{filename[:-3]}')
        

        for filename in os.listdir('./cogs'):
          await message.channel.send(f"```yaml\n{str(filename[:-3])}-Cogs: online```")
          if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')
        
        await message.channel.send("```ini\n[ Reboot Success : No Errors Found]```")
      
  await client.process_commands(message)


## reads all cogs.py
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')


keep_alive()
client.run(botKEY)