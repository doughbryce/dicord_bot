# This example requires the 'message_content' intent.

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('OTk1ODIwMjg2NjA5OTg1NjA5.G8QGm8.gkbgwMGTjGSj-3V7C0BtTsCXyyr8Zt2mVhgZ84')
