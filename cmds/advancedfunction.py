from discord.ext import commands
from Bot1.code.classes import Cog_Extension
import discord
import datetime
import http.client
import hashlib
import urllib
import random
import json
import os
import requests
import urllib.request
import urllib.error
import base64
import cv2

with open('setting.json', mode='r', encoding='utF8') as jFile:
    j = json.load(jFile)


class Advanced_Function(Cog_Extension):



    @commands.command()
    async def translator(self, ctx, language, *,sentence):
        appid = j['translator_appid']
        secretKey = j['translator_secretKey']

        myurl = '/api/trans/vip/translate'

        fromLang = 'auto'  # Your language
        toLang = language  # Translate
        salt = random.randint(1, 10000)
        q = sentence
        sign = appid + q + str(salt) + secretKey
        sign = hashlib.md5(sign.encode()).hexdigest()
        myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign

        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)
        final_result = result['trans_result']
        key_result = final_result[0]

        embed = discord.Embed(title="Translation", description='Changing Language to: ' + language,
                              color=0xff80ff, timestamp=datetime.datetime.now())
        embed.add_field(name='Input Language: ', value=q, inline=False)
        embed.add_field(name='After the translation: ', value=key_result["dst"], inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def emotion(self, ctx):

        request_url = j["Affective_disposition_analysis_url"]

        access_token = j['access_TOKEN']
        text = ctx.message.content
        params = {'access_token': access_token}
        payload = json.dumps({'text': text})
        headers = {'Content-Type': 'application/json; charset=UTF-8'}
        response = requests.post(url=request_url, params=params, data=payload, headers=headers).json()
        dict_to_list = response['items']
        out_list = dict_to_list[0]
        positive = out_list['positive_prob']
        negative = out_list['negative_prob']
        confidence = out_list['confidence']
        embed = discord.Embed(title="Emotion Test", description='WOW! Your mood is: ',
                              color=0xff80ff, timestamp=datetime.datetime.now())
        embed.add_field(name='The optimistic index: ', value=positive, inline=False)
        embed.add_field(name='The negative index: ', value=negative, inline=False)
        embed.add_field(name='confidence index: ', value=confidence, inline=False)
        await ctx.send(embed=embed)







def setup(bot):
    bot.add_cog(Advanced_Function(bot))