import discord
from discord.ext import commands
import asyncio
from gtts import gTTS
import os

# Settings

language = "en"
slow_mode = False
seele_icon = "https://cdn.discordapp.com/attachments/827750533091164212/888979263376748554/2144a219bf596033a533fe27159ddbb9_5411164789189210907.jpg"


class tts(commands.Cog):
  def __init__(self, client):
    self.client = client
    global language
    ttsconfig = open(r".//configurations//tts-config.txt","r")
    lang = ttsconfig.readline(2)
    language = lang

  # Events
  @commands.Cog.listener()
  async def on_ready(self):
    
    print('text_to_speech-cog Active')
    
    
  # async def t(self,ctx,*,message):
  #   global language
  #   global slow_mode
  #   output = gTTS(text=message, lang=language, slow=slow_mode)
  #   output.save("output.mp3")

  #   if not ctx.message.author.voice:
  #         await ctx.send('`Captain you are not connected to a voice channel`')
  #   else:
  #     try:
  #       channel = ctx.message.author.voice.channel
  #       await channel.connect()
  #     except:
  #       pass
    
  #     server = ctx.message.guild
  #     voice_channel = server.voice_client
  #     voice_channel.play(discord.FFmpegPCMAudio("output.mp3"))
  
  @commands.Cog.listener()
  async def on_message(self,message):
    sentence = message.content.lower()
    is_bot = message.author.bot 
    global language
    global slow_mode
    

    if not is_bot:
      if message.channel.name == '🎤│text-to-speech':
        if not message.content.startswith('.'):
          output = gTTS(text=sentence, lang=language, slow=slow_mode)
          output.save("output.mp3")

          if not message.author.voice:
            await message.channel.send('`Captain you are not connected to a voice channel`')
          else:
            try:
              channel = message.author.voice.channel
              await channel.connect()
            except:
              pass
            
            server = message.guild
            voice_channel = server.voice_client
            voice_channel.play(discord.FFmpegPCMAudio("output.mp3"))
        
  @commands.command()
  async def ttslang(self,ctx,lang):
    global language
    language = lang
    ttsconfig = open(r".//configurations//tts-config.txt","w")
    ttsconfig.write(lang + " - Language" + "\nFalse - slowMode")
    await ctx.send(f'`Roger Captain: Language Changed to {lang}`')
  
  @commands.command()
  async def tp(self,ctx):
    global language
    global slow_mode

    embed = discord.Embed(
          title="Text-To-Speech Profile",
          url="https://Bronya-Bot.rafaellachica.repl.co",
          description="Type `help tts` to learn more",
          color=discord.Color.blue())
    embed.set_thumbnail(url=seele_icon)
    embed.add_field(name="Language: ",value=language,inline=False)
    embed.add_field(name="Voice Slow Mode: ",value=slow_mode,inline=False)
    await ctx.send(embed=embed)
  
  @commands.command()
  async def lang(self,ctx):
    global language
    global slow_mode

    embed = discord.Embed(
          title="Text-To-Speech Supported Languages",
          url="https://Bronya-Bot.rafaellachica.repl.co",
          description="tl = tagalog\n en = english\n ja = japanese\n zh = chinese\n ru = russian\n es = espanyol\n ko = korean\n fr = french\n de = german\n ar = arabic",
          color=discord.Color.purple())
    embed.set_thumbnail(url=seele_icon)
    
    await ctx.send(embed=embed)
  
  @commands.command()
  async def test(self,ctx,*,msg):
    await ctx.send(msg, tts=True)
 
  @commands.command()
  async def slow(self, ctx):
    global slow_mode

    if slow_mode == True:
      slow_mode = False
    else:
      slow_mode = True
    
    await ctx.message.add_reaction("👍")
  
  
 

    


    

  

    
    

    
  

      
    

def setup(client):
  client.add_cog(tts(client))
