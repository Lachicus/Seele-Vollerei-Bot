import discord
from discord.ext import commands
import asyncio


class crypto(commands.Cog):
  def __init__(self, client):
    self.client = client

  # Events
  @commands.Cog.listener()
  async def on_ready(self):
    print('crypto-cog Active')
    
  # Commands
  @commands.command()
  async def coin(self,ctx,crypto):
    print("show crypto value")

    ## usage - .coin btc
    ## usage - .coin slp


      
    

def setup(client):
  client.add_cog(crypto(client))