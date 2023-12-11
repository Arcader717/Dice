import discord

class baseTurnViews(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Basic", style=discord.ButtonStyle.secondary)
    async def basic(i: discord.Interaction, b: discord.ui.Button):
        r = i.response
        await r.send_message("Basic clicked", ephemeral=True)

    @discord.ui.button(label="Item", style=discord.ButtonStyle.primary)
    async def item(i: discord.Interaction, b: discord.ui.Button):
        r = i.response
        await r.send_message("Item clicked", ephemeral=True)

    @discord.ui.button(label="Improvise", style=discord.ButtonStyle.greeen)
    async def improvise(i: discord.Interaction, b: discord.ui.Button):
        r = i.response
        await r.send_message("Improvise clicked", ephemeral=True)

    @discord.ui.button(label="Brace", style=discord.ButtonStyle.danger)
    async def brace(i: discord.Interaction, b: discord.ui.Button):
        r = i.response
        await r.send_message("Brace clicked", ephemeral=True)
        
    @discord.ui.button(label="Move", style=discord.ButtonStyle.red)
    async def move(i: discord.Interaction, b: discord.ui.Button):
        r = i.response
        await r.send_message("Move clicked", ephemeral=True)

    @discord.ui.button(label="Special", style=discord.ButtonStyle.danger)
    async def special(i: discord.Interaction, b: discord.ui.Button):
        r = i.response
        await r.send_message("Special clicked", ephemeral=True)

class turnEmbeds:
    def __init__(self, page: str | None = None):
        # page represents which page, b is basic, s is special, i is item, v is improvise, e is brace, m is move   
        self.page = page