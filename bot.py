from attr import dataclass
from discord.ext import commands
import discord
from config import BOT_TOKEN

CHANNEL_ID = 1223904426553507880


@dataclass 
class Session:
    is_active: bool = False
    start_time: int = 0



bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
session = Session()

@bot.event
async def on_ready():
    print("Hello! Study bot is ready!")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hello! Study bot is ready!")
    
@bot.command()
async def start(ctx):
    if session.is_active:
        await ctx.send("A study session is already active")
        
    session.is_active = True
    session.start_time = ctx.message.created_at.timestamp()
    await ctx.send(f"Study session has started at {ctx.message.created_at}")

@bot.command()
async def end(ctx):
    if not session.is_active:
        await ctx.send("No session is active")
        return
        
    session.is_active = False
    end_time = ctx.message.created_at.timestamp()
    duration = end_time - session.start_time
    await ctx.send(f"Study ended after {duration} seconds")
    
    

bot.run(BOT_TOKEN)