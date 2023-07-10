import discord
from discord.ext import commands
from command_list import general
import asyncio
from decouple import config

# get bot token from .env
bot_token = config('BOT_TOKEN')

# honorofic commands
intents = discord.Intents.default()
intents.message_content = True

# bot prefix
client = commands.Bot(command_prefix='!', intents=intents)

# remove default help command
client.remove_command('help')


@client.event
# bot status
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='GDSC USK'))


async def setup():
    # load cogs
    await client.add_cog(general(client))

asyncio.run(setup())

# bot token
client.run(bot_token) # type: ignore
