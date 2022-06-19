from discord.ext.commands.errors import CommandNotFound, MissingRequiredArgument
from discord.ext import commands

class Manager(commands.Cog):
    def __init__(self, bot):
        """Manages the bot"""
        self.bot = bot


    @commands.Cog.listener() 
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Você não informou todos os argumentos necessários!")
        if isinstance(error, CommandNotFound):
            await ctx.send("Comando não encontrado!")
        else:
            raise error

def setup(bot):
    bot.add_cog(Manager(bot))
