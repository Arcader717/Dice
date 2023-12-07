import discord # Lets me start up a discord bot
from discord import app_commands as apc
from discord.ext import commands
from discord.ext.commands import has_permissions
import os # Secret variables
import random

intents = discord.Intents.all()
intents.message_content = True

client = discord.Client(intents=intents, application_id="1182093023274868777")
bot = commands.Bot(command_prefix="/", intents=intents)
token = os.environ['BOT_TOKEN'] or ""

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
@apc.choices(dice=[
    apc.Choice(name="D6", value="6"),
    apc.Choice(name="D20", value="20")
])
async def roll(i: discord.Interaction, dice: apc.Choice[str]):
    r = i.response
    await r.send_message(f"{i.user.mention} rolled a D{dice.value} and got a ***{str(random.randint(1, int(dice.value)))}***") # Simulates a Dice
    

@bot.tree.command(
    name="create",
    description="Create a character"
)
@apc.describe(name="The name of your character")
@apc.choices(type=[
    apc.Choice(name="Fighter", value="f"),
    apc.Choice(name="Ranger", value="r"),
    apc.Choice(name="Thief", value="t"),
    apc.Choice(name="Guardian", value="g"),
    apc.Choice(name="Bard", value="b"),
    apc.Choice(name="Wizard", value="w"),
    apc.Choice(name="Hero", value="h")
])
async def create(i: discord.Interaction, name: str, type: apc.Choice[str]):
    r = i.response
    await r.send_message(f"{i.user.mention} made a new **{str(type.name)}** named ***{name}***")

if __name__ == "__main__":
    token = os.environ['BOT_TOKEN']
    bot.run(token)