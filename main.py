import discord # Lets me start up a discord bot
from discord import app_commands as apc
from discord.ext import commands
from discord.ext.commands import has_permissions
import os # Secret variables
import random

from dotenv import load_dotenv # Loads the secret values

load_dotenv() # The () means I'm using the function

intents = discord.Intents.all()
intents.message_content = True

client = discord.Client(intents=intents, application_id=os.getenv('CLID'))
bot = commands.Bot(command_prefix="/", intents=intents)
token = os.getenv('BOT_TOKEN') or ""

@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"\nSynced {len(synced)} command(s)")  
    except Exception as e:
        print(f"\n{e}")
    finally:
        print("Bot is Online!")
        await bot.change_presence(activity=discord.Activity(
            type=discord.ActivityType.listening, name="/roll"
        ))

@bot.tree.command(
    name="roll",
    description="Roll the dice!"
)
@apc.choices(Dice=[
    apc.Choice(name="D6", value="6"),
    apc.Choice(name="D20", value="20")
])
async def roll(i: discord.Interaction, Dice: apc.Choice[str]):
    if Dice == "6":
        await i.response.send_message(f"{interaction.user.name} rolled a D6 and got a {str(random.randint(1, 6)}")
    elif Dice == "20":
        await i.response.send_message(f"{interaction.user.name} rolled a D20 and got a {str(random.randint(1, 20)}")
    

