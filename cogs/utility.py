import discord
from discord.ext import commands
import asyncio

# WordSets and Images

seele_disappointed = "https://cdn.discordapp.com/attachments/827750533091164212/888963103692296202/6d96462777ec0a3228c69f9bb576c6df.jpg"
pokes = "https://cdn.discordapp.com/attachments/827750533091164212/827750562648031242/d5b18a40da583b359f2e953c1c7abe27f4c28b21r1-600-338_hq.gif"
seele_icon = "https://cdn.discordapp.com/attachments/827750533091164212/888979263376748554/2144a219bf596033a533fe27159ddbb9_5411164789189210907.jpg"
seele_jap_only = "https://cdn.discordapp.com/attachments/827750533091164212/888961872353705994/d90ecaf73e1f5ac6698e9dcea63ac2e7.jpg"

# poll indicators
enable_option = False
poll_message = " "
num_emoji = [":one:",":two:",":three:",":four:",":five:"]
options = []
pollcounter = True 
index = 0
emji_count =0

#command counter
cmdcounter = True

class utility(commands.Cog):
  def __init__(self, client):
    self.client = client

  # Events
  @commands.Cog.listener()
  async def on_ready(self):
    print('utility-cog Active')
  
  
  @commands.command()
  async def poke(self, ctx, username: discord.Member):
    global cmdcounter
    
    if cmdcounter == True :
      channel = await username.create_dm()
      await channel.send(str(ctx.author) + " pokes you")
      await channel.send(pokes)
      await ctx.message.add_reaction("👌")
      cmdcounter = False
      await asyncio.sleep(4)
      cmdcounter = True
    else: 
      await ctx.send("`Captain! Please don't use the command too fast`")
      await asyncio.sleep(4)
      cmdcounter = True
  
  @commands.command()
  async def whisper(self, ctx, username: discord.Member,*,message):
      channels = await username.create_dm()
      embed = discord.Embed(
          title="WHISPER MESSAGE",
          url="https://Seele-Vollerei-Bot.rafaellachica.repl.co",
          description=message,
          color=discord.Color.blue())
      embed.set_author(name="Anonymous Whisper", url="https://Seele-Vollerei-Bot.rafaellachica.repl.co",icon_url=seele_icon)
      embed.set_thumbnail(url=seele_icon)
      embed.set_footer(text="Type .help to learn more")
      await channels.send(embed=embed)
      await ctx.channel.purge(limit=1)
  
  @commands.command()
  async def announceimg(self,ctx,imgurl,*,messages, ch=814645400174198795):
    admin = "Lach#0816"
    author_temp = str(ctx.author)
    if author_temp == admin:
      everyone = discord.utils.get(ctx.guild.roles, id=813708956916121611)
      channel = self.client.get_channel(ch)
      embed = discord.Embed(
          title="SERVER ANNOUNCEMENT",
          url="https://Seele-Vollerei-Bot.rafaellachica.repl.co",
          description="{}".format(everyone.mention) + ' ' + messages,
          color=discord.Color.blue())
      embed.set_author(name="Admin Announcement", url="https://tsukasa-Bot.rafaellachica.repl.co",icon_url=seele_icon)
      embed.set_thumbnail(url=seele_icon)
      embed.set_image(url=imgurl)
      embed.set_footer(text="Message your `admin` to learn more")
      print(ctx.author)
      await channel.send(embed=embed)
      await ctx.channel.purge(limit=1)
    else:
      await ctx.channel.send("`Sorry you are not allowed to use me`")

  
  
  @commands.command()
  async def join(self, ctx):
      if not ctx.message.author.voice:
          await ctx.send('`Captain you are not connected to a voice channel`')
      else:
          channel = ctx.message.author.voice.channel
      await channel.connect()

  @commands.command()
  async def leave(self, ctx):
      voice_client = ctx.message.guild.voice_client
      await voice_client.disconnect()
      await ctx.send('`Roger Captain`')   

  @commands.command()
  async def clear(self, ctx, amount=1):
    #
    if amount <= 10:
      rem = amount + 1
      await ctx.channel.purge(limit=rem)
    else:
      await ctx.send("```Captain! i can only delete 10 messages at a time!```")
        
  @commands.command()
  async def reset(self,ctx):
    rem = 3000
    await ctx.send("```yaml\nROGER CAPTAIN: PLEASE AVOID SENDING MESSAGES WHILE PERFORMING THE DELETION PROCESS```")
    await ctx.send("```yaml\nIT WILL TAKE 3 MINUTES OR MORE DEPENDING IN THE NUMBER OF MESSAGES```")
    await asyncio.sleep(6)
    async with ctx.typing():
      await ctx.channel.purge(limit=rem)
      await asyncio.sleep(2)
      await ctx.channel.purge(limit=rem)
      await asyncio.sleep(2)
      await ctx.channel.purge(limit=rem)
    await ctx.send("```yaml\nRESET SUCCESSFULL: The Channel Looks Good as New!```")
    await ctx.send("```yaml\nEXPERIENCE PROBLEM: Press Ctrl+R to Refresh```")

  @commands.command()
  async def confess(self,ctx,*,messages,ch=824660572644704336):
      emojis = ['👍','😆','😢','😡','🤯']
      channel = self.client.get_channel(ch)
      embed = discord.Embed(
          title="Anonymous Confession",
          url="https://Seele-Vollerei-Bot.rafaellachica.repl.co",
          description=messages,
          
          color=discord.Color.blue())
      embed.set_author(name="Anonymous User!", url="https://Seele-Vollerei-Bot.rafaellachica.repl.co",icon_url=seele_icon)
      embed.set_thumbnail(url=seele_icon)
      embed.set_footer(text="Learn more by typing #help")
      try: 
        await ctx.channel.purge(limit=1)
        msg = await channel.send(embed=embed)
        for emoji in emojis:
          await msg.add_reaction(emoji)
      except: 
        print("An Exception occured")
        await ctx.message.add_reaction("👌")
        msg = await channel.send(embed=embed)
        for emoji in emojis:
          await msg.add_reaction(emoji)

  @commands.command()
  async def confessimg(self,ctx,image=None,*,messages,ch=824660572644704336):
      emojis = ['👍','😆','😢','😡','🤯']
      channel = self.client.get_channel(ch)
      embed = discord.Embed(
          title="Anonymous Confession",
          url="https://Seele-Vollerei-Bot.rafaellachica.repl.co",
          description=messages,
          
          color=discord.Color.purple())
      embed.set_author(name="Anonymous User!", url="https://Seele-Vollerei-Bot.rafaellachica.repl.co",icon_url=seele_icon)
      embed.set_thumbnail(url=seele_icon)
      embed.set_image(url=image)
      embed.set_footer(text="Learn more by typing #help")
      try: 
        await ctx.channel.purge(limit=1)
        msg = await channel.send(embed=embed)
        for emoji in emojis:
          await msg.add_reaction(emoji)
      except: 
        print("An Exception occured")
        await ctx.message.add_reaction("👌")
        msg = await channel.send(embed=embed)
        for emoji in emojis:
          await msg.add_reaction(emoji)
  
  @commands.command()
  async def chat(self,ctx,*,messages):
    admin = "Lach#0816"
    author_temp = str(ctx.author)
  
    if author_temp == admin:
      await ctx.send(messages)
    else:
      await ctx.send("`Sorry you are not allowed to use me`")
  
  ## Seele Poll Commands 

  @commands.group(invoke_without_command=True)
  async def poll(self,ctx,*,pollmsg):
    global pollcounter
    global enable_option
    global poll_message

    if pollcounter == True:
      #await ctx.send("```Poll Question Set! Type [poll option <description>] to add Options ```")

      poll_message = pollmsg
      embed = discord.Embed(
          title="Discord Poll",
          url="https://Seele-Vollerei-Bot.rafaellachica.repl.co",
          description=poll_message,
          
          color=discord.Color.purple())
      embed.set_author(name=ctx.author, url="https://Seele-Vollerei-Bot.rafaellachica.repl.co",icon_url=seele_icon)
      embed.set_thumbnail(url=seele_icon)
      embed.add_field(name="👍 Add Options",value="Type `poll option description`",inline=False)
      embed.set_footer(text="Learn more by typing .help")
      embed.add_field(name="❌ Exit poll",value="Type `poll exit`",inline=False)
      embed.set_footer(text="Learn more by typing .help")
      await ctx.send(embed=embed)
      enable_option = True
      pollcounter = False

    
  @poll.command()
  async def option(self, ctx,*,option):
    global enable_option
    global options

    if enable_option == True:
      if len(options) <= 4:
        options.append(option)
        await ctx.message.add_reaction("👍")
      else:
        await ctx.send("You can only put 5 options")

  @poll.command()
  async def exit(self, ctx):
    global options
    global poll_message
    global num_emoji
    global index
    global emji_count
    global pollcounter
    global enable_option

    enable_option = False
    poll_message = " "
    options = []
    pollcounter = True
    index = 0
    emji_count =0

    await ctx.message.add_reaction("👍")
    await ctx.send("```Roger Captain: Poll Cancelled!```")

  @poll.command()
  async def finish(self, ctx):
    global options
    global poll_message
    global num_emoji
    global index
    global emji_count
    global pollcounter
    global enable_option

    if len(options) > 1:
      # await ctx.send(poll_message)
      # await ctx.send(options)
      embed = discord.Embed(
          title="Discord Poll",
          url="https://Seele-Vollerei-Bot.rafaellachica.repl.co",
          description=poll_message,
          
          color=discord.Color.blue())
      embed.set_author(name=ctx.author, url="https://Seele-Vollerei-Bot.rafaellachica.repl.co",icon_url=seele_icon)
      embed.set_thumbnail(url=seele_icon)

      for opt in options:
        embed.add_field(name=num_emoji[index]+" "+opt,value="react to vote",inline=False)
        index = index + 1
      embed.set_footer(text="Learn more by typing .help")

      data = 3 + index

      
      await ctx.channel.purge(limit=data)

      poll_message = await ctx.send(embed=embed)

      if index == 1:
        await poll_message.add_reaction('1️⃣')
      if index == 2:
        await poll_message.add_reaction('1️⃣')
        await poll_message.add_reaction('2️⃣')
      if index == 3:
        await poll_message.add_reaction('1️⃣')
        await poll_message.add_reaction('2️⃣')
        await poll_message.add_reaction('3️⃣')
      if index == 4:
        await poll_message.add_reaction('1️⃣')
        await poll_message.add_reaction('2️⃣')
        await poll_message.add_reaction('3️⃣')
        await poll_message.add_reaction('4️⃣')
      if index == 5:
        await poll_message.add_reaction('1️⃣')
        await poll_message.add_reaction('2️⃣')
        await poll_message.add_reaction('3️⃣')
        await poll_message.add_reaction('4️⃣')
        await poll_message.add_reaction('5️⃣')
      
      enable_option = False
      poll_message = " "
      options = []
      pollcounter = True
      index = 0
      emji_count =0

    else:
      await ctx.message.add_reaction("❌")
      await ctx.send("```Poll Options cannot be empty or lessthan 1```")

  

def setup(client):
  client.add_cog(utility(client))
