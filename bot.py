from discord.ext import commands
import discord
import word
import cred
import Member

# Global Variables
bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())
CHANNEL_ID = 958397523217756213
SERVER_ID = 958397522768982099
#using this means this code will only work for 1 server
#that will need to be changed soon
members = []
loaded_data = False


@bot.event
async def on_ready():
    print("Greetings")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Loading data...")
    #look through data files for members alr there. Then create any new ones
    #for new members that don't alr have members in it.
    ## fill up members list
    guild = bot.get_guild(SERVER_ID)
    for user in guild.members:
        members.append(Member.Member(user.name, user.id, [], [], 0, 0, 0))
    await channel.send("...done")
'''
@bot.event
async def on_message(message):
    channel = bot.get_channel(CHANNEL_ID)

    #not sure if this needs an await
    scan_msg(message)
    if (message.content == "$hello"):
        if (message.author != cred.BIBMO_NAME):
            await message.channel.send("got it from: " + str(message.author))
            await message.author.send('👋')
    if (message.content == "$members"):
        await channel.send("People in this server: ")
        for member in message.guild.members:
            await channel.send(member)
    if (message.content[:5] == "$addword"):
        await add_word(message)


async def add_word(message):
    #get the word/phrase
    msg_content = message.content[5:]
    #do a check to see if its alr a word
    for word in words:
        if (word.term == msg_content):
            return
    #create the new word object
    words.append(word(msg_content, authors, 0, 0, 0))
    words.append(msg_content)
    ## lets try some file IO
    for guild in bot.guilds:
        await message.channel.send(message.guild.name)

#def scan_msg(message):
    
'''
def printstuff(stuff):
    print(stuff)


bot.run(cred.BOT_TOKEN)
