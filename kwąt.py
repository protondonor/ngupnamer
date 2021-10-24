import random

# documentation of the game:
# https://docs.google.com/document/d/1EJ1G7npctNtCNi9wJ0B6Frx2rSIIZPnq7zwBf4Tv4Fg/edit

# noinspection NonAsciiCharacters
pemehąn = {
    'oyo': 'take {} token{} from the pot',
    'rahi': 'put {} token{} into the pot',
    'řąha': 'give {} token{} to the player on your right',
    'poryą': 'take {} token{} from the player on your right',
    'xahąx': 'everyone hand all their tokens to the player on their right',
    'zerą': 'do nothing'
}

# noinspection NonAsciiCharacters
peząhąn = {
    'mwi •': '1',
    'řą ••': '2',
    'łi ⛬': '3',
    'łam ◆': 'half of the',
    'nanarą ▲': 'all of the',
    'pełinat': 'no'
}

def plural(i):
    return "s" if i != '1' else ""

def roll():
    action = random.choice(list(pemehąn.keys()))
    number = random.choice(list(peząhąn.keys()))

    if action in ['xahąx', 'zerą']:
        return f'{action}\n{pemehąn[action]}'

    return f'{action} {number}\n' + pemehąn[action].format(peząhąn[number], plural(peząhąn[number]))