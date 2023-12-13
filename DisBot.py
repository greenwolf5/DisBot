# This example requires the 'message_content' intent.

import discord
import datetime
import re
import asyncio
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

#Websites that help
#https://regex101.com/r/BFJBpZ/1 regex help
#https://discordpy.readthedocs.io/en/latest/api.html discord.py doc

#Two domains this works on not modular to add a new domain but not too difficult
TWITTER = 'twitter'
XCOM = 'x'
INSTAGRAM = 'instagram'
TIKTOK = "tiktok"
REDDIT = "reddit"
REGEXLINKS = f"{XCOM}|{TWITTER}|{INSTAGRAM}|{TIKTOK}|{REDDIT}"
def regexTwitterLinks(stringToRegex):
    #([\s\S]*?)(?P<LinkChecker>(?:http(?:s)?://)+(?:www.)?(?:x|twitter)\.com/(.\S*))([\s\S]*?)(?=(?:(?P=LinkChecker))|$) 
    #in theory this regex grabs all the floating text, and the after link message but I could not figure out how to get the groups to work in python
    return re.findall(f"(?:http(?:s)?)?://(?:www.)?((?:{REGEXLINKS})\\.com/.\\S*)", stringToRegex)
def getFormattedMessage(message, author):
    #Regex to find if the message has either a twitter link or an x.com link the * means any character after the domain
    if(regexTwitterLinks(message.content) != []):
        completeMessage = (f'{author} posted\n')
        freeMessages, unformattedLinks = regexFreeMessages(message.content)
        if(freeMessages != []):
            if(freeMessages[0] != ''):
                completeMessage += (f'{freeMessages[0]}')
                if(freeMessages[0][len(freeMessages[0])-1] != '\n'):
                    completeMessage += '\n'
        #if discord lets you put one spoil embed in with multiple non spoiler embeds, change the function "removeSpoiledMesages" into "spoiledSpoiledMessages"
        unformattedLinks = spoilSpoiledMessages(unformattedLinks, getSpoiledMessages(message))
        for singleLink in unformattedLinks:
            if((singleLink[:len(TWITTER)] == "twitter") and (singleLink[len(singleLink)-1] != "|")):
                completeMessage += (f'https://fx{singleLink}\n')
            elif((singleLink[:len(TWITTER)] == "twitter") and (singleLink[len(singleLink)-1] == "|")):
                completeMessage += (f'||https://fx{singleLink}\n')
            if((singleLink[:len(XCOM)] == "x") and (singleLink[len(singleLink)-1] != "|")):
                completeMessage += (f'https://fixup{singleLink}\n')
            elif((singleLink[:len(XCOM)] == "x") and (singleLink[len(singleLink)-1] == "|")):
                completeMessage += (f'||https://fx{singleLink }\n')
            if((singleLink[:len(INSTAGRAM)] == "instagram") and (singleLink[len(singleLink)-1] != "|")):
                completeMessage += (f'https://dd{singleLink}\n')
            elif((singleLink[:len(INSTAGRAM)] == "instagram") and (singleLink[len(singleLink)-1] == "|")):
                completeMessage += (f'||https://dd{singleLink}\n')
            if((singleLink[:len(TIKTOK)] == "tiktok") and (singleLink[len(singleLink)-1] != "|")):
                completeMessage += (f'https://vx{singleLink}\n')
            elif((singleLink[:len(TIKTOK)] == "tiktok") and (singleLink[len(singleLink)-1] == "|")):
                completeMessage += (f'||https://vx{singleLink}\n')
            if((singleLink[:len(REDDIT)] == "reddit") and (singleLink[len(singleLink)-1] != "|")):
                completeMessage += (f'https://rx{singleLink[2:]}\n')
            elif((singleLink[:len(REDDIT)] == "reddit") and (singleLink[len(singleLink)-1] == "|")):
                completeMessage += (f'||https://rx{singleLink[2:]}\n')
                
        if(completeMessage == ''):
            completeMessage = None
        return [completeMessage, freeMessages]
    
def regexFreeMessages(stringToRegex):
    match = re.findall(f"([\\s\\S]*?)(?:http(?:s)?://)+(?:www.)?((?:{REGEXLINKS})\\.com/.\\S*)([\\s\\S]*?)(?=(?:http(?:s)?://)+(?:www.)?(?:{REGEXLINKS})\\.com/.\\S*|$)([\\s\\S]*?)", stringToRegex)
    freeMessages = []
    twitterLinks = []
    for matchList in match:
        freeMessages.append(matchList[0])
        twitterLinks.append(matchList[1])
        freeMessages.append(matchList[2])
    countOfSpoilers = re.findall("\\|\\|", freeMessages[0])
    if(len(countOfSpoilers)%2 != 0):
        freeMessages[0] = (f"{freeMessages[0]}||")
    if (freeMessages != []):
        for message in freeMessages:
            if((message != '') and (message[len(message)- 1] == '|') and (message != freeMessages[0])): #please make this better, I don't need to check the first index b/c it is special
                messageIndex = freeMessages.index(message)
                freeMessages.remove(message)
                freeMessages.insert(messageIndex, f'||{message}')    
    return freeMessages, twitterLinks

    #awful bandaid fix
def getSpoiledMessages(message):
    spoiled = re.findall('\\|\\|.*?\\|\\|', message.content) #Grabs *any* message in spoiler tags
    completeSpoiledMessages = ''
    for spoiledMessage in spoiled:
        completeSpoiledMessages += spoiledMessage
    #makes the spoiler tag message into one string, I couldn't find their toString probably does exist
    return completeSpoiledMessages

def removeSpoiledMessages(unformattedLinks, spoiled):
    spoiledList = regexTwitterLinks(spoiled) #Grabs all twitter links in the spoiler tags (why in a separate function? b/c... idk)
    for link in spoiledList:
        if link in unformattedLinks:
            unformattedLinks.remove(link)
    return unformattedLinks

def spoilSpoiledMessages(unformattedLinks, spoiled):
    spoiledList = regexTwitterLinks(spoiled) #Grabs all twitter links in the spoiler tags (why in a separate function? b/c... idk)
    for link in spoiledList:
        if link in unformattedLinks:   
            spoiledLinkIndex = unformattedLinks.index(link)
            unformattedLinks.remove(link)
            if(link[len(link)-1] != "|"):
                unformattedLinks.insert(spoiledLinkIndex, (f'{link}||'))
            else:
                unformattedLinks.insert(spoiledLinkIndex, link)
                
    return unformattedLinks

def makeMessage(freeMessages):
    i = 1
    completeFreeMessage = ''
    for i in range(1,len(freeMessages)):
        completeFreeMessage += freeMessages[i]
    return completeFreeMessage

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    #Check's to make sure the bot doesn't respond to itself
    if message.author != client.user:
        if(regexTwitterLinks(message.content) != []):
            tupleCompleteAndFreeMessages = getFormattedMessage(message, message.author.display_name)
            if(tupleCompleteAndFreeMessages[0] != None): #This is important b/c I remove messages from removedSpoiledMessages()
                await asyncio.sleep(1) #Sleeps to help with the delay of when the picture embeds? :shrug:
                await message.edit(suppress=True) #Removes the embeds from the original message b/c y'know it's ugly
                await message.reply(tupleCompleteAndFreeMessages[0], allowed_mentions=discord.AllowedMentions.none(), silent = True) #Sends the message then, removes the mention so it doesn't @ the person
                if ((followUpMessage := makeMessage(tupleCompleteAndFreeMessages[1])) != ''):
                    await message.channel.send(followUpMessage)
            
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
                                botFollowUpContent = makeMessage(completeMessage[1])
                                if(botFollowUpContent != ''):
                                    await botFollowUpMessage.edit(content = botFollowUpContent, allowed_mentions = discord.AllowedMentions.none())
                                else:
                                    await botFollowUpMessage.delete()                                    
                            else:
                                await botFollowUpMessage.delete()
                    return
                                
                    
                    
client.run(open('TOKEN.bottoken','r').read())
