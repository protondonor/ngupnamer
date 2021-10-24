import os
import random

import discord
from dotenv import load_dotenv

import conjugamatron
import ngupnames
import semshifter
import logging

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
logging.basicConfig(level=logging.INFO)

client = discord.Client()

langs = ngupnames.init_langs()


def dict_choice(d):
    return random.choice(list(d.values()))


def chunk_response(text: str) -> list:
    words = iter(text.split(', '))
    lines, current = [], next(words)
    for word in words:
        if len(current) + 2 + len(word) > 2000:
            lines.append(current)
            current = word
        else:
            current += ", " + word
    lines.append(current)
    return lines


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!ngupname'):
        print('starting ngupname')
        args = message.content.split()
        if len(args) > 1 and args[1] in langs.keys():
            response = ngupnames.ngupname(langs[args[1]])
        else:
            response = ngupnames.ngupname(dict_choice(langs))
        await message.channel.send(response)

    if message.content.startswith('!conjugate'):
        args = message.content.split()
        if len(args) < 3:
            response = conjugamatron.usage
        else:
            response = conjugamatron.conjugate(args[1], args[2:])
        await message.channel.send(response)

    if message.content.startswith('!semshift'):
        print('starting semshifter')
        async with message.channel.typing():
            try:
                args = ' '.join(message.content.split(' ')[1:])
                response = list(semshifter.semshift(args))
                response = ', '.join(response)
                response = chunk_response(response)
                for r in response:
                    await message.channel.send(r)
            except Exception as e:
                await message.channel.send('There was an error! check your logs')
                raise e

    if message.content.startswith('!reverse'):
        print('starting semshifter in reverse gear')
        async with message.channel.typing():
            try:
                args = ' '.join(message.content.split(' ')[1:])
                response = list(semshifter.reverse(args))
                response = ', '.join(response)
                response = chunk_response(response)
                for r in response:
                    await message.channel.send(r)
            except Exception as e:
                await message.channel.send('There was an error! check your logs')
                raise e

client.run(TOKEN)