import discord
from discord.ext import commands
import asyncio

from riotwatcher import LolWatcher
import os

riotKey = os.environ.get("RIOT")
lol_watcher = LolWatcher(riotKey)
region = 'jp1'

seele_icon = "https://cdn.discordapp.com/attachments/827750533091164212/888979263376748554/2144a219bf596033a533fe27159ddbb9_5411164789189210907.jpg"

class riot(commands.Cog):
  def __init__(self, client):
    self.client = client

  # Events
  @commands.Cog.listener()
  async def on_ready(self):
    print('net-cog Active')
    
  # Commands
  @commands.command()
  async def search(self,ctx,*,userName):
    link = userName.replace(" ","+")
    try:
      summoner = lol_watcher.summoner.by_name(region,userName)
      stats = lol_watcher.league.by_summoner(region,summoner['id'])
      if stats != []:
        level = summoner['summonerLevel']
        tier = stats[0]['tier']
        rank = stats[0]['rank']
        lp = stats[0]['leaguePoints']
        wins = int(stats[0]['wins'])
        losses = int(stats[0]['losses'])
        winrate = int((wins / (wins + losses)) * 100)
        

        embed = discord.Embed(
          title="Summoner Details",
          url="https://Seele-Bot.rafaellachica.repl.co",
          description="Summoner: " + userName + f"\n Level: {level}",
          color=discord.Color.blue())
        embed.set_thumbnail(url=seele_icon)
        embed.add_field(name="Rank & Division",value=f"{tier} {rank}",inline=False)
        embed.add_field(name="League Points",value=f"Points: {lp} lp",inline=False)
        embed.add_field(name="Victories/Defeats",value=f"Wins:{wins} Loss:{losses}",inline=False)
        embed.add_field(name="Rank Percentage",value=f"Win ratio: {winrate}%",inline=False)
        embed.add_field(name="Full Details",value=f"https://jp.op.gg/summoner/userName={link}")
        await ctx.send(embed=embed)
      else:
        
        level = summoner['summonerLevel']
        embed = discord.Embed(
          title="Summoner Details",
          url="https://Seele-Bot.rafaellachica.repl.co",
          description="Summoner: " + userName + f"\n Level: {level}",
          color=discord.Color.blue())
        embed.set_thumbnail(url=seele_icon)
        embed.add_field(name="Rank & Division",value="Unranked",inline=False)
        embed.add_field(name="League Points",value="Unranked",inline=False)
        embed.add_field(name="Victories/Defeats",value="Unranked",inline=False)
        embed.add_field(name="Rank Percentage",value="Unranked",inline=False)
        embed.add_field(name="Full Details",value=f"https://jp.op.gg/summoner/userName={link}")
        
        await ctx.send(embed=embed)
        

    except:
      await ctx.channel.send("```Error: Captain the Summoner-Name is incorrect or does not exist!```" + 
      "```Captain im only limited to jp server```")

  # @commands.command()
  # async def test(self,ctx):
    



def setup(client):
  client.add_cog(riot(client))