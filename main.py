import os
from random import choice

import discord
from discord.ext import commands
from dotenv import load_dotenv
import requests

from get_facts import get_facts


load_dotenv(verbose=True)
API_KEY = os.getenv('API_KEY')

facts = get_facts()

bot = commands.Bot(command_prefix='!')
@bot.command()
async def cat(ctx):
    await ctx.send(choice(facts))

@bot.command()
async def meow(ctx):
    json_data = requests.get('https://api.thecatapi.com/v1/images/search').json()
    await ctx.send(json_data[0]['url'])

print('Running the bot...')
bot.run(API_KEY)
