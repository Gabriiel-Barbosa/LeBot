import requests
from discord.ext import commands

class Crypto(commands.Cog):
    def __init__(self, bot):
        """Works with Crypto"""
        self.bot = bot

    #Esse comando é para pegar o valor da cripto moeda
    @commands.command(
        help= "Verifica o preço de um par na bianance. Ex: !binance  btc usd" 
    )
    async def binance(self, ctx, coin, base ):
        """Verifica o preço de um par na bianance"""
        try:
            response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}")
            data = response.json()
            price= data.get("price")

            if price:
                await ctx.send(f"O preço de {coin} em {base} é {price}")
            else:
                await ctx.send("Não foi possível encontrar o preço")
        except Exception as error:
            await ctx.send(f"Ocorreu algum erro. Tente novamente mais tarde!")
            
def setup(bot):
    bot.add_cog(Crypto(bot))

