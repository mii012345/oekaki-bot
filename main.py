import discord
import re
import oekaki
import json

json_open = open('id.json', 'r')
json_load = json.load(json_open)

Token = json_load['token']

client = discord.Client()
oemori = oekaki.Oekaki(json_load['user'], json_load['pass'])

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == "スタート":
        await message.channel.send('お絵描き始まるよ')
    if_add = re.compile(u"!add (.+) (.+)").search(message.content)
    if if_add:
        try:
            oemori.add_word(if_add.group(1), if_add.group(2))
            await message.channel.send('%sを%sで追加しました！'%(if_add.group(1), if_add.group(2)))
        except:
            await message.channel.send('エラー:追加できませんでした')

client.run(Token)