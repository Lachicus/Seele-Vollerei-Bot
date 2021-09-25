import discord
from discord.ext import commands
import asyncio


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
  

      
    

def setup(client):
  client.add_cog(net(client))
