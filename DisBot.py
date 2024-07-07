# This example requires the 'message_content' intent.
from LinkLogic import *
from SillyCommands import *
import discord
from discord import app_commands
import datetime
import asyncio
import configparser
import os.path

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)
config = configparser.ConfigParser()
if(not os.path.isfile("config.ini")):
    config['DEFAULT'] = {'ServerID': '1'}
    config['USERS'] = {'GreenId ' : 1, 'ReshId' : 1,
'SlyId' : 1, 'PonId ' : 1, 'KodahnId' : 1, 'KatId' : 1}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

config.read('config.ini')
serverId = config['DEFAULT']['ServerID']

id = discord.Object(serverId)
#Websites that help
#https://regex101.com/r/BFJBpZ/1 regex help
#https://discordpy.readthedocs.io/en/latest/api.html discord.py doc

# Add the guild ids in which the slash command will appear.
# If it should be in all, remove the argument, but note that
# it will take some time (up to an hour) to register the
# command if it's for all guilds.
@tree.command(description="embed a spoiled twitter, x, instagram, reddit media")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True) 
async def embed(interaction: discord.Interaction, link: str): 
    fullstring = interaction.user.display_name + " has posted\n"
    fullstring += returnSingleLink(link)
    await interaction.response.send_message(fullstring)

@tree.command(description="embed a spoiled twitter, x, instagram, reddit media")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True) 
@app_commands.guild_only()
async def spoil(interaction: discord.Interaction, link: str): 
    fullstring = interaction.user.display_name + "has posted\n"
    fullstring += returnSpoiledSingleLink(link)
    await interaction.response.send_message(fullstring)
    
@client.event
async def on_ready():
    await tree.sync(guild=id)
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    #Check's to make sure the bot doesn't respond to itself
    if message.author != client.user:
        if(regexTwitterLinks(message.content) != []):
            tupleCompleteAndFreeMessages = getFormattedMessage(message, message.author.display_name)
            if(tupleCompleteAndFreeMessages[0] != None): 
                await asyncio.sleep(1) #Sleeps to help with the delay of when the picture embeds? :shrug:
                #await message.edit(suppress=True) #Removes the embeds from the original message b/c y'know it's ugly
                await message.reply(tupleCompleteAndFreeMessages[0], allowed_mentions=discord.AllowedMentions.none(), silent = True) #Sends the message then, removes the mention so it doesn't @ the person
                await message.edit(suppress=True) #Removes the embeds from the original message b/c y'know it's ugly
                if ((followUpMessage := formatFreeMessages(tupleCompleteAndFreeMessages[1])) != ''):
                    await message.channel.send(followUpMessage)
                #if ((tupleCompleteAndFreeMessages[1]) != None):
                #    await message.channel.send("\n".join(tupleCompleteAndFreeMessages[1]))
        if(checkKnownUser(message.author.id) == True):
            responseMessage, isReaction = containsKeyword(message.content, message.author.id)
            if(responseMessage != ''):
                if(isReaction != True):
                    await message.reply(responseMessage, allowed_mentions=discord.AllowedMentions.none(), silent = True)
                else:
                    await message.add_reaction(responseMessage)
            
@client.event
async def on_raw_message_delete(rawMessage):
    #Complicated, two cases incase the message is cached or not if it is cached it's wayyy more accurate, when not cached it probably doesn't work so will need to be fixed
    if rawMessage.cached_message == None:
        #Read history, limit of 4 (b/c inaccuracy? it was an attempt, sloppy tbh) around the time of the message being deleted- if message is 5mins old it won't work unfortunately
        async for oldMessages in client.get_channel(rawMessage.channel_id).history(limit = 4, around = datetime.datetime.now()):
               if oldMessages.author == client.user:
                    deleteMessage = oldMessages
                    #this is a check to see if the bot's message that it's replying too was deleted or not, if so then it's safe to delete this message.
                    if isinstance(deleteMessage.reference.resolved, discord.DeletedReferencedMessage) or deleteMessage.reference.resolved == 'None': 
                        await deleteMessage.delete()
    else:
        message = rawMessage.cached_message
        if (regexTwitterLinks(message.content)) != []:
            async for oldMessages in message.channel.history(limit = 2, after = message):
                if oldMessages.author == client.user:
                    await oldMessages.delete() 

@client.event
async def on_raw_message_edit(rawMessage):
    #complicated line, but since message does exist, it can be grabbed using the partial messageable object
    editedMessage = await client.get_partial_messageable(rawMessage.channel_id).fetch_message(rawMessage.message_id)
    if(editedMessage.author == client.user):
        return
    #If the message was edited more than x second(s) ago then you can edit the bot message- reason being removing the embeds from the OG message (in the on_message event)
    if(editedMessage.created_at > (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(seconds=3))): # 
        return
    #This logic is flawed. Checks if message has twitter link, but what if I replace the twitter link with a .?
    #if (regexTwitterLinks(editedMessage.content)) != []:
    async for postMessage in editedMessage.channel.history(limit = 2, after = editedMessage):
        if postMessage.author == client.user:
            if(postMessage.reference != None):
                if (postMessage.reference.message_id == editedMessage.id):
                    completeMessage = getFormattedMessage(editedMessage, editedMessage.author.display_name)
                    if(completeMessage != None):
                        await postMessage.edit(content= completeMessage[0], allowed_mentions=discord.AllowedMentions.none())
                    else:
                        await postMessage.delete()
                    async for botFollowUpMessage in postMessage.channel.history(limit=2, after = postMessage):
                        if(botFollowUpMessage.author == client.user):
                            if((completeMessage != None)):
                                botFollowUpContent = formatFreeMessages(completeMessage[1])
                                if(botFollowUpContent != ''):
                                    await botFollowUpMessage.edit(content = botFollowUpContent, allowed_mentions = discord.AllowedMentions.none())
                                else:
                                    await botFollowUpMessage.delete()                                    
                            else:
                                await botFollowUpMessage.delete()
                    return
                                
                    
                    
client.run(open('TOKEN.bottoken','r').read())