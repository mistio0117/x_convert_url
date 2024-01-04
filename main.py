import discord
import os
from keep_alive import keep_alive

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    channel_name = message.channel
    if message.author.bot:
        return
    if message.content.find('x.com'):
        vx_url = message.content.replace('x.com', 'vxtwitter.com')
        vx_url_str = str(vx_url)
        await channel_name.send(vx_url_str)
    else:
        await channel_name.send("not in!!")

TOKEN = os.getenv("DISCORD_TOKEN")
# Web サーバの立ち上げ
keep_alive()
client.run(TOKEN)