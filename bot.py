from discord.ext import commands
import discord
import word
BOT_TOKEN = "MTA4NDUyMzk4MTk0OTkwNzA2NQ.GECY0X.rz8jjOrj1w2J1J0Q0IfEKe7GW36mMwha-dMCTI"
bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())
CHANNEL_ID = 958397523217756213
BIBMO_NAME = "bimbo#0660"



@bot.event
async def on_ready():
    print("Greetings")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Greetings")

@bot.event
async def on_message(message):
    channel = bot.get_channel(CHANNEL_ID)
    if (message.content == "$hello"):
        if (message.author != BIBMO_NAME):
            await message.channel.send("got it from: " + str(message.author))
            await message.author.send('👋')

bot.run(BOT_TOKEN)