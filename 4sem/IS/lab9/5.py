import discord
from ds_bot import token


class HWBot(discord.Client):

    async def on_ready(self):
        channel = client.get_channel(970997313147375668)
        await channel.send("Привет! Я подключился и готов показать котика или собачку")

    async def on_message(self, message):
        if message.author == self.user:
            return
        if "собака" in message.content.lower():
            with open('dog.jpg', 'rb') as file:
                picture = discord.File(file)
                await message.channel.send(file=picture)
        elif "кот" in message.content.lower():
            with open('cat.jpg', 'rb') as file:
                picture = discord.File(file)
                await message.channel.send(file=picture)

client = HWBot()
client.run(token)
