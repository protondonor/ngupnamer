import os

import discord
import random
import ngupnames
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

langs = ngupnames.init_langs()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # ngupnames = [
    #     'Ŋụlẹrạ Kułujiko',
    #     'Jń Tọnụldạh',
    #     'Mirèñą Zamřani Zįʼąząļì Liì',
    #     'Rra³ Zį²ʼą¹zą² Mbi³ Ti¹rú³',
    #     'Hé³xi² Ñą¹³mba³ Se²',
    #     'Ra Sịyịhạạsạ Muwi Tirukkoxał',
    #     'Ñžeз Ra Sịyịhạạsạ Ŋokun Luukwa Ñaƞ',
    #     'Sạmlạnị Sịyịhạạsạ Ra Jakwarał Ŋoruyalayex'
    # ]

    if message.content == '!ngupname':
        response = ngupnames.ngupname(langs)
        await message.channel.send(response)


client.run(TOKEN)
