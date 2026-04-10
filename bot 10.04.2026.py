import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Bot ligado!")

@bot.command()
async def poluicao(ctx):
    await ctx.send("Poluição é a contaminação do meio ambiente.")

@bot.command()
async def ar(ctx):
    await ctx.send("Poluição do ar vem de carros, fábricas e queimadas.")

@bot.command()
async def agua(ctx):
    await ctx.send("Poluição da água vem de lixo e esgoto.")

bot.run("COLE_SEU_TOKEN_AQUI")
