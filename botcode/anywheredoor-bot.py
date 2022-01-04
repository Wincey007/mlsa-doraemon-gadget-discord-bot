import discord
from discord import Embed, File
from datetime import datetime

client = discord.Client()
bot_token = 'TOKEN HERE'

@client.event
async def on_ready( ):
    print("Doraemon's Gadgets bot is ready to use")
    await client.change_presence(status=discord.Status.online, activity=discord.Game('อั๊ง อัง อัง'))

@client.event
async def on_message(message):
    if message.content == 'Hi Doraemon':
        await message.channel.send('สวัสดีท่านสมาชิก')

    if message.content == 'ประตูไปที่ไหนก็ได้':
        embed = Embed(title='ประตูไปที่ไหนก็ได้', description='どこでもドア', color=0xFF0000, timestamp=datetime.utcnow())
        fields = [('INFORMATION', 'ประตูไปที่ไหนรุ่นแรกมีขนาดที่ใหญ่โตมโหฬารมาก มีขนาดใหญ่เทียบเท่ากับบ้านสามชั้นเลย จนกระทั่งได้มีการพัฒนามาเรื่อย ๆ ซึ่งประตูไปที่ไหนก็ได้รุ่นต่าง ๆ ได้ถูกจัดแสดงไว้ที่พิพิธภัณฑ์ของวิเศษ และพัฒนาต่อเรื่อยมาจนกลายเป็นประตูไปที่ไหนก็ได้แบบที่เห็นโดราเอมอนนำมาใช้บ่อย ๆ ก็คือประตูบานสีชมพูขนาดเล็กดีไซน์เรียบง่ายนั่นเอง', False),
                  ('HOW TO USE', 'เมื่อบอกสถานที่ที่อยากไปกับประตูนี่แล้ว ก็จะสามารถไปได้ทุกที่บนโลก แต่หากไม่ใส่แผนที่โลกลงไป ก็จะไม่สามารถไปที่ไหนได้เลย เช่นเดียวกับในตอน โดราเอมอน: ไดโนเสาร์ของโนบิตะ ที่ทุกคนย้อนกลับไปยังยุคครีเทเชียส แต่ไม่สามารถใช้ประตูไปที่ไหนก็ได้ในยุคนั้นได้เลย ก็เพราะไม่ได้ใส่แผนที่โลกในยุคดึกดำบรรพ์เอาไว้', False),
                  ('CREDIT', 'https://doraemon.fandom.com/th/wiki/ประตูไปที่ไหนก็ได้', False)]
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=False)
        embed.set_image(url='https://raw.githubusercontent.com/5hyfilm/mlsa-doraemon-gadget-discord-bot/main/img/%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%95%E0%B8%B9%E0%B9%84%E0%B8%9B%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B9%84%E0%B8%AB%E0%B8%99%E0%B8%81%E0%B9%87%E0%B9%84%E0%B8%94%E0%B9%89.jpeg')
        await message.channel.send(embed=embed)

client.run(bot_token)