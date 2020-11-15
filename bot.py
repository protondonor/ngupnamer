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


def dict_choice(d):
    return random.choice(list(d.values()))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!ngupname'):
        args = message.content.split()
        if len(args) > 1 and args[1] in langs.keys():
            response = ngupnames.ngupname(langs[args[1]])
        else:
            response = ngupnames.ngupname(dict_choice(langs))
        await message.channel.send(response)


client.run(TOKEN)
