import discord
from discord.ext import commands
import asyncio
import psutil
import os

seele_icon = "https://cdn.discordapp.com/attachments/827750533091164212/888979263376748554/2144a219bf596033a533fe27159ddbb9_5411164789189210907.jpg"

#load,load5,load15 = psutil.getloadavg()
#cpu_average_usage = (load5/os.cpu_count()) * 100

class net(commands.Cog):
  def __init__(self, client):
    self.client = client

  # Events
  @commands.Cog.listener()
  async def on_ready(self):
    print('net-cog Active')
    
  # Commands
  @commands.command()
  async def ping(self,ctx,index=3):
    for i in range(index):
      ms = round(self.client.latency * 1000)
      await ctx.send(f'`Seele Vollerei Latency:'+ str(ms) +' ms`')
    if ms < 80:
      await ctx.send('`Seele Vollerei is nominal`')
    if ms > 80:
      await ctx.send('`Seele Vollerei is unstable`')
  
  @commands.command()
  async def stats(self,ctx):
    cpu_percentage = psutil.cpu_percent(5)
    memory_percentage = psutil.virtual_memory()[2]

    ##Embed
    embed = discord.Embed(
          title="Seele Vollerei System Status",
          url="https://Seele-Bot.rafaellachica.repl.co",
          description=" ",
          color=discord.Color.blue())
    embed.set_thumbnail(url=seele_icon)
    embed.set_author(name="Sebastian Lachicus", url="https://Seele-Bot.rafaellachica.repl.co", icon_url=seele_icon)
    embed.add_field(name="CPU Usage",value=f"cpu-util: {cpu_percentage}%",inline=False)
    embed.add_field(name="Memory Usage",value=f"memory-used: {memory_percentage}%",inline=False)

    await ctx.send(embed=embed)

    



  

      
    

def setup(client):
  client.add_cog(net(client))
