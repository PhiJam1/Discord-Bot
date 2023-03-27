from discord.ext import commands
import discord
import word
import cred
import Member

# Global Variables
bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())
CHANNEL_ID = 694909060285333557
SERVER_ID = 694909060285333554
file_name = "word_data.txt"
#^using this means this code will only work for 1 server
#that will need to be changed soon
members = []
loaded_data = False


@bot.event
async def on_ready():
    print("Bot is online")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Loading data...")
    #look through data files for members alr there. Then create any new ones
    #for new members that don't alr have members in it.
    ## fill up members list
    guild = bot.get_guild(SERVER_ID)
    for user in guild.members:
        members.append(Member.Member(user.name, user.id, [], [], 0, 0, 0))
    await channel.send("...done")

@bot.event
async def on_message(message):
    channel = bot.get_channel(CHANNEL_ID)
    #just used to see if anything works
    if (message.content == "$hello"):
        if (message.author != cred.BIBMO_NAME):
            await message.channel.send("got it from: " + str(message.author))
            await message.author.send('👋')
    
    #Actual commands
    scan_msg(message) #need to get stats on every message sent
    if (message.content == "$members"):
        await get_members(message)
        
    if (message.content[:8] == "$addword"):
        await add_word(message)
    if (message.content[:9] == "$seewords"):
        await display_words_tracked(message.channel)
    if (message.content[:11] == "$seestatsof"):
        await get_user_stats(message)
        return
    if (message.content[:9] == "$seestats"):
        await get_use_of_word(message)
    if (message.content == "$save"):
        save_all_data()
async def get_members(message):
    await message.channel.send("People in this server: ")
    for member in message.guild.members:
        await message.channel.send(member)
async def add_word(message):
    print("here")
    #get the word/phrase
    msg_content = message.content[9:]
    #do a check to see if its alr a word
    for word in members[0].terms_to_track:
        if (word == msg_content):
            await message.channel.send("That word is already being tracked")
            return
    #Now add this as a term to all members
    for member in members:
        member.add_term(msg_content)


async def display_words_tracked(channel):
    await channel.send("Here is a list of all words being tracked")
    for word in members[0].terms_to_track:
        await channel.send(word)

def scan_msg(message):
    if (message.content[0] != "$"):
        for member in members:
            if (member.user_name == message.author.name):
                member.update_message_history(message.content)
    save_all_data()

async def get_use_of_word(message):
    for member in members:
        await message.channel.send(member.get_total_stats())
        print("line 84")
async def get_user_stats(message):
    for member in members:
        if (message.content.find(str(member.user_id)) >= 0):
            await message.channel.send(member.get_total_stats())
async def get_stats_of_term(message):
    msg = message[5:]
    await message.channel.send("Word: " + msg)
    for i in range(len(members[0].terms_to_track)):
        if (members[0].terms_to_track[i] == msg):
            for member in members:
                await message.channel.send(member.user_name)
                await message.channel.send(member.get_stats_of_word(i))
def save_all_data():
    file = open(file_name, "w")
    for  member in members:
        file.write(member.get_data())
        file.write("\n")
    file.write("END")
    #file.flush()
    file.close()
bot.run(cred.BOT_TOKEN)
