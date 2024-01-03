import discord
import os
from keep_alive import keep_alive

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    # 送信者がbotである場合は弾く
    if message.author.bot:
        return 
    # メッセージの本文が 鳴いて だった場合
    if message.content == "鳴いて":
        # 送信するメッセージをランダムで決める
        content = "aaaa"
        # メッセージが送られてきたチャンネルに送る
        await message.channel.send(content)
    elif message.content == "おはよう":
        await message.channel.send("おはよう！！")

TOKEN = os.getenv("DISCORD_TOKEN")
# Web サーバの立ち上げ
keep_alive()
client.run(TOKEN)