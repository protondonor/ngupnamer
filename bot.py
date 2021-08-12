import os
import random

import discord
from dotenv import load_dotenv

import conjugamatron
import ngupnames
import semshifter

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

    if message.content.startswith('!conjugate'):
        args = message.content.split()
        if len(args) < 3:
            response = 'Conjugate what?'
        else:
            response = conjugamatron.conjugate(args[1], args[2:])
        await message.channel.send(response)

    if message.content.startswith('!semshifter'):
        args = message.content[12:]
        response = semshifter.semshift(args)
        await message.channel.send(response)


client.run(TOKEN)
