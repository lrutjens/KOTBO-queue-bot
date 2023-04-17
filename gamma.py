import dotenv
import os
import asyncio
from typing import Union
from discord import option
dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))

import discord
import os 
from dotenv import load_dotenv

load_dotenv()
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")

@bot.slash_command(description="Sends the bot's latency.")
async def ping(ctx):
    await ctx.respond(f"Pong! Latency is {bot.latency}")

@bot.slash_command(name="queue", description="Group up for raids")
@option("queue", description="Dungeons, Raids, or Roulettes", choices=["Dungeons", "Raids", "Roulettes"])

async def queue(ctx: discord.ApplicationContext, queue: str):
    await ctx.respond(f"Queuing you for {queue}...")
    member = ctx.author
    role = discord.utils.get(ctx.guild.roles, name=f"{queue} Queue")
    await member.add_roles(role, reason=None, atomic=True)
    await asyncio.sleep(1)
    await ctx.send(f"Queued you for {queue}! You can leave the queue at any time by typing `/unqueue`.")
    if queue == "Dungeons":
        channel = bot.get_channel(1097502016147824642)
    if queue == "Raids":
        channel = bot.get_channel(1097502016147824643)
    if queue == "Roulettes":
        channel = bot.get_channel(1097502016147824644)
    await channel.send(f'{role.mention}, {ctx.author.mention} has queued for {queue}!')

@bot.slash_command(description="Leave the queue for Roulettes/Dungeons/Raids")
async def unqueue(ctx):
    print(f"{ctx.author.name}")
    await ctx.respond("Removing you from the queue...")
    member = ctx.author
    roles = [discord.utils.get(ctx.guild.roles, name="Raids Queue"),
             discord.utils.get(ctx.guild.roles, name="Dungeons Queue"),
             discord.utils.get(ctx.guild.roles, name="Roulettes Queue")]
    matching_roles = set(member.roles).intersection(set(roles))
    for role in matching_roles:
        await member.remove_roles(role, reason=None, atomic=True)
    await asyncio.sleep(1)
    await ctx.send("Removed you from the queue!")

bot.run(os.getenv('TOKEN'))
