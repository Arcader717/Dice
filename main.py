import discord # Lets me start up a discord bot
from discord import app_commands as apc
from discord.ext import commands
from discord.ext.commands import has_permissions
import os # Secret variables
import random

# from data.classes import Class, Fighter, Ranger, Thief, Guardian, Bard, Wizard, Hero
from alpha import alpha_id

intents = discord.Intents.all()
intents.message_content = True

client = discord.Client(intents=intents, application_id="1182093023274868777")
bot = commands.Bot(command_prefix="/", intents=intents)
token = os.environ['BOT_TOKEN'] or ""

def is_alpha():
    def predicate(i: discord.Interaction):
        if i.user.id in alpha_id:
            return True
        else:
            return False
    return apc.check(predicate)




class ocreateClassView(discord.ui.View):
    def __init__(self, name):
        super().__init__(timeout=None)
        self.name = name

    @discord.ui.button(label="Fighter", style=discord.ButtonStyle.secondary)
    async def fighter(self, i: discord.Interaction, b: discord.ui.Button):
        r = i.response
        await r.edit_message(content=f"{i.user.mention} made a new **Fighter** named ***{self.name}***", embed=None, view=None)

    @discord.ui.button(label="Ranger", style=discord.ButtonStyle.secondary)
    async def ranger(self, i: discord.Interaction, b: discord.ui.Button):
        r = i.response
        await response.edit(f"{i.user.mention} made a new **Ranger** named ***{self.name}***")

    @discord.ui.button(label="Thief", style=discord.ButtonStyle.secondary)
    async def thief(self, i: discord.Interaction, b: discord.ui.Button):
        r = i.response
        await response.edit(f"{i.user.mention} made a new **Thief** named ***{self.name}***")
    
    @discord.ui.button(label="Guardian", style=discord.ButtonStyle.secondary)
    async def guardian(self, i: discord.Interaction, b: discord.ui.Button):
        r = i.response
        await response.edit(f"{i.user.mention} made a new **Guardian** named ***{self.name}***")
    
    @discord.ui.button(label="Bard", style=discord.ButtonStyle.secondary)
    async def bard(self, i: discord.Interaction, b: discord.ui.Button):
        r = i.response
        await response.edit(f"{i.user.mention} made a new **Bard** named ***{self.name}***")

    @discord.ui.button(label="Wizard", style=discord.ButtonStyle.secondary)
    async def wizard(self, i: discord.Interaction, b: discord.ui.Button):
        r = i.response
        await response.edit(f"{i.user.mention} made a new **Wizard** named ***{self.name}***")

    @discord.ui.button(label="Hero", style=discord.ButtonStyle.secondary)
    async def hero(self, i: discord.Interaction, b: discord.ui.Button):
        r = i.response
        await response.edit(f"{i.user.mention} made a new **Hero** named ***{self.name}***")



    

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

@bot.tree.command(
    name="ocreate",
    description="A version of the /create command, making it simpler"
)
@is_alpha()
@apc.describe(name="The name of your character")
async def onboard(i: discord.Interaction, name: str):
    r = i.response
    e = discord.Embed(title="***Pick a Class***", color=0x7ae4ff)
    e.add_field(name="Fighter", value="Fighters are a really *in* *your* *face* kind of person, and will hit even harder when in range", inline=False)
    e.add_field(name="Ranger", value="Skilled in the use of bows, Rangers can hit enemies from further away, and sometimes even multiple ", inline=False)
    e.add_field(name="Thief", value="Using their stealth and agility, Thieves can scout ahead, and sneak around enemies", inline=False)
    e.add_field(name="Guardian", value="Slow but tough, basically the Guardian motto, whatever they lack in speed they make up for greatly in defense", inline=False)
    e.add_field(name="Bard", value="Known for their charm, Bards can support their allies through song, but are weak to being attacked", inline=False)
    e.add_field(name="Wizard", value="Beings of great Elemental power and knowledge. Wizards are immune to attacks using the same element as them, but are weak to certain other elements ", inline=False)
    e.add_field(name="Hero", value="Not having any major increase in stats to boast about, Hero isn't for everyone, but that special can hit ***REALLY*** hard", inline=False)
    v = ocreateClassView(name)
    await r.send_message(embed=e, view=v)


if __name__ == "__main__":
    token = os.environ['BOT_TOKEN']
    bot.run(token)