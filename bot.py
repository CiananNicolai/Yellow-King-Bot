import discord
from marko import *

print(discord.__version__)

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$Marko'):
     await message.channel.send(BibleLovecraftGrim())

client.run(os.getenv('TOKEN'))