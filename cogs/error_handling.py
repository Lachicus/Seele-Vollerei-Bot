import discord
from discord.ext import commands
from datetime import datetime
import asyncio
import os



class error_handling(commands.Cog):
  def __init__(self, client):
    self.client = client

  # Events
  @commands.Cog.listener()
  async def on_ready(self):
    print('error_handling-cog Active')

  @commands.command()
  async def err_logs(self,ctx):
    with open(".//configurations//error-logs.txt","rb") as file:
      await ctx.send("Seele Vollerei Error Report:", file=discord.File(file,"error-logs.txt"))
      
  @commands.Cog.listener()
  async def on_command_error(self,ctx,error):
    logs = open(r".//configurations//error-logs.txt", "a")
    current = datetime.now()
    dt_string = current.strftime("%d/%m/%Y %H:%M:%S")

    if isinstance(error,commands.MissingRequiredArgument):
      await ctx.send("`Error:` Captain There is missing in your input!")
      logs.write(f"[{dt_string}] MissingRequiredArgument : {error}"+"\n")

    if isinstance(error,commands.CommandNotFound):
      await ctx.send("`Error:` Captain! Command not found!")
      logs.write(f"[{dt_string}] CommandNotFound : {error}"+"\n")
    
    if isinstance(error,commands.BadArgument):
      await ctx.send("`Error:` Captain! There is something wrong in your input")
      logs.write(f"[{dt_string}] BadArgument : {error}"+"\n")

    if isinstance(error, commands.UserInputError):
      await ctx.send("`Error:` Captain! There is something wrong in your input")
      logs.write(f"[{dt_string}] UserInputError : {error}"+"\n")

    if isinstance(error, commands.BotMissingAnyRole):
      await ctx.send("`Error:` Captain! I don't have role permission to take action")
      logs.write(f"[{dt_string}] BotMissingAnyRole : {error}"+"\n")
    
    if isinstance(error, commands.ExtensionFailed):
      await ctx.send("`Error:` Captain! Extension Failed Error Found!")
      logs.write(f"[{dt_string}] ExtensionFailedError : {error}"+"\n")

    if isinstance(error, commands.CommandInvokeError):
      await ctx.send("`Error:` Captain! Invoke Error!")
      logs.write(f"[{dt_string}] CommandInvokeError : {error}"+"\n")

    logs.close

  

def setup(client):
  client.add_cog(error_handling(client))
