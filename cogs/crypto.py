import discord
from discord.ext import commands, tasks
import asyncio
from bs4 import BeautifulSoup
import requests
from datetime import datetime
  

## Media
slp = "https://cdn.discordapp.com/attachments/813722820462379028/896644728039297034/SLP.png"

class crypto(commands.Cog):
  def __init__(self, client):
    self.client = client
    self.updateCrypto.start()

  # Events
  @commands.Cog.listener()
  async def on_ready(self):
    print('crypto-cog Active')
    
    
  # Commands
  @commands.command()
  async def slp(self,ctx,amount=1):
   if ctx.channel.name == '🤖│bot-commands': 
      Url = 'https://coinmarketcap.com/currencies/smooth-love-potion/slp/php/'
      Url2 = 'https://coinmarketcap.com/currencies/smooth-love-potion/'
      HTML = requests.get(Url)
      HTML2 = requests.get(Url2)
      soup = BeautifulSoup(HTML.text,'html.parser')
      soup2 = BeautifulSoup(HTML2.text,'html.parser')
    
      slp_php = soup.find("div", attrs={'class':'priceValue'}).text
      php_val = slp_php.replace("₱", "")
      temp = float(php_val) * amount

      slp_btc = soup.find("div", attrs={'class':'sc-16r8icm-0 kjciSH alternatePrices'}).find("p", attrs={'class':'esfl2f-0 kqzSsi'})
      for match in slp_btc.findAll('span'):
        match.replace_with(" ")
      final = slp_btc.text
    
      slp_eth = soup.find("div", attrs={'class':'sc-16r8icm-0 kjciSH alternatePrices'}).find("p", attrs={'class':'esfl2f-0 kqzSsi'}).next_sibling
      for match in slp_eth.findAll('span'):
        match.replace_with(" ")
      final2= slp_eth.text

      slp_usd = soup2.find("div", attrs={'class':'priceValue'}).text
      usd_val = slp_usd.replace("$", "")
      temp2 = float(usd_val) * amount

      current = datetime.now()
      dt_string = current.strftime("%d/%m/%Y %H:%M:%S")
    

      embed = discord.Embed(
      title="Sweet Love Potion",
      url="https://Seele-Bot.rafaellachica.repl.co",
      description="Sweet Love Potion Axie Infinity Tokens",
      color=discord.Color.blue())
      embed.set_thumbnail(url=slp)
      embed.set_author(name="Seele Vollerei", url="https://Seele-Bot.rafaellachica.repl.co", icon_url=slp)
      if amount > 1:
        embed.add_field(name="SLP PHP VALUE",value=f"price: {slp_php} ({amount} SLP = ₱{temp})",inline=False)
        embed.add_field(name="SLP USD VALUE",value=f"price: {slp_usd} ({amount} SLP = ${temp2})",inline=False)
      else:
        embed.add_field(name="SLP PHP VALUE",value=f"price: {slp_php}",inline=False)
        embed.add_field(name="SLP USD VALUE",value=f"price: {slp_usd}",inline=False)
      embed.add_field(name="SLP BTC VALUE",value=f"price: {final}",inline=False)
      embed.add_field(name="SLP ETH VALUE",value=f"price: {final2}",inline=False)
      embed.set_footer(text=f"data aquired: {dt_string}")
      await ctx.send(embed=embed)

  @commands.command()
  async def testing(self,ctx):
    ch1 = 902879885083688962
    ch2 = 902880594256617512
    channel1 = self.client.get_channel(ch1)
    channel2 = self.client.get_channel(ch2)
  
    await ctx.send("test:passed")
    await channel1.edit(name="💷│SLP : ₱3.26")
    await channel2.edit(name="💶│AXS : ₱2000")
    
    
  @tasks.loop(minutes=2.0)
  async def updateCrypto(self):
    await self.client.wait_until_ready()

    ch1 = 902879885083688962
    ch2 = 902880594256617512
    channel1 = self.client.get_channel(ch1)
    channel2 = self.client.get_channel(ch2)

    Url = 'https://coinmarketcap.com/currencies/smooth-love-potion/slp/php/'
    HTML = requests.get(Url)
    soup = BeautifulSoup(HTML.text,'html.parser')
    slp_php = soup.find("div", attrs={'class':'priceValue'}).text

    Url2 = 'https://coinmarketcap.com/currencies/axie-infinity/axs/php/'
    HTML2 = requests.get(Url2)
    soup2 = BeautifulSoup(HTML2.text,'html.parser')
    axs_php = soup2.find("div", attrs={'class':'priceValue'}).text

    await channel1.edit(name=f"💷│SLP : {slp_php}")
    await channel2.edit(name=f"💶│AXS : {axs_php}")
    print("crypto data updated")
    

  

def setup(client):
  client.add_cog(crypto(client))