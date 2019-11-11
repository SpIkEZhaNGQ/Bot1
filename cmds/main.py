from discord.ext import commands
from Bot1.code.classes import Cog_Extension
import discord
import datetime


class Main(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)' )

    @commands.command()
    async def add(self, ctx, a: int, b: int):
        await ctx.send(a + b)

    @commands.command()
    async def multiply(ctx, a: int, b: int):
        await ctx.send(a * b)

    @commands.command()
    async def division(ctx, a: int, b: int):
        await ctx.send(int(a / b))

    @commands.command()
    async def hi(self, ctx):
        await ctx.send('123')


    @commands.command()
    async def em(self, ctx):
        embed = discord.Embed(title= "About", url="https://ai.baidu.com/docs/TTS-API/top", description='description',
        color=0xff80ff, timestamp = datetime.datetime.now())
        embed.set_thumbnail(url="https://ai.baidu.com/docs/TTS-API/top")
        embed.add_field(name=1, value=11, inline=False)
        embed.add_field(name=11, value=11, inline=False)
        embed.add_field(name=111, value=111, inline=True)
        embed.add_field(name=1111, value=1111, inline=True)
        embed.set_footer(text=123123)
        await ctx.send(embed=embed)






def setup(bot):
    bot.add_cog(Main(bot))