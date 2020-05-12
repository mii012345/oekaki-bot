import discord
import re
import oekaki
import json

json_open = open('id.json', 'r')
json_load = json.load(json_open)

Token = json_load['token']

client = discord.Client()
oemori = oekaki.Oekaki(json_load['user'], json_load['pass'])

admin = client.get_user("mii#0001")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    activity = discord.Game(name="!start [難易度]で開始")
    await client.change_presence(activity=activity)

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if_level = re.compile(u"!start (.+)").search(message.content)

    if if_level:
        await message.channel.send('レベル%sのお絵描き始まるよ！'%if_level.group(1))
        await message.channel.send('絵を書く人にDMするよ。画面共有と視聴の準備をしてね。')
        try:
            oemori.start_oekaki()
            oemori.get_word(if_level.group(1))
        except:
            await message.channel.send('難易度が正しくないか、ワードリストが空だよ。')
            await message.channel.send('!add [ワード] [難易度]でワードを追加してね。')

    if_add = re.compile(u"!add (.+) (.+)").search(message.content)
    if if_add:
        try:
            oemori.add_word(if_add.group(1), if_add.group(2))
            await message.channel.send('%sをレベル%sで追加しました！'%(if_add.group(1), if_add.group(2)))
        except:
            await message.channel.send('エラー:追加できませんでした')
    
    if message.content == "!debug":
        user = client.get_user(message.author.id)
        await user.send("aaa")
        oemori.get_word(1)

client.run(Token)