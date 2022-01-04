import discord
from discord import Embed, File
from datetime import datetime

client = discord.Client()
bot_token = 'TOKEN HERE'

gadgets = {'!ขนมปังช่วยจำ': ['アンキパン', 'เป็นของวิเศษของโดราเอมอน เป็นของวิเศษที่เมื่อนำขนมปังแปะบนหนังสือและกินเข้าไป ก็จะจำเรื่องที่แปะในหนังสือได้ เป็นของวิเศษประเภทอาหาร ปรากฏครั้งแรกในตอนขนมปังช่วยจำเล่มที่ 2', 'เพียงนำขนมปังไปแปะบนหนังสือหน้าที่ต้องการจะจำและกินเข้าไปก็จะจำสิ่งแปะบนหน้านั้นๆได้ แต่ถ้าถ่ายออกสิ่งที่กินเข้าไปเพื่อจำนั้นก็จะหายไปหมด', 'https://doraemon.fandom.com/th/wiki/ขนมปังช่วยจำ', 'https://github.com/5hyfilm/mlsa-doraemon-gadget-discord-bot/blob/main/img/%E0%B8%82%E0%B8%99%E0%B8%A1%E0%B8%9B%E0%B8%B1%E0%B8%87%E0%B8%8A%E0%B9%88%E0%B8%A7%E0%B8%A2%E0%B8%88%E0%B8%B3.png?raw=true'],
           '!คอปเตอร์ไม้ไผ่': ['タケコプター', 'ประวัติของคอปเตอร์ไม้ไผ่แสดงได้ให้เห็นในตอน โนบิตะล่าโจรปริศนาในพิพิธภัณฑ์ของวิเศษ โดยเล่าว่าคอปเตอร์ไม้ไผ่รุ่นแรกมีขนาดใหญ่มาก เป็นการผสมผสานกันระหว่างใบพัดของเฮลิคอปเตอร์และเครื่องยนต์ขนาดกลาง ในรุ่นแรกจะใช้สวมทั้งตัวและมีสามใบพัด ใบพัดเล็กอีกสอง และใบพัดใหญ่หนึ่งอัน และต่อๆมาก็มีขนาดเริ่มเล็กลงเรื่อยๆ จนมาถึงรุ่นที่สี่ จะเป็นแบบหมวกมีใบพัดติดที่หัว และพัฒนาเรื่อยมาจนมาเป็นคอปเตอร์ไม้ไผ่ในปัจจุบันที่มีขนาดเล็กกระทัดรัดพกพาง่าย', 'เพียงแค่กดปุ่มที่ฐานของคอปเตอร์ไม้ไผ่ ก็จะสามารถบินได้อย่างอิสระ โดยการเคลื่อนที่บินไปมาว่าจะเลี้ยวไปทางไหน ผู้ใช้จะต้องคิดว่าจะเลี้ยวซ้าย เลี้ยวขวา หรือตรงไป เมื่อคิดแล้วมันก็จะพาเลี้ยวไปยังอัตโนมัติ', 'https://doraemon.fandom.com/th/wiki/คอปเตอร์ไม้ไผ่', 'https://github.com/5hyfilm/mlsa-doraemon-gadget-discord-bot/blob/main/img/%E0%B8%84%E0%B8%AD%E0%B8%9B%E0%B9%80%E0%B8%95%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B9%84%E0%B8%A1%E0%B9%89%E0%B9%84%E0%B8%9C%E0%B9%88.jpeg?raw=true'],
           '!ไทม์แมชชีน': ['タイムマシン', 'เป็นของวิเศษที่ปรากฎบ่อยๆในหลายๆตอนของโดราเอมอน ใช้ย้อนเวลาไปยังยุคอดีต หรือเดินทางไปยังอนาคตได้ โดยจะเดินทางผ่านอุโมงค์กาลเวลา ที่มีลักษณะเป็นห้วงมิติที่มีนาฬิกาลอยอยู่รอบๆ', 'ใช้สำหรับเดินทางข้ามกาลเวลา หรือย้อนเวลาได้ ไม่ว่าจะเป็นการเดินทางไปยังโลกอนาคต หรือย้อนไปยังยุคอดีต สามารถไปได้ด้วยการระบุช่วงเวลา สถานที่ที่ต้องการไปได้ โดยไทม์แมชชีนจะเดินทางผ่านอุโมงค์กาลเวลาใน Stand By Me โดราเอมอน เพื่อนกันตลอดไป ได้ระบุไว้ว่า หากตกลงไปในอุโมงค์กาลเวลา คนที่ตกลงไปจะหายไปตลอดกาล หรือก็คือคนๆนั้นจะไม่เคยมีตัวตนอยู่จริงๆเลย', 'https://doraemon.fandom.com/th/wiki/ไทม์แมชชีน', 'https://github.com/5hyfilm/mlsa-doraemon-gadget-discord-bot/blob/main/img/%E0%B9%84%E0%B8%97%E0%B8%A1%E0%B9%8C%E0%B9%81%E0%B8%A1%E0%B8%8A%E0%B8%8A%E0%B8%B5%E0%B8%99.jpeg?raw=true'],
           '!ประตูไปที่ไหนก็ได้': ['どこでもドア', 'ประตูไปที่ไหนรุ่นแรกมีขนาดที่ใหญ่โตมโหฬารมาก มีขนาดใหญ่เทียบเท่ากับบ้านสามชั้นเลย จนกระทั่งได้มีการพัฒนามาเรื่อย ๆ ซึ่งประตูไปที่ไหนก็ได้รุ่นต่าง ๆ ได้ถูกจัดแสดงไว้ที่พิพิธภัณฑ์ของวิเศษ และพัฒนาต่อเรื่อยมาจนกลายเป็นประตูไปที่ไหนก็ได้แบบที่เห็นโดราเอมอนนำมาใช้บ่อย ๆ ก็คือประตูบานสีชมพูขนาดเล็กดีไซน์เรียบง่ายนั่นเอง', 'เมื่อบอกสถานที่ที่อยากไปกับประตูนี่แล้ว ก็จะสามารถไปได้ทุกที่บนโลก แต่หากไม่ใส่แผนที่โลกลงไป ก็จะไม่สามารถไปที่ไหนได้เลย เช่นเดียวกับในตอน โดราเอมอน: ไดโนเสาร์ของโนบิตะ ที่ทุกคนย้อนกลับไปยังยุคครีเทเชียส แต่ไม่สามารถใช้ประตูไปที่ไหนก็ได้ในยุคนั้นได้เลย ก็เพราะไม่ได้ใส่แผนที่โลกในยุคดึกดำบรรพ์เอาไว้', 'https://doraemon.fandom.com/th/wiki/ประตูไปที่ไหนก็ได้', 'https://raw.githubusercontent.com/5hyfilm/mlsa-doraemon-gadget-discord-bot/main/img/%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%95%E0%B8%B9%E0%B9%84%E0%B8%9B%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B9%84%E0%B8%AB%E0%B8%99%E0%B8%81%E0%B9%87%E0%B9%84%E0%B8%94%E0%B9%89.jpeg'],
           '!ไฟฉายขยายส่วน': ['ビッグライト', 'เป็นของวิเศษชนิดไฟฉายที่ขยายวัตถุที่ถูกแสงส่อง ตรงข้ามกับไฟฉายย่อส่วนที่ทำให้วัตถุเล็กลง', 'เมื่อฉายไฟไปที่วัตถุ จะทำให้วัตถุใหญ่ขึ้น ยิ่งฉายนานยิ่งใหญ่ขึ้นมาก', 'https://doraemon.fandom.com/th/wiki/ไฟฉายขยายส่วน', 'https://github.com/5hyfilm/mlsa-doraemon-gadget-discord-bot/blob/main/img/%E0%B9%84%E0%B8%9F%E0%B8%89%E0%B8%B2%E0%B8%A2%E0%B8%82%E0%B8%A2%E0%B8%B2%E0%B8%A2%E0%B8%AA%E0%B9%88%E0%B8%A7%E0%B8%99.png?raw=true'],
           '!ไฟฉายย่อส่วน': ['スモールライト', 'แสงย่อส่วน เป็นของวิเศษชนิดไฟฉายที่ย่อวัตถุที่ถูกแสงส่อง', 'เมื่อฉายไฟไปที่วัตถุ จะทำให้วัตถุเล็กลง ยิ่งส่องนานยิ่งเล็กลงมาก', 'https://doraemon.fandom.com/th/wiki/ไฟฉายย่อส่วน', 'https://github.com/5hyfilm/mlsa-doraemon-gadget-discord-bot/blob/main/img/%E0%B9%84%E0%B8%9F%E0%B8%89%E0%B8%B2%E0%B8%A2%E0%B8%A2%E0%B9%88%E0%B8%AD%E0%B8%AA%E0%B9%88%E0%B8%A7%E0%B8%99.gif?raw=true']}

@client.event
async def on_ready( ):
    print("Doraemon's Gadgets bot is ready to use")
    await client.change_presence(status=discord.Status.online, activity=discord.Game('!gadgets'))

@client.event
async def on_message(message):
    if message.content == 'Hi Doraemon':
        await message.channel.send('สวัสดีท่านสมาชิก')

    elif message.content == '!gadgets':
        embed = Embed(title="Doraemon's Gadget lists", description='รายชื่อของวิเศษของโดราเอม่อนทั้งหมด', color=0xFF0000, timestamp=datetime.utcnow())
        gadgets_lst = []
        for gadget in gadgets:
            gadgets_lst.append((gadget[1:], gadgets[gadget][0], False))
        for name, value, inline in gadgets_lst:
            embed.add_field(name=name, value=value, inline=False)
        await message.channel.send(embed=embed)

    elif message.content in gadgets:
        target = gadgets[message.content]
        embed = Embed(title=str(message.content)[1:], description=target[0], color=0xFF0000, timestamp=datetime.utcnow())
        fields = [('INFORMATION', target[1], False),
                  ('HOW TO USE', target[2], False),
                  ('CREDIT', target[3], False)]
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=False)
        embed.set_image(url=target[4])
        await message.channel.send(embed=embed)

client.run(bot_token)