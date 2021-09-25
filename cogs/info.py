import discord
from discord.ext import commands
import asyncio

jap_logo = "https://cdn.discordapp.com/attachments/813722820462379028/824963649470070785/flag.PNG"
seele_icon = "https://cdn.discordapp.com/attachments/827750533091164212/888979263376748554/2144a219bf596033a533fe27159ddbb9_5411164789189210907.jpg"
seele_bg = "https://cdn.discordapp.com/attachments/827750533091164212/888975323880902706/wp6452089-seele-vollerei-wallpapers.png"

class info(commands.Cog):
  def __init__(self, client):
    self.client = client

  # Events
  @commands.Cog.listener()
  async def on_ready(self):
    print('info-cog Active')
    
  # Commands
  @commands.group(invoke_without_command=True)
  async def help(self, ctx):
    embed = discord.Embed(
          title="Seele Vollerei Bot Commands",
          url="https://Seele-Bot.rafaellachica.repl.co",
          description="All Available Commands",
          image="https://cdn.discordapp.com/attachments/827750533091164212/888975323880902706/wp6452089-seele-vollerei-wallpapers.png",
          color=discord.Color.blue())
    embed.set_thumbnail(url=seele_icon)
    embed.set_author(name="Seele Vollerei - 2nd Gen Discord Impact", url="https://Seele-Bot.rafaellachica.repl.co", icon_url=seele_icon)
    embed.set_image(url=seele_bg)
    embed.add_field(name=".help learnjp",value="returns learnjp commands",inline=False)
    embed.add_field(name=".help poll",value="returns poll commands ",inline=False)
    embed.add_field(name=".help net",value="returns net commands ",inline=False)
    embed.add_field(name=".help tts",value="returns text-to-speech commands ",inline=False)
    embed.add_field(name=".help utility",value="returns text-to-speech commands ",inline=False)
    embed.add_field(name=".help league",value="returns league of legends commands ",inline=False)



    await ctx.send(embed=embed)

  @help.command()
  async def learnjp(self, ctx):
    embed = discord.Embed(
          title="Learn Japanese Class",
          url="https://Seele-Bot.rafaellachica.repl.co",
          description="All japanese Learning Commands",
          color=discord.Color.red())
    embed.set_author(name="Seele Sensei", url="https://Seele-Bot.rafaellachica.repl.co", icon_url=seele_icon)
    embed.set_thumbnail(url=jap_logo)
    embed.add_field(name="HIRAGANA COMMANDS", value="list of hiragana commands", inline=False,)
    embed.add_field(name="`.learnHiragana<CHARACTER>`", value="display all hiragana characters [A, K, S, T, N, H, M, Y, R, W, n]", inline=False,)
    embed.add_field(name="`.quizHiragana`", value="asks 10 random hiragana characters", inline=False)
    embed.add_field(name="KATAKANA COMMANDS", value="list of katakana commands", inline=False)
    embed.add_field(name="`.learnkatana`", value="display all katakana characters", inline=False)
    embed.add_field(name="`.quizkatakana`", value="asks 10 random katakana characters", inline=False)
    embed.add_field(name="KANJI COMMANDS", value="list of kanji commands",inline=False)
    embed.add_field(name="`.spawnkanji`", value="will give random kanji character and description", inline=False)
    embed.add_field(name="JP-PODCAST COMMANDS",value="list of podcast commands", inline=False)
    embed.add_field(name="`.playjp<lesson>`", value="will play japanese podcast from [ lesson01, lesson02, lesson03, lesson04, lesson05 ]", inline=False)
    embed.add_field(name="`.pausejp`", value="will pause the japanese podcast", inline=False)
    embed.add_field(name="`.resumejp`", value="will resume the paused japanese podcast", inline=False)
    embed.add_field(name="`.stopjp`", value="will stop playing japanese podcast and Seele will leave", inline=False)

    embed.set_footer(text="Learn more by typing #learnjp")
    await ctx.send(embed=embed)

  
  @help.command()
  async def poll(self, ctx):
    embed = discord.Embed(
          title="Seele Vollerei Poll Commands",
          url="https://Seele-Bot.rafaellachica.repl.co",
          description="All Poll Commands",
          color=discord.Color.blue())
    embed.set_thumbnail(url=seele_icon)
    embed.set_author(name="Sebastian Lachicus", url="https://Seele-Bot.rafaellachica.repl.co", icon_url=seele_icon)
    embed.add_field(name=".poll",value="[.poll Question] ",inline=False)
    embed.add_field(name=".poll option",value="[.poll option yourOption]adds option in the optionlist ",inline=False)
    embed.add_field(name=".poll exit",value="exits and discards the poll creation ",inline=False)
    embed.add_field(name=".poll finish",value="will display the question and options  ",inline=False)
    await ctx.send(embed=embed)
  
  @help.command()
  async def net(self, ctx):
    embed = discord.Embed(
          title="Seele Vollerei Net Commands",
          url="https://Seele-Bot.rafaellachica.repl.co",
          description="All Net Commands",
          color=discord.Color.blue())
    embed.set_thumbnail(url=seele_icon)
    embed.set_author(name="Sebastian Lachicus", url="https://Seele-Bot.rafaellachica.repl.co", icon_url=seele_icon)
    embed.add_field(name=".ping",value="[.ping number-of-iterations] ",inline=False)
    await ctx.send(embed=embed)
  
  @help.command()
  async def tts(self, ctx):
    embed = discord.Embed(
          title="Seele Vollerei Text-To-Speech Commands",
          url="https://Seele-Bot.rafaellachica.repl.co",
          description="All Text-To-Speech Commands",
          color=discord.Color.blue())
    embed.set_thumbnail(url=seele_icon)
    embed.set_author(name="Sebastian Lachicus", url="https://Seele-Bot.rafaellachica.repl.co", icon_url=seele_icon)
    embed.add_field(name=".t",value="[.t Message] Seele will read your message outloud",inline=False)
    embed.add_field(name=".pt",value="Seele will the current Text-to-Speech Setting ",inline=False)
    embed.add_field(name=".ttslang",value="[.ttslang languageCode] Seele will change the language accent",inline=False)
    embed.add_field(name=".slow",value="Seele will toggle slow/regular speech",inline=False)
    embed.add_field(name=".lang",value="Seele will display all supported languages",inline=False)
    await ctx.send(embed=embed)
  
  @help.command()
  async def utility(self, ctx):
    embed = discord.Embed(
          title="Seele Vollerei Utility Commands",
          url="https://Seele-Bot.rafaellachica.repl.co",
          description="All Utility Commands",
          color=discord.Color.blue())
    embed.set_thumbnail(url=seele_icon)
    embed.set_author(name="Sebastian Lachicus", url="https://Seele-Bot.rafaellachica.repl.co", icon_url=seele_icon)
    embed.add_field(name=".poke",value="[.poke @User] Seele will send a direct poke message ",inline=False)
    embed.add_field(name=".whisper",value="[.whisper @User message] Seele will relay your message anonymously ",inline=False)
    embed.add_field(name=".confess",value="[.confess message] Seele will post your confession ",inline=False)
    embed.add_field(name=".clear",value="[.clear 1-10] Seele will delete a number of messages from the latest ",inline=False)
    embed.add_field(name=".join",value="[.join] Seele will accompany you in discord VC ",inline=False)
    embed.add_field(name=".leave",value="[.leave] Seele will leave ",inline=False)
    await ctx.send(embed=embed)

  @help.command()
  async def league(self, ctx):
    embed = discord.Embed(
          title="Seele Vollerei Utility Commands",
          url="https://Seele-Bot.rafaellachica.repl.co",
          description="All Utility Commands",
          color=discord.Color.blue())
    embed.set_thumbnail(url=seele_icon)
    embed.set_author(name="Sebastian Lachicus", url="https://Seele-Bot.rafaellachica.repl.co", icon_url=seele_icon)
    embed.add_field(name=".search",value="[.search SummonersName] Seele will return the Summoners Details",inline=False)
    await ctx.send(embed=embed)

    
  



def setup(client):
  client.add_cog(info(client))
