import discord
from discord.ext import commands
import asyncio

restricted_words = ["bading","bakla","bobo","tanga","tanginamo", "tangina", "tngina", "vovo", "weak", "cheat", "gago", "qaqo", "futa", "pakyu", "bovo", "tangi","fuck you","fuckyou","T A N G I N A", "Tang in a glass", "pota", "fota"]
seele_disappointed = "https://cdn.discordapp.com/attachments/827750533091164212/891434905416912957/download.jpg"
#"https://cdn.discordapp.com/attachments/827750533091164212/888963103692296202/6d96462777ec0a3228c69f9bb576c6df.jpg"
pokes = "https://cdn.discordapp.com/attachments/827750533091164212/827750562648031242/d5b18a40da583b359f2e953c1c7abe27f4c28b21r1-600-338_hq.gif"
seele_icon = "https://cdn.discordapp.com/attachments/827750533091164212/888979263376748554/2144a219bf596033a533fe27159ddbb9_5411164789189210907.jpg"
seele_jap_only = "https://cdn.discordapp.com/attachments/827750533091164212/888961872353705994/d90ecaf73e1f5ac6698e9dcea63ac2e7.jpg"
alphabet = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","ｂ","ｃ","ｄ","ｆ","ｇ","ｈ","ｊ","ｋ","ｌ","ｍ", "ｎ","ｐ","ｑ","ｒ","ｓ","ｔ","ｖ","ｘ","ｙ","ｚ"}
names = {"BRONYA", "Bronya", "brony", "bron"}

class net(commands.Cog):
  def __init__(self, client):
    self.client = client

  # Events
  @commands.Cog.listener()
  async def on_ready(self):
    print('observer-cog Active')

  # Observer Events
  @commands.Cog.listener()
  async def on_message(self,message):
    sentence = message.content.lower()

    is_bot = message.author.bot 

    if is_bot:

      if str(message.author) == "Tsukasa#9908":
        if message.content.startswith("Seele: command ping"):
              await message.channel.send("```yaml\nCommand-Cogs:(Working) Passed```")
              await message.channel.send("```yaml\nLearnjp-Cogs:(Working) Passed```")
              await message.channel.send("```yaml\nObserver-Cogs:(Working) Passed```")
              await message.channel.send("```yaml\nFlask-Cogs:(Working) Passed```")
              await message.channel.send("```yaml\nUptimeRobot-Cogs:(Working) Passed```")
              await message.channel.send(f'```yaml\nSeele Vollerei Latency: {round(self.client.latency * 1000)}ms```')

      pass
    else:

      if message.content.startswith('.showip'):
          embed = discord.Embed(
            title="ATERNOS MINECRAFT SERVER",
            url="https://aternos.org/:en/",
            description="MC NOTICE",
            color=discord.Color.green())
          embed.set_author(name="Aternos", url="https://Seele-Vollerei-Bot.rafaellachica.repl.co", icon_url=seele_icon)
          embed.set_thumbnail(url=seele_icon)
          embed.add_field(name="ASIAN BATH HOUSE MC SERVER ",value="IP:AsianBathHouse.aternos.me:33893",inline=False)
          embed.add_field(name="Not Working?",value="Type `.dynip` for a dynamic ip request",inline=False)
          embed.set_footer(text="Learn more by typing .help")

          await message.channel.send(embed=embed)
      
      if not message.content.startswith('.'):
        if message.channel.name == '💬│jp-chat':
            if str(message.author) != "Seele Vollerei#9911":
              if str(message.author) != "Translator#2653":
                  if not message.content.startswith('?'):
                    if not message.content.startswith('#'):
                      if not message.content.startswith('-t'):
                        if any( word in sentence for word in alphabet):
                                await message.delete()
                                await message.channel.send("`"+str(message.author)+ "`" + ': このチャンネルでは`English`の文字は使用できません')
                                await message.channel.send(seele_jap_only)

      if message.content.startswith('#'):
        if message.channel.name == '💬│jp-chat':
          await message.channel.send('`＃`プレフィックスが `.`に変更されました。コマンドのリストを表示するには、` .help`を使用してみてください')
        else:
          await message.channel.send('The `#`prefix has been changed to `.` Try using `.help` to see the list of commands')
      
      if any( word in sentence for word in restricted_words):
        if any( word in sentence for word in names):
          await message.channel.send(str(message.author) + 'Shut your dirty mouth you twat!')
          await message.channel.send(seele_disappointed)
      
      if str(message.author) != "Tamago#3912":
        if str(message.author) != "Mudae#0807":
          if any( word in sentence for word in restricted_words):
              await message.channel.send(str(message.author) + ' Seele is disappointed in your choice of words captain')
              await message.channel.send(seele_disappointed)
      
      if ".chat" in message.content:
          await message.delete()

      

      
      
  
  

      
    

def setup(client):
  client.add_cog(net(client))
