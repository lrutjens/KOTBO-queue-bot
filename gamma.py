import dotenv #type: ignore
from dotenv import load_dotenv #type: ignore
import os
import asyncio

from discord import option
dotenv.load_dotenv()
import discord
import os 

load_dotenv()
bot = discord.Bot()
queue = bot.create_group("queue", "Queue for Raids, Dungeons, and Roulettes!")


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(description="Sends the bot's latency.") # this decorator makes a slash command
async def ping(ctx): # a slash command will be created with the name "ping"
    await ctx.respond(f"Pong! Latency is {bot.latency}")

@queue.command()
@option("tier", base=queue, description="Raid Tiers", choices=["Tier 1", "Tier 2"], required=True)
async def raids(ctx: discord.ApplicationContext, tier: str):
    await ctx.respond(f"Queuing you for Raids...")
    member = ctx.author
    role = discord.utils.get(ctx.guild.roles, name=f"{tier} Raid Queue")
    await member.add_roles(role, reason=None, atomic=True)
    await asyncio.sleep(1)
    await ctx.send(f"Queued you for {tier} Raids! Unqueue at anytime by typing `/unqueue`")
    print(f"{ctx.author.name} has queued for Raids {tier}!")
    if tier=="Tier 1":
        channel = bot.get_channel(int(os.getenv('RAID_QUEUE_CHANNEL_ID_1')))
    else:
        channel = bot.get_channel(int(os.getenv('RAID_QUEUE_CHANNEL_ID_2')))
    await channel.send(f'{role.mention}, {ctx.author.mention} has queued for Raids {queue}!')

@queue.command()
async def dungeons(ctx: discord.ApplicationContext):
    await ctx.respond(f"Queuing you for Dungeons...")
    member = ctx.author
    role = discord.utils.get(ctx.guild.roles, name=f"Dungeons Queue")
    await member.add_roles(role, reason=None, atomic=True)
    await asyncio.sleep(1)
    await ctx.send(f"Queued you for Dungeons! Unqueue at anytime by typing `/unqueue`")
    print(f"{ctx.author.name} has queued for Dungeons!")
    channel = bot.get_channel(int(os.getenv('DUNGEON_QUEUE_CHANNEL_ID')))
    await channel.send(f'{role.mention}, {ctx.author.mention} has queued for Dungeons!')

@queue.command()
@option("type", base=queue, description="Roulette Tiers", choices=["Leveling", "Raid", "Expert"], required=True)
async def roulettes(ctx: discord.ApplicationContext, type: str):
    await ctx.respond(f"Queuing you for Raids...")
    member = ctx.author
    role = discord.utils.get(ctx.guild.roles, name=f"{type} Roulette Queue")
    await member.add_roles(role, reason=None, atomic=True)
    await asyncio.sleep(1)
    await ctx.send(f"Queued you for {type} Raids! Unqueue at anytime by typing `/unqueue`")
    print(f"{ctx.author.name} has queued for {type} Roulettes!")
    if type=="Leveling":
        channel = bot.get_channel(int(os.getenv('ROULETTE_QUEUE_LEVELING')))
    elif type=="Raid":
        channel = bot.get_channel(int(os.getenv('ROULETTE_QUEUE_RAIDS')))
    else:
        channel = bot.get_channel(int(os.getenv('ROULETTE_QUEUE_EXPERT')))
    await channel.send(f'{role.mention}, {ctx.author.mention} has queued for {type} Roulettes!')
    
@bot.slash_command(description="Leave the queue for Roulettes/Dungeons/Raids")
async def unqueue(ctx):
    await bot.wait_until_ready()
    member = ctx.author
    await ctx.send_response("Removing you from the queue...")
    print(f"{ctx.author} has left the queue")
    roles = [discord.utils.get(ctx.guild.roles, name="Tier 1 Raid Queue"),
             discord.utils.get(ctx.guild.roles, name="Tier 2 Raid Queue"),
             discord.utils.get(ctx.guild.roles, name="Dungeons Queue"),
             discord.utils.get(ctx.guild.roles, name="Leveling Roulette Queue"),
             discord.utils.get(ctx.guild.roles, name="Raid Roulette Queue"),
             discord.utils.get(ctx.guild.roles, name="Expert Roulette Queue")]
    matching_roles = set(member.roles).intersection(set(roles))
    for role in matching_roles:
        await member.remove_roles(role, reason=None, atomic=True)
        if role.name == "Dungeons Queue":
            channel = bot.get_channel(int(os.getenv('DUNGEON_QUEUE_CHANNEL_ID')))
            await channel.send(f"{ctx.author.name} has left the queue.")
        if role.name == "Tier 1 Raid Queue":
           channel = bot.get_channel(int(os.getenv('RAID_QUEUE_CHANNEL_ID_1')))
           await channel.send(f"{ctx.author.name} has left the queue.")
        if role.name == "Tier 2 Raid Queue":
           channel = bot.get_channel(int(os.getenv('RAID_QUEUE_CHANNEL_ID_2')))
           await channel.send(f"{ctx.author.name} has left the queue.")
        if role.name == "Leveling Roulette Queue":
            channel = bot.get_channel(int(os.getenv('ROULETTE_QUEUE_LEVELING')))
            await channel.send(f"{ctx.author.name} has left the queue.")
        if role.name == "Raid Roulette Queue":
            channel = bot.get_channel(int(os.getenv('ROULETTE_QUEUE_RAIDS')))
            await channel.send(f"{ctx.author.name} has left the queue.")
        if role.name == "Expert Roulette Queue":
            channel = bot.get_channel(int(os.getenv('ROULETTE_QUEUE_EXPERT')))
            await channel.send(f"{ctx.author.name} has left the queue.")
        print(f"{ctx.author.name} has left the {role.name} queue")
    await asyncio.sleep(1)
    await ctx.send("Removed you from the queue!")

@bot.slash_command(description="Info about the bot")
async def about(ctx):
    ctx.send_response("I'm a bot made by Angry Fool#2653 for `The Knights of the Blood Oath` for queuing people into Dungeons/Raids/Roulettes.s")

bot.run(str(os.getenv('TOKEN')))
