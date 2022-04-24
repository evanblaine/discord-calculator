import discord
from discord.ext import commands
from config import *


class Calculator(discord.ui.View):
    def __init__(self):
        self.message = ""
        self.operators = [
            "+",
            "*",
            "/",
            "-",
            "."
        ]
        super().__init__(timeout=None)

    @discord.ui.button(label="C", style=discord.ButtonStyle.red)
    async def _clear(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.message = ""
        await interaction.response.edit_message(content=f"`0`")

    @discord.ui.button(label="9", style=discord.ButtonStyle.green)
    async def _nine(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.message += button.label
        await interaction.response.edit_message(content=f"`{self.message}`")

    @discord.ui.button(label="8", style=discord.ButtonStyle.green)
    async def _eight(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.message += button.label
        await interaction.response.edit_message(content=f"`{self.message}`")

    @discord.ui.button(label="7", style=discord.ButtonStyle.green)
    async def _seven(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.message += button.label
        await interaction.response.edit_message(content=f"`{self.message}`")

    @discord.ui.button(label="=", style=discord.ButtonStyle.grey)
    async def _equals(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.message = str(eval(self.message))
        await interaction.response.edit_message(content=f"`{self.message}`")

    @discord.ui.button(label="+", style=discord.ButtonStyle.grey)
    async def _add(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.message != "":
            if self.message[-1] not in self.operators:
                self.message += button.label
                await interaction.response.edit_message(content=f"`{self.message}`")

    @discord.ui.button(label="6", style=discord.ButtonStyle.green)
    async def _six(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.message += button.label
        await interaction.response.edit_message(content=f"`{self.message}`")

    @discord.ui.button(label="5", style=discord.ButtonStyle.green)
    async def _five(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.message += button.label
        await interaction.response.edit_message(content=f"`{self.message}`")

    @discord.ui.button(label="4", style=discord.ButtonStyle.green)
    async def _four(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.message += button.label
        await interaction.response.edit_message(content=f"`{self.message}`")

    @discord.ui.button(label="-", style=discord.ButtonStyle.grey)
    async def _subtract(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.message != "":
            if self.message[-1] not in self.operators:
                self.message += button.label
                await interaction.response.edit_message(content=f"`{self.message}`")

    @discord.ui.button(label="*", style=discord.ButtonStyle.grey)
    async def _multiply(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.message != "":
            if self.message[-1] not in self.operators:
                self.message += button.label
                await interaction.response.edit_message(content=f"`{self.message}`")

    @discord.ui.button(label="3", style=discord.ButtonStyle.green)
    async def _three(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.message += button.label
        await interaction.response.edit_message(content=f"`{self.message}`")

    @discord.ui.button(label="2", style=discord.ButtonStyle.green)
    async def _two(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.message += button.label
        await interaction.response.edit_message(content=f"`{self.message}`")

    @discord.ui.button(label="1", style=discord.ButtonStyle.green)
    async def _one(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.message += button.label
        await interaction.response.edit_message(content=f"`{self.message}`")

    @discord.ui.button(label="/", style=discord.ButtonStyle.grey)
    async def _divide(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.message != "":
            if self.message[-1] not in self.operators:
                self.message += button.label
                await interaction.response.edit_message(content=f"`{self.message}`")

    @discord.ui.button(label="\u200b", style=discord.ButtonStyle.grey)
    async def _placeholder1(self, button: discord.ui.Button, interaction: discord.Interaction):
        pass

    @discord.ui.button(label="\u200b", style=discord.ButtonStyle.grey)
    async def _placeholder2(self, button: discord.ui.Button, interaction: discord.Interaction):
        pass

    @discord.ui.button(label="0", style=discord.ButtonStyle.grey)
    async def _zero(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.message += button.label
        await interaction.response.edit_message(content=f"`{self.message}`")

    @discord.ui.button(label=".", style=discord.ButtonStyle.grey)
    async def _decimal(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.message != "":
            if self.message[-1] not in self.operators:
                self.message += button.label
                await interaction.response.edit_message(content=f"`{self.message}`")

    @discord.ui.button(label="\u200b", style=discord.ButtonStyle.grey)
    async def _placeholder3(self, button: discord.ui.Button, interaction: discord.Interaction):
        pass


class CalculatorBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


bot = CalculatorBot()

@bot.slash_command()
async def calculator(ctx: commands.Context):
    """A calculator within Discord!"""
    await ctx.respond("`0`", view=Calculator())

bot.run(TOKEN)
