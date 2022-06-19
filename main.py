import discord
from discord.ext import commands
from decouple import config

bot = commands.Bot("!")



bot.load_extension("commands.talks")
bot.load_extension("commands.finance")
TOKEN = config("TOKEN")
bot.run(TOKEN)