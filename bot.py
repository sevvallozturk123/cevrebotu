import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')
@bot.command()
async def atıkları_azaltmanın_yolları(ctx):
    fikirler = [
        "Atıkları ayrıştrabilirsin..",
        "Atıkları sanat eserine dönüştürebilirsin.",
        "Atıkları arıştırıp atık kumbaralarına atabilirsin.",
        "Atık toplama etkinliklerini karılabilirsin."
    ]
    
    await ctx.send(f"Evde yapabileceğin plastik el işleri:\n- " + "\n- ".join(fikirler))
bot.run("token")
    
    
    
