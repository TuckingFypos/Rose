import secrets
import discord
from discord.ext.commands import Bot
import requests
import random
import json

rose = Bot(command_prefix="!")

@rose.event
async def on_read():
    print('Logged in as')
    print(rose.user.name)

@rose.command()
async def commands(*args):
    await rose.say("!roll NdN to roll a dice")
    await rose.say("!coinflip to flip a coin")
    await rose.say("!hello to say hi")
    await rose.say("!slap [username] to slap someone in public")
    await rose.say("!choose [choices, separated by spaces]")
    await rose.say("!Overwatch [battle tag] NOTE:: replace # with -")
    await rose.say("!Destiny to get a list of destiny-related commands")

@rose.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}! Type !commands for a list of available bot commands.'
    await rose.send_message(server, fmt.format(member, server))

@rose.command(pass_context=True)
async def hello(ctx):
    respond_to = ctx.message.author
    return await rose.say("Hello, " + str(respond_to) + "! I'm Rose, a Chatbot and Automod"
                                                        " for the Casual Tryhards Discord."
                          " Type !commands to see a list of available chat commands."
                          " Type !admin to page a live administrator.")

@rose.command()
async def roll(dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await rose.say('Format has to be in NdN!')
        return
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await rose.say(result)

@rose.command(pass_context=True)
async def slap(ctx, member: discord.Member):
    inventory = random.randint(1, 7)
    if inventory == 1:
        weapon = "a rusty spoon."
    if inventory == 2:
        weapon = "a smelly fish."
    if inventory == 3:
        weapon = "a purple dildo bat."
    if inventory == 4:
        weapon = "the Master Sword."
    if inventory == 5:
        weapon = "a lightsaber."
    if inventory == 6:
        weapon = "a mean backhand ... but they missed."
    if inventory == 7:
        weapon = "a wet noodle."
    attacker = ctx.message.author
    return await rose.say(str(attacker) + " slaps " + member.mention + " with " + weapon)

@rose.command()
async def choose(*choices: str):
    await rose.say(random.choice(choices))

@rose.command(pass_context=True)
async def admin(ctx):
    helpme = str(ctx.message.author)
    await rose.send_message(, "Hello")


rose.run(secrets.client_token)
