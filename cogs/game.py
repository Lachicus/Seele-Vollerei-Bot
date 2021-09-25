import discord
from discord.ext import commands
import asyncio


class game(commands.Cog):
  def __init__(self, client):
    self.client = client

  # Events
  @commands.Cog.listener()
  async def on_ready(self):
    print('game-cog Active')
    
  # Commands
  @commands.command()
  async def start(self,ctx):
    embed = discord.Embed(
          title="Spyfall",
          url="https://Seele-Bot.rafaellachica.repl.co",
          description="All Utility Commands",
          color=discord.Color.blue())
    embed.set_thumbnail(url=None)
    embed.set_author(name="Sebastian Lachicus", url="https://Seele-Bot.rafaellachica.repl.co", icon_url=None)
    embed.add_field(name=".search",value="[.search SummonersName] Seele will return the Summoners Details",inline=False)
    await ctx.send(embed=embed)
  
  @commands.command()
  async def spyinfo(self,ctx):
    print("sample command")

  
      
    

def setup(client):
  client.add_cog(game(client))