import discord

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

client.run('NTM2MzM3NzMzMTk5NzI0NTY0.DyVZ_w.2ld9xQAnXpsB6rj3ovKG59KkX88')