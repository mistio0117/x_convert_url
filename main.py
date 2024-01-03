import discord
import os
from keep_alive import keep_alive

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    # emoji ="👍"
    # await message.add_reaction(emoji)
    # await message.channel.send("おはよう！！")
    if message.content.find('https:\/\/x.com'):
        vx_url = message.content.replace('x.com', 'vxtwitter.com')
        await message.channel.send(vx_url)

TOKEN = os.getenv("DISCORD_TOKEN")
# Web サーバの立ち上げ
keep_alive()
client.run(TOKEN)