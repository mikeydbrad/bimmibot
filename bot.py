import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return # enures we don't respond to self

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        
@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise


# loading .env file for the TOKEN key
from dotenv import load_dotenv
load_dotenv()

client.run(os.getenv('TOKEN'))