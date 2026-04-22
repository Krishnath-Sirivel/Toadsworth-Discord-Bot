import discord
import asyncio
import os


TOKEN = os.getenv("TOKEN")

intents = discord.Intents(messages=True, guilds=True)
intents.reactions = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    # ignore your own bot
    if message.author == client.user:
        return
      
    if message.content.lower().startswith('i suggest') and message.channel.id == 1064671109158535230:
        response = await message.channel.send('I will think about it. Thank you for your suggestion!')
        thumbsUp = '\N{THUMBS UP SIGN}'
        thumbsDown = '\N{THUMBS DOWN SIGN}'
        await message.add_reaction(thumbsUp)
        await message.add_reaction(thumbsDown)
        await asyncio.sleep(7)
        await response.delete()
        return



client.run(TOKEN)
