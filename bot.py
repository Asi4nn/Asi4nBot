# bot.py
import discord
import time
from discord.ext import commands

client = commands.Bot(command_prefix = '/')

################################
# EVENTS
################################

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await client.process_commands(message) # THIS MAKES SURE THE COMMANDS EXTENSION WORKS


@client.event
async def on_message_delete(message):
    if (message.author.bot):
        return
    else:
        print(f'Deleted "{message.content}" by {message.author.mention}')
        await message.channel.send(f"{message.author.mention}'s message got deleted: {message.content}")

################################
# COMMANDS
################################

@client.command()
async def dinner(ctx):
    await ctx.send('<@&631594442771660801> the table is set.')


@client.command()
async def nuke(ctx):
    await ctx.send('<:nuke:535289100761038869> TACTICAL NUKE INCOMING <:nuke:535289100761038869>')


@client.command()
async def tsar_bomba(ctx):
    await ctx.send(("The Tsar Bomba was the biggest bomb ever created. \nTested"
                    "on 30 October 1961 as an experimental verification of "
                    "calculation principles and multi-stage thermonuclear weapon "
                    "designs, it also remains the most powerful human-made "
                    "explosive ever detonated.\nIt's frequently dropped by "
                    "Cameron 'fucking' Neethling"))


@client.command()
async def jason(ctx, num = ''):
    if num.isnumeric() == False:
        await ctx.send("Welcome to Jason quotes V1.0, type /jason 1-4 for some famous quotes")
        return
    num = int(num)

    if 1 <= num <= 4:
        if num == 1:
            await ctx.send("The North pole isn't Antarctica?")
        elif num == 2:
            await ctx.send("I'll take a screenshot of my screentearing")
        elif num == 3:
            await ctx.send("What's the capital of France?")
        elif num == 4:
            await ctx.send("Wait we have to download the PTS?")
        else:
            await ctx.send("Welcome to Jason quotes V1.0, type /jason 1-4 for some famous quotes")
    else:
        await ctx.send("Welcome to Jason quotes V1.0, type /jason 1-4 for some famous quotes")


@client.command()
async def echo(ctx, message: str):
    await ctx.send(message)


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command()
async def clear(ctx, num=0):
    await ctx.channel.purge(limit = num)
    time.sleep(2)
    await ctx.send(f"Deleted {num} messages!")


client.run('Njk1Nzc3NDIzNDU4OTU5NDEw.XokeEw.-AhrLA3fF9PW7cY-QGZ4gjLEtz4')