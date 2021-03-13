import os
import eproll
import discord

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

helpmessage = "Rolls a d100 for EP mechanics, accepts an integer between 0 and 130 as input for skill level"


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(help="Prints out arguments provided by user")
async def test(ctx, *arg):
    await ctx.send(arg)


@bot.command(name='ep', help=helpmessage, pass_context=True)
async def roll(ctx, skill: int, dmg=''):
    print("Skill is:", skill)
    username = ctx.message.author.nick  # THIS IS IT

    if isinstance(skill, int) and (skill in range(0, 131)) and (dmg != ''):
        print('Number is between 0 & 130 and is an Int')
        result = eproll.check(skill)
        damage = eproll.damage(dmg)
        outcome = str(result[0]) + '\r' + result[1]

        await ctx.send('{} rolled, result: {}, damage: {}'.format(username, outcome, damage))
        return

    elif isinstance(skill, int) and (skill in range(0, 131)):
        print('Number is between 0 & 130 and is an Int')
        result = eproll.check(skill)
        outcome = str(result[0]) + '\r' + result[1]

        await ctx.send('{} rolled, result: {}'.format(username, outcome))
        return

    else:
        print('Invalid Number')
        await ctx.send('Invalid input, must be an integer between 0 and 130')
        return


@bot.event
async def on_command_error(ctx, error):
    print("ERROR")
    await ctx.send(error)


bot.run(TOKEN)
