import discord
from discord.ext import commands
import json
from Bot1.code.classes import Cog_Extension
with open('setting.json', mode='r', encoding='utF8') as jFile:
    j = json.load(jFile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(j['channel']))
        await channel.send(f'{member} join!')

    @commands.Cog.listener()
    async def on_member_leave(self, member):
        channel = self.bot.get_channel(int(j['channel']))
        await channel.send(f'{member} Leave!')

    @commands.Cog.listener()
    async def on_message(self, message):
        #Keyword = ['Good morning', 'Good evening', 'Good afternoon', 'Hi', 'Hello']
        if message.content == 'Good evening' and message.author != self.bot.user:
            await message.channel.send('hi')



def setup(bot):
    bot.add_cog(Event(bot))