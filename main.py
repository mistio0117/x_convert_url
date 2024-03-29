import discord
import os

# ここを変更するとメッセージが受け取れなくなる
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
  print('ログインしました')

@client.event
async def on_message(message):
  print(message.content)
  # Botのメッセージの場合は何もしない
  if message.author.bot:
    return
  # TODO:wtwitter.comの場合に対応できていない。
  # main
  if 'https://x.com' in message.content:
    vx_url = message.content.replace('x.com', 'vxtwitter.com')
    vx_url_str = str(vx_url)
    await message.channel.send(vx_url_str)
    return
  else:
    print(message.content)
    return

TOKEN = os.getenv("DISCORD_TOKEN")
client.run(TOKEN)