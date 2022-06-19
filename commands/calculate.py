from urllib import response


from urllib import response
import requests
from discord.ext import commands

class Calculate(commands.Cog):
    def __init__(self, bot):
        """A lot of useful commands for calculating"""
        self.bot = bot



    @commands.command(name = "calcular", help = "Calcula expressões matemáticas(!calcular)")
    async def calculate_expession(self, ctx, *expression):
        try:
            expression = "".join(expression)
            response = eval(expression)
            await ctx.send("A resposta é: " +  str(response))
        except Exception as error:
            await ctx.send(f"Ocorreu algum erro. Tente novamente mais tarde!")
def setup(bot):
    bot.add_cog(Calculate(bot))