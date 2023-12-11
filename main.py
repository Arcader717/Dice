import discord # Lets me start up a discord bot
from discord import app_commands as apc
from discord.ext import commands
import os # Secret variables
import random
from keep_alive import keep_alive

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
    def __init__(self, name: str | None, page: int):
        super().__init__(timeout=None)
        self.name = name
        self.page = page
        self.pageToClass = {
            1: 'Fighter',
            2: "Ranger",
            3: "Thief",
            4: "Guardian", 
            5: "Bard",
            6: "Wizard",
            7: "Hero"
        }

    @discord.ui.button(label="Previous", style=discord.ButtonStyle.primary)
    async def prev(self, i: discord.Interaction, button: discord.ui.Button):
        r = i.response
        if self.page == 1:
            v = ocreateClassView(self.name, 7)
            e = await ocreateClassEmbeds().getPage(7)
        else:
            v = ocreateClassView(self.name, self.page - 1)
            e = await ocreateClassEmbeds().getPage(self.page - 1)
        await r.edit_message(embed=e, view=v)

    @discord.ui.button(label="Select", style=discord.ButtonStyle.success)
    async def sel(self, i: discord.Interaction, button: discord.ui.Button):
        r = i.response
        await r.edit_message(content=f"{i.user.mention} created a new **{self.pageToClass[self.page]}** named ***{self.name}***", view=None, embed=None)

    @discord.ui.button(label="Next", style=discord.ButtonStyle.primary)
    async def next(self, i: discord.Interaction, button: discord.ui.Button):
        r = i.response
        if self.page == 7:
            v = ocreateClassView(self.name, 1)
            e = await ocreateClassEmbeds().getPage(1)
        else:
            v = ocreateClassView(self.name, self.page + 1)
            e = await ocreateClassEmbeds().getPage(self.page + 1)
        await r.edit_message(embed=e, view=v)



class ocreateClassEmbeds:
    
    def __init__(self):
        
        self.fighter = discord.Embed(title="***Pick a Class***", color=0x7ae4ff)
        self.fighter.add_field(name="Fighter", value="Fighters are a really *in* *your* *face* kind of person, and will hit even harder when in range", inline=False)

        self.ranger = discord.Embed(title="***Pick a Class***", color=0x7ae4ff)
        self.ranger.add_field(name="Ranger", value="Skilled in the use of bows, Rangers can hit enemies from further away, and sometimes even multiple ", inline=False)

        self.thief = discord.Embed(title="***Pick a Class***", color=0x7ae4ff)
        self.thief.add_field(name="Thief", value="Using their stealth and agility, Thieves can scout ahead, and sneak around enemies", inline=False)

        self.guardian = discord.Embed(title="***Pick a Class***", color=0x7ae4ff)
        self.guardian.add_field(name="Guardian", value="Slow but tough, basically the Guardian motto, whatever they lack in speed they make up for greatly in defense", inline=False)

        self.bard = discord.Embed(title="***Pick a Class***", color=0x7ae4ff)
        self.bard.add_field(name="Bard", value="Known for their charm, Bards can support their allies through song, but are weak to being attacked", inline=False)

        self.wizard = discord.Embed(title="***Pick a Class***", color=0x7ae4ff)
        self.wizard.add_field(name="Wizard", value="Beings of great Elemental power and knowledge. Wizards are immune to attacks using the same element as them, but are weak to certain other elements", inline=False)

        self.hero = discord.Embed(title="***Pick a Class***", color=0x7ae4ff)
        self.hero.add_field(name="Hero", value="Not having any major increase in stats to boast about, Hero isn't for everyone, but that special can hit ***REALLY*** hard", inline=False)

    async def getPage(self, page: str | int) -> discord.Embed:
        if page == "fighter":
            return self.fighter
        elif page == "ranger":
            return self.ranger
        elif page == "thief":
            return self.thief
        elif page == "guardian":
            return self.guardian
        elif page == "bard":
            return self.bard
        elif page == "wizard":
            return self.wizard
        elif page == "hero":
            return self.hero
        elif page == 1:
            return self.fighter
        elif page == 2:
            return self.ranger
        elif page == 3:
            return self.thief
        elif page == 4:
            return self.guardian
        elif page == 5:
            return self.bard
        elif page == 6:
            return self.wizard
        elif page == 7:
            return self.hero
        else:
            return discord.Embed(title="Error", description="Invalid Page", color=0xff0000)
            
        



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
@apc.describe(number="The number of dice you want to roll")
async def roll(i: discord.Interaction, dice: apc.Choice[str], number: int | None):
    r = i.response
    if isinstance(number, None):
        await r.send_message(f"{i.user.mention} rolled a D{dice.value} and got a ***{str(random.randint(1, int(dice.value)))}***") # Simulates a Dice
    elif isinstance(number, int):
        if number > 10:
            await r.send_message("Too many dice, try less than or equal to 10", ephemeral=True)
        rollNum = 0
        rolled = []
        total = 0
        rollStr = ""
        while rollNum < number:
            rollNum += 1
            rolled.append = str(random.randint(1, int(dice.value)))
        for roll in rolled:
            total += int(roll)
            if roll == rolled[number - 1]:
                rollStr = rollStr + f"**{str(roll)}**"
            else:
                rollStr = rollStr + f"**{str(roll)}**, "
        await r.send_message(f"{i.user.mention} rolled {str(number)} D{dice.value}'s, and got {rollStr} for a total of {str(total)}")
    

"""@bot.tree.command(
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
    await r.send_message(f"{i.user.mention} made a new **{str(type.name)}** named ***{name}***")"""

@bot.tree.command(
    name="create",
    description="Create a character"
)
@apc.describe(name="The name of your character")
async def create(i: discord.Interaction, name: str):
    r = i.response
    e = await ocreateClassEmbeds().getPage(1)
    v = ocreateClassView(name, 1)
    await r.send_message(embed=e, view=v)


@bot.tree.command(
    name="turn",
    description="Take a turn"
)
@is_alpha()
async def turn(i: discord.Interaction):
    r = i.response
    if True: # The condition if it's there turn
        await r.send_message("This doesn't work yet, check back later")


if __name__ == "__main__":
    keep_alive()
    token = os.environ['BOT_TOKEN']
    bot.run(token)
