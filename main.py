import discord
import os

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
  print('ログインしました')

@client.event
async def on_message(message):
  print(message.content)
  if message.author.bot:
    return
  if 'https://x.com' in message.content:
    vx_url = message.content.replace('x.com', 'vxtwitter.com')
    vx_url_str = str(vx_url)
    await message.channel.send(vx_url_str)
    return
  else:
    print(message.content)
    await message.channel.send("not in")
    return


TOKEN = os.getenv("DISCORD_TOKEN")
client.run(TOKEN)