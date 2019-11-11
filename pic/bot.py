import youtube_dl
import discord
from discord.ext import commands
import os
import json



with open('setting.json', mode='r', encoding='utF8') as jFile:
    j = json.load(jFile)


# ctx = context(上下文)
# A:hi(上文) {使用者,id,所在服务器,所在频道}
# B:hello(下文)

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(">> Bot is online<<")
    print('------')


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded{extension} done.')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Un - Loaded{extension} done.')


@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re - Loaded{extension} done.')


for Filename in os.listdir('./cmds'):
    if Filename.endswith('.py'):
        bot.load_extension(f'cmds.{Filename[:-3]}')

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Exclusive robot", description="Nicest bot there is ever.", color=0xeee657)

    embed.add_field(name="Author", value="Spike")

    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    await ctx.send(embed=embed)


@bot.command()
async def join(self, ctx, *, channel: discord.VoiceChannel):
    """Joins a voice channel"""

    if ctx.voice_client is not None:
        return await ctx.voice_client.move_to(channel)

    await channel.connect()

if __name__ == "__main__":
    bot.run(j['TOKEN'])
