# This example requires the 'message_content' intent.

import discord
import datetime
import re
import asyncio
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

## Bug found, if a link is spoilered, it will still show link, check to see if the message has a || and if it does, check if a link is between the other ||

#Websites that help
#https://regex101.com/r/BFJBpZ/1 regex help
#https://discordpy.readthedocs.io/en/latest/api.html discord.py doc

#Two domains this works on not modular to add a new domain but not too difficult
twitter = 'https://twitter.'
xcom = 'https://x.'

def getFormattedMessage(message):
    #Regex to find if the message has either a twitter link or an x.com link the * means any character after the domain
    if (linkSubstring := re.findall(f'{twitter}.\S*|{xcom}.\S*', message.content)) != []:
        completeMessage = ''
        for singleString in linkSubstring:
            #Check if link is twitter or x.com, would need to add another elif for a new domain
            if re.findall(f'{twitter}.*', singleString) != []:
                singleString = singleString[len(twitter):]
            else:
                singleString = singleString[len(xcom):]
            #Add the fx link to the message
            completeMessage += 'https://fxtwitter.' + singleString + '\n'
        return completeMessage

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    #Check's to make sure the bot doesn't respond to itself
    if message.author == client.user:
        return
    if(completeMessage := getFormattedMessage(message)) != None:
        return
    completeMessage = "@silent" + completeMessage
    if(completeMessage != None):
        await asyncio.sleep(1) #Sleeps to help with the delay of when the picture embeds? :shrug:
        await message.edit(suppress=True) #Removes the embeds from the original message b/c y'know it's ugly
        await message.reply(completeMessage, allowed_mentions=discord.AllowedMentions.none()) #Sends the message then, removes the mention so it doesn't @ the person

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
        if (re.findall(f'{twitter}.\S*|{xcom}.\S*', message.content)) != []:
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
    if(editedMessage.created_at > (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(seconds=2))): # 
        return
    if (re.findall(f'{twitter}.\S*|{xcom}.\S*', editedMessage.content)) != []:
            async for postMessages in editedMessage.channel.history(limit = 2, after = editedMessage):
                if postMessages.author == client.user:
                    completeMessage = getFormattedMessage(editedMessage)
                    if(completeMessage != None):
                        await postMessages.edit(content = completeMessage, allowed_mentions=discord.AllowedMentions.none())
                        
client.run(open('TOKEN.bottoken','r').read())
