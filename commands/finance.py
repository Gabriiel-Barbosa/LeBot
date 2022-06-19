from urllib import response
import requests
from discord.ext import commands

class Finance(commands.Cog):
    def __init__(self, bot):
        """Works with finace"""
        self.bot = bot

    #Esse comando é para pegar o valor da cripto moeda
    @commands.command( help= "Verifica o preço de um par na binance (!crypto btc usd)" )
    async def crypto(self, ctx, coin, base ):
        """Verifica o preço de um par na binance"""
        try:
            response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}")
            data = response.json()
            price= data.get("price")

            if price:
                await ctx.send(f"O preço de {coin} em {base} NA BINANCE é {price}")
            else:
                await ctx.send("Não foi possível encontrar o preço")
        except Exception as error:
            await ctx.send(f"Ocorreu algum erro. Tente novamente mais tarde!")
    

    @commands.command( help= "Retorna a cotação do dolar em real (!dolar)" )       
    async def dolar(self, ctx):
        """Cotação do dolar para real"""
        try:
            response = requests.get("https://economia.awesomeapi.com.br/all/USD-BRL")
            price = response.json()
            if price:
                await ctx.send(f"Moeda:" + price["USD"]["name"])
                await ctx.send(f"Data: " + price ["USD"]["create_date"])
                await ctx.send(f"O valor atual do dolar é {price['USD']['bid']}")
            else:
                await ctx.send("Não foi possível encontrar a cotação")
        except Exception as error:
            await ctx.send(f"Ocorreu algum erro. Tente novamente mais tarde!")


   

def setup(bot):
    bot.add_cog(Finance(bot))

