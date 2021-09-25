import discord
from discord.ext import commands
import asyncio
import youtube_dl

seele_icon = "https://cdn.discordapp.com/attachments/827750533091164212/888979263376748554/2144a219bf596033a533fe27159ddbb9_5411164789189210907.jpg"
seele_jap_only = "https://cdn.discordapp.com/attachments/827750533091164212/888961872353705994/d90ecaf73e1f5ac6698e9dcea63ac2e7.jpg"

lesson01 = "https://www.youtube.com/watch?v=siBMCOm83ko&t=1s"
lesson02 = "https://www.youtube.com/watch?v=U9JXNHNpYuY"
lesson03 = "https://www.youtube.com/watch?v=2Cxap8hvcUA"
lesson04 = "https://www.youtube.com/watch?v=_XwvcQUGYqU"
lesson05 = "https://www.youtube.com/watch?v=8ngjNTsAE8U"
lesson_list = [ "lesson01", "lesson02", "lesson03", "lesson04", "lesson05" ]

## Japanese Learning Commands
## Jp Media Library

jap_logo = "https://cdn.discordapp.com/attachments/813722820462379028/824963649470070785/flag.PNG"

hiragana_A = "https://cdn.discordapp.com/attachments/824977447161692161/824980032912228392/AIUEO.PNG"
hiragana_K = "https://cdn.discordapp.com/attachments/824977447161692161/824977480028389386/KAKIKUKEKO.PNG"
hiragana_S = "https://cdn.discordapp.com/attachments/824977447161692161/824977487229485106/SASHISUSESO.PNG"
hiragana_T = "https://cdn.discordapp.com/attachments/824977447161692161/824977488513204244/TACHITSUTETO.PNG"
hiragana_N = "https://cdn.discordapp.com/attachments/824977447161692161/824977484415369266/NANINUNENO.PNG"
hiragana_H = "https://cdn.discordapp.com/attachments/824977447161692161/824977476349591592/HAHIHUHEHO.PNG"
hiragana_M = "https://cdn.discordapp.com/attachments/824977447161692161/824977481576349756/MAMIMUMEMO.PNG"
hiragana_Y = "https://cdn.discordapp.com/attachments/824977447161692161/824977491286425670/YAYUYO.PNG"
hiragana_R = "https://cdn.discordapp.com/attachments/824977447161692161/824977485572734996/RARIRURERO.PNG"
hiragana_W = "https://cdn.discordapp.com/attachments/824977447161692161/824977489617092648/WAO.PNG"
hiragana_n = "https://cdn.discordapp.com/attachments/824977447161692161/824977482644979732/n.PNG"

katakana_A = "https://cdn.discordapp.com/attachments/824977447161692161/824992930644492288/AIUEO.PNG"
katakana_K = "https://cdn.discordapp.com/attachments/824977447161692161/824992934877069352/KAKIKUKEKO.PNG"
katakana_S = "https://cdn.discordapp.com/attachments/824977447161692161/824992944460791828/SASHISUSESO.PNG"
katakana_T = "https://cdn.discordapp.com/attachments/824977447161692161/824992946834243636/TACHITSUTETO.PNG"
katakana_N = "https://cdn.discordapp.com/attachments/824977447161692161/824992940127682560/NANINUNENO.PNG"
katakana_H = "https://cdn.discordapp.com/attachments/824977447161692161/824992932842700810/HAHIHUHEHO.PNG"
katakana_M = "https://cdn.discordapp.com/attachments/824977447161692161/824992936281505843/MAMIMUMEMO.PNG"
katakana_Y = "https://cdn.discordapp.com/attachments/824977447161692161/824993854926749726/YAYUYO.PNG"
katakana_R = "https://cdn.discordapp.com/attachments/824977447161692161/824992942254456852/RARIRURERO.PNG"
katakana_W = "https://cdn.discordapp.com/attachments/824977447161692161/824992948240121896/WAO.PNG"
katakana_n = "https://cdn.discordapp.com/attachments/824977447161692161/824992937791455252/n.PNG"

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data) 
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)



class learnjp(commands.Cog):
  def __init__(self, client):
    self.client = client

  # Events
  @commands.Cog.listener()
  async def on_ready(self):
    print('learnjp-cog Active')

 

  @commands.command()
  async def learnhiragana(self,ctx,args):
      ch = 824960250158252042
      channel = self.client.get_channel(ch)
      arg = args.lower()
      if(arg == "a"):
          await channel.send(hiragana_A)
      if(arg == "k"):
          await channel.send(hiragana_K)
      if (arg == "s"):
          await channel.send(hiragana_S)
      if (arg == "t"):
          await channel.send(hiragana_T)
      if (arg == "n"):
          await channel.send(hiragana_N)
          await channel.send(hiragana_n)
      if (arg == "h"):
          await channel.send(hiragana_H)
      if (arg == "m"):
          await channel.send(hiragana_M)
      if (arg == "y"):
          await channel.send(hiragana_Y)
      if (arg == "r"):
          await channel.send(hiragana_R)
      if (arg == "w"):
          await channel.send(hiragana_W)


  @commands.command()
  async def learnkatakana(self,ctx,args):
      ch = 824960473871024139
      channel = self.client.get_channel(ch)
      arg = args.lower()
      if(arg == "a"):
          await channel.send(katakana_A)
      if(arg == "k"):
          await channel.send(katakana_K)
      if (arg == "s"):
          await channel.send(katakana_S)
      if (arg == "t"):
          await channel.send(katakana_T)
      if (arg == "n"):
          await channel.send(katakana_N)
          await channel.send(katakana_n)
      if (arg == "h"):
          await channel.send(katakana_H)
      if (arg == "m"):
          await channel.send(katakana_M)
      if (arg == "y"):
          await channel.send(katakana_Y)
      if (arg == "r"):
          await channel.send(katakana_R)
      if (arg == "w"):
          await channel.send(katakana_W)


  @commands.command()
  async def playjp(self,ctx, arg):
      topic = arg.lower()

      if not ctx.message.author.voice:
          await ctx.send('`Captain you are not connected to a voice channel`')
      else:
          try:
            channel = ctx.message.author.voice.channel
            await channel.connect()
          except:
             pass

      server = ctx.message.guild
      voice_channel = server.voice_client
      
    
      if topic == "lesson01":  
        async with ctx.typing():
            player = await YTDLSource.from_url(lesson01, loop=self.client.loop)
        voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
        await ctx.send('`Now playing: {}`'.format(player.title))

      if topic == "lesson02":
        async with ctx.typing():
            player = await YTDLSource.from_url(lesson02, loop=self.client.loop)
        voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
        await ctx.send('`Now playing: {}`'.format(player.title))
      
      if topic == "lesson03":
        async with ctx.typing():
            player = await YTDLSource.from_url(lesson03, loop=self.client.loop)
        voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
        await ctx.send('`Now playing: {}`'.format(player.title))
      
      if topic == "lesson04":
        async with ctx.typing():
            player = await YTDLSource.from_url(lesson04, loop=self.client.loop)
        voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
        await ctx.send('`Now playing: {}`'.format(player.title))
      
      if topic == "lesson05":
        async with ctx.typing():
            player = await YTDLSource.from_url(lesson05, loop=self.client.loop)
        voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
        await ctx.send('`Now playing: {}`'.format(player.title))

      if not(topic == "lesson01"):
        if not(topic == "lesson02"):
          if not(topic == "lesson03"):
            if not(topic == "lesson04"):
              if not(topic == "lesson05"):
                  voice_client = ctx.message.guild.voice_client
        await voice_client.disconnect()
        await ctx.send('Captain There is no `'+ arg + '` in the database' )


  @commands.command()
  async def pausejp(self,ctx):
      server = ctx.message.guild
      voice_channel = server.voice_client
      voice_channel.pause()
      await ctx.send('`Roger Captain : The Podcast is Paused.`')


  @commands.command()
  async def resumejp(self,ctx):
      server = ctx.message.guild
      voice_channel = server.voice_client
      voice_channel.resume()
      await ctx.send('`Roger Captain : The Podcast is Resumed.`')


  @commands.command()
  async def stopjp(self,ctx):
      voice_client = ctx.message.guild.voice_client
      await voice_client.disconnect()
      await ctx.send('`Roger Captain : The Podcast has stopped.`')



    
  
      
    

def setup(client):
  client.add_cog(learnjp(client))
