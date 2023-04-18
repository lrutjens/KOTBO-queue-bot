import dotenv
from dotenv import load_dotenv
import os
import asyncio

from typing import Union
from discord import option
dotenv.load_dotenv()
import discord
import os 

load_dotenv()
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")

@bot.slash_command(description="Sends the bot's latency.") # this decorator makes a slash command
async def ping(ctx): # a slash command will be created with the name "ping"
    await ctx.respond(f"Pong! Latency is {bot.latency}")

@bot.slash_command(name="queue", description="Group up for raids")
@option("queue", description="Dungeons, Raids, or Roulettes", choices=["Dungeons", "Raids", "Roulettes"])
async def queue(ctx: discord.ApplicationContext, queue: str):
    await bot.wait_until_ready()
    await ctx.respond(f"Queuing you for {queue}...")
    member = ctx.author
    role = discord.utils.get(ctx.guild.roles, name=f"{queue} Queue")
    await member.add_roles(role, reason=None, atomic=True)
    await asyncio.sleep(1)
    await ctx.send(f"Queued you for {queue}! You can leave the queue at any time by typing `/unqueue`.")
    if queue == "Dungeons":
        channel = bot.get_channel(int(os.getenv('DUNGEON_QUEUE_CHANNEL_ID'))) #Place channel id for dungeons queue here
    if queue == "Raids":
        channel = bot.get_channel(int(os.getenv('RAID_QUEUE_CHANNEL_ID'))) #Place channel id for the Raids Queue here
    if queue == "Roulettes":
        channel = bot.get_channel(int(os.getenv('ROULETTE_QUEUE_CHANNEL_ID'))) #Place channel id for the roulettes queue here
    await channel.send(f'{role.mention}, {ctx.author.mention} has queued for {queue}!')
    print(f"{ctx.author.name} has queued for {queue}!")

@bot.slash_command(description="Leave the queue for Roulettes/Dungeons/Raids")
async def unqueue(ctx):
    await bot.wait_until_ready()
    member = ctx.author
    await ctx.send_response("Removing you from the queue...")
    print(f"{ctx.author} has left the queue")
    roles = [discord.utils.get(ctx.guild.roles, name="Raids Queue"),
             discord.utils.get(ctx.guild.roles, name="Dungeons Queue"),
             discord.utils.get(ctx.guild.roles, name="Roulettes Queue")]
    matching_roles = set(member.roles).intersection(set(roles))
    for role in matching_roles:
        await member.remove_roles(role, reason=None, atomic=True)
        if role.name == "Dungeons Queue":
            channel = bot.get_channel(int(os.getenv('DUNGEON_QUEUE_CHANNEL_ID')))
        if role.name == "Raids Queue":
           channel = bot.get_channel(int(os.getenv('RAID_QUEUE_CHANNEL_ID')))
        if role.name == "Roulettes Queue":
            channel = bot.get_channel(int(os.getenv('ROULETTE_QUEUE_CHANNEL_ID')))
        await channel.send(f"{ctx.author.name} has left the queue.")
        print(f"{ctx.author.name} has left the {role.name} queue")
    await asyncio.sleep(1)
    await ctx.send("Removed you from the queue!")

@bot.slash_command(description="Info about the bot")
async def about(ctx):
    ctx.send_response("I'm a bot made by Angry Fool#2653 for `The Knights of the Blood Oath` for queuing people into Dungeons/Raids/Roulettes.s")

bot.run(str(os.getenv('TOKEN')))
