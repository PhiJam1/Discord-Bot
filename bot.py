from discord.ext import commands
import discord
import word
import cred
bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())
CHANNEL_ID = 958397523217756213

#i've made a change
#i've now made another change
#third change
@bot.event
async def on_ready():
    print("Greetings")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Greetings")

@bot.event
async def on_message(message):
    channel = bot.get_channel(CHANNEL_ID)
    if (message.content == "$hello"):
        if (message.author != cred.BIBMO_NAME):
            await message.channel.send("got it from: " + str(message.author))
            await message.author.send('👋')

bot.run(BOT_TOKEN)