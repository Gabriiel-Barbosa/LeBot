from discord.ext import commands
class Talks(commands.Cog):
    def __init__(self, bot):
        """Talks with user"""
        self.bot = bot
    #Essecomando é só pra ter uma mensagem de boas vindas
    @commands.command(name="oi", help = "Envia um oi e orienta o usuário")
    async def send_oi(self, ctx):

        name = ctx.author.name

        response = f"Olá {name}. Para saber os comandos disponíveis, digite !help"  

        await ctx.send(response)

def setup(bot):
    bot.add_cog(Talks(bot))

