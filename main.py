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
    if message.author.bot:
        return
    
    if message.content.find('https:\/\/x.com'):
        vx_url = message.content
        vx_url = vx_url.replace('x.com', 'vxtwitter.com')
        await message.channel.send("in!!")
    else:
        await message.channel.send("not in!!")

TOKEN = os.getenv("DISCORD_TOKEN")
# Web サーバの立ち上げ
keep_alive()
client.run(TOKEN)