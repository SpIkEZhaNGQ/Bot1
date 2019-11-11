from discord.ext import commands
from Bot1.code.classes import Cog_Extension
import json
import youtube_dl
import http.client

players={}

with open('setting.json', mode='r', encoding='utF8') as jFile:
    j = json.load(jFile)

class React(Cog_Extension):

    @commands.command()
    async def cat(self, ctx):
        await ctx.send("https://pic1.zhimg.com/v2-5115ee9fc07e3cf02e3be14464275beb_1200x500.jpg")

    @commands.command()
    async def greet(self, ctx):
        await ctx.send(":smiley: :wave: Hello, there!")

    @commands.command()
    async def play(self, ctx, music):
        server = ctx.message.server
        voice_cline = http.client.vioce_bot_in(server)
        player = await voice_cline.creat_youtubeDL_player(music)
        players[server.id] = player
        player.start()



def setup(bot):
    bot.add_cog(React(bot))