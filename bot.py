import discord
from discord import Embed, File
from datetime import datetime

client = discord.Client()

@client.event
async def on_ready( ):
    print('bot is ready to use')
    # c = get_channel('927601384629628960')
    # await c.send('bot is ready to use')

@client.event
async def on_message(message):
    # if message.author == client.user:
    #     return 'hi'
    if message.content == 'Woody' or message.content == 'woody':
        embed = Embed(title='Woody', description='Cowboy', color=0xFF0000, timestamp=datetime.utcnow())
        fields = [
                    ('Name', 'Value', True),
                    ('information', 'vc', True),
                    ('X', 'Y', True)
                ]
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=True)
        embed.set_author(name='BOT')
        embed.set_image(url='https://github.com/5hyfilm/mlsa-toystory-discord-bot/blob/main/img/woody.jpeg')
        await message.channel.send(embed=embed)




    # if message.content == 'Hi bot':
    #     await message.channel.send('Greetings sir!')

    # await message.channel.send('Sawasdee')

# client.run('OTI3NjAxMzg0NjI5NjI4OTYw.YdMmHA.1PZcvKmzXOntEuOIYwJjZXgkiTw')