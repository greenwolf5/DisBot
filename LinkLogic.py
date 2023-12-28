import re
#The links the bot supports, in theory can add any link here as long as someone has made a variant that embeds better
TWITTER = 'twitter.com/'
XCOM = 'x.com/'
INSTAGRAM = 'instagram.com/'
TIKTOK = "tiktok.com/"
TIKTOK_TWO = "vm.tiktok.com/"
REDDIT = "reddit.com/"

#Probably could make this a for loop later
#All the links that the bot supports. must be done otherwise it won't be found in the regex
REGEXLINKS = f"{XCOM}|{TWITTER}|{INSTAGRAM}|{TIKTOK}|{TIKTOK_TWO}|{REDDIT}"
#https://regex101.com/r/Xnde5g/1

#These are the links that we are switching the links to.
TWITTER_LINK = "fxtwitter.com/"
XCOM_LINK = "fixupx.com/"
INSTAGRAM_LINK = "ddinstagram.com/"
TIKTOK_LINK = "vxtiktok.com/"
TIKTOK_TWO_LINK ="vxtiktok.com/t/"
REDDIT_LINK = "rxddit.com/"

#This dictonary pairs the og link and the new link together for easy searching.
linkDictionary = {}
linkDictionary[TWITTER] = TWITTER_LINK
linkDictionary[XCOM] = XCOM_LINK
linkDictionary[INSTAGRAM] = INSTAGRAM_LINK
linkDictionary[TIKTOK] = TIKTOK_LINK
linkDictionary[TIKTOK_TWO] = TIKTOK_TWO_LINK
linkDictionary[REDDIT] = REDDIT_LINK

#Simple method that returns all of the links found that are supported
def regexTwitterLinks(stringToRegex):
    #([\s\S]*?)(?P<LinkChecker>(?:http(?:s)?://)+(?:www.)?(?:x|twitter)\.com/(.\S*))([\s\S]*?)(?=(?:(?P=LinkChecker))|$) 
    #in theory this regex grabs all the floating text, and the after link message but I could not figure out how to get the groups to work in python
    return re.findall(f"(?:http(?:s)?)?://(?:www.)?((?:{REGEXLINKS}).\\S*)", stringToRegex)

#One of the most complicated methods as it returns two variables
#Complete Message, which is the message of who posted it, the first line said by the user, then all of the links
#FreeMessages, which is all of the lines said by the user that is *not* the links, including the first line.
def getFormattedMessage(message, author):
    #Regex to find if the message has either a twitter link or an x.com link the * means any character after the domain
    if(regexTwitterLinks(message.content) != []):
        completeMessage = (f'{author} posted\n')
        nonEmptyFreeMessages, unformattedLinks = regexFreeMessages(message.content)
        firstMessage = getFirstMessage(nonEmptyFreeMessages)
        if(firstMessage != None):
            completeMessage += firstMessage
        #if discord lets you put one spoil embed in with multiple non spoiler embeds, change the function "removeSpoiledMesages" into "spoiledSpoiledMessages"
        unformattedLinks = spoilSpoiledLinks(unformattedLinks, getSpoiledMessages(message))
        completeMessage += returnFormattedLink(unformattedLinks)
        if(completeMessage == ''):
            completeMessage = None
        return [completeMessage, nonEmptyFreeMessages]
 
#This grabs the first message from freeMessages, returns it to completeMessage, and then removes the first message from freeMessages
def getFirstMessage(freeMessages):
    tempString = ""
    if(freeMessages != []): 
            if(freeMessages[0] != ''):
                tempString = freeMessages[0]
                if(freeMessages[0][len(freeMessages[0])-1] != '\n'):
                    tempString += '\n'
                freeMessages.remove(freeMessages[0])
                return tempString

#This checks the links against the dictonary in order to get their proper new link
def returnFormattedLink(unformattedLinks):
    completeMessage = ""
    for singleLink in unformattedLinks:
            isSpoiled = False
            if(singleLink[len(singleLink)-1] == "|"):
                isSpoiled = True
            for originalWebsiteName in linkDictionary: 
                #This checks if link from the start to the length of the name matches; i.e if twitter.com/123 will match twitter by [:7]
                if((singleLink[:len(originalWebsiteName)] == originalWebsiteName)):
                    spoilPart = ""
                    if(isSpoiled):
                        spoilPart += "||"
                    completeMessage += (f'{spoilPart}https://{linkDictionary[originalWebsiteName]}{singleLink[len(originalWebsiteName):]}\n')
    return completeMessage
    
#The other most complicated method, as it returns two variables
#FreeMessages, which is all the lines said by the user
#Twitter links which is all of the links said by the user.
def regexFreeMessages(stringToRegex):
    #This regex is complicated; as it captures all lines before the link, and after the link, with no overlapping
    #match = re.findall(f"([\\s\\S]*?)(?:http(?:s)?://)+(?:www.)?((?:{REGEXLINKS}).\\S*)([\\s\\S]*?)(?=(?:http(?:s)?://)+(?:www.)?(?:{REGEXLINKS}).\\S*|$)([\\s\\S]*?)", stringToRegex)
    match = re.findall(r"([\s\S]*?)(?:http(?:s)?://)+(?:www.)?((?:twitter|x|reddit|instagram|tiktok|vm\.tiktok).\S*)([\s\S]*?)(?=(?:http(?:s)?://)+(?:www.)?(?:twitter|x|reddit|instagram|tiktok|vm\.tiktok).\S*|$)([\s\S]*?)", stringToRegex)
    regex = fr"([\s\S]*?)(?:http(?:s)?://)+(?:www.)?((?:{REGEXLINKS}).\S*)([\s\S]*?)(?=(?:http(?:s)?://)+(?:www.)?(?:{REGEXLINKS}).\S*|$)([\s\S]*?)"
    matches = re.finditer(regex, stringToRegex, re.MULTILINE)
    freeMessages = []
    twitterLinks = []
    lastMessages = []
    #There are 3 matches, all messages before the link, the link, then all messages after the link.
    for matchList in matches:
    #for matchNum, match in enumerate(matches, start=1):
        freeMessages.append(matchList[1])
        twitterLinks.append(matchList[2])
        freeMessages.append(matchList[3])
        endMessage = matchList[3]
        if(endMessage != '' and endMessage != "\n" and endMessage != ' ' and endMessage != "||\n||" and endMessage != "\n||" and endMessage != "||\n"):
            lastMessages.append(matchList[3])
    #Since you could spoil a link and a message in the same spoiler i.e ||x.com/213 this message is spoiled||
    #This checks if there's an uneven amount of spoiling as the spoiler text will get cut off as it'll be attatched to the link.
    countOfSpoilers = re.findall("\\|\\|", freeMessages[0])
    if(len(countOfSpoilers)%2 != 0):
        #This checks if there is an uneven spoiler amount, and only if the freeMessage[0] is greater than length of 2
        #Will it spoil it, because for case of... "||x.com/123 this is spoiled||" freeMessage[0] == || freeMessage[1] == " this is spoiled"
        #Since "||" is a useless message, it gets removed as the spoiling is handled elsewhere.
        if(len(freeMessages[0]) > 2):
            freeMessages[0] = (f"{freeMessages[0]}||")
        else:
            freeMessages[0] = ''
    if (freeMessages != []):
        #for message in freeMessages:
        #    if((message != '') and (message[len(message)- 1] == '|') and (message != freeMessages[0])): #please make this better, I don't need to check the first index b/c it is special
        #        messageIndex = freeMessages.index(message)
        #        freeMessages.remove(message)
        #        freeMessages.insert(messageIndex, f'||{message}')    
        nonEmptyFreeMessages = []
        for message in freeMessages:
            tempMessage = message
            #This line removes any new line characters that are caught if you do "x.com/123\nx.com/321" freemessage[1] will be \n which is useless to send
            if(message != '' and message != "\n" and message != ' ' and message != "||\n||" and message != "\n||" and message != "||\n"): #please make this better, I don't need to check the first index b/c it is special
                #At this point there are 4 cases: "not spoiled", "||start spoiled", "ends spoiled||", "||fully spoiled||"
                #Case #1 and case #4 can be ignored, but case #2 and #3 need to be checked for 
                
                #check if message ends in ||
                #if it starts with|| nothing
                #if it is in list of lastMessages nothing
                # !in list, then remove the last ||
                if(message[len(message)-2] == "|" and message[0] != "|" and not(message in lastMessages)): 
                    message = message[:len(message)-2]
                if((message[0] == '|')):
                    if(message[2:3] == "\n"):
                        message = message[0:1] + message[4:] 
                    if((message[len(message)-2]) != '|'):
                        if(message[len(message)-1:len(message)] == "\n"):
                            message = message[:len(message)-1]
                        messageIndex = freeMessages.index(tempMessage)
                        #tempMessage = message
                        #freeMessages.remove(message)
                        #freeMessages.insert(messageIndex, f'{tempMessage}||')    
                        nonEmptyFreeMessages.insert(messageIndex,f'{message}||')
                    else:
                        nonEmptyFreeMessages.insert(messageIndex,f'{message}')
                elif((message[len(message)-2]) == '|'):
                        if(message[0:1] == "\n"):
                            message = message[1:] 
                        if(message[len(message)-3:len(message)-2] == "\n"):
                            message = message[:len(message)-3] + message[len(message)-2:]
                        messageIndex = freeMessages.index(tempMessage)
                        #tempMessage = message
                        #freeMessages.remove(message)
                        #freeMessages.insert(messageIndex, f'||{tempMessage}')   
                        nonEmptyFreeMessages.insert(messageIndex,f'||{message}')
                else:
                        if(message[0:1] == "\n"):
                            message = message[1:] 
                        if(message[len(message)-1:] == "\n"):
                            message = message[:len(message)-1]
                        messageIndex = freeMessages.index(tempMessage)
                        nonEmptyFreeMessages.insert(messageIndex,f'{message}')
    return nonEmptyFreeMessages, twitterLinks

#Simple method that grabs every single message that is between spoiler. will grab 'freemessage' and 'singlelink' together in one message
def getSpoiledMessages(message):
    spoiled = re.findall('\\|\\|.*?\\|\\|', message.content) #Grabs *any* message in spoiler tags
    completeSpoiledMessages = ''
    for spoiledMessage in spoiled:
        completeSpoiledMessages += spoiledMessage
    #makes the spoiler tag message into one string, I couldn't find their toString probably does exist
    return completeSpoiledMessages

[DeprecationWarning]
#This will remove links from the message to be sent if they have been spoiled
#Depreciated as it got replaced with just sending a spoiled version with spoilSpoiledLinks
def removeSpoiledLinks(unformattedLinks, spoiled):
    spoiledList = regexTwitterLinks(spoiled) #Grabs all twitter links in the spoiler tags (why in a separate function? b/c... idk)
    for link in spoiledList:
        if link in unformattedLinks:
            unformattedLinks.remove(link)
    return unformattedLinks

#Simple method that grabs any links that are located in the spoilMessages, and ends them in a spoiler tag, putting them back in the same place in the list
def spoilSpoiledLinks(unformattedLinks, spoiled):
    spoiledList = regexTwitterLinks(spoiled) 
    for link in spoiledList:
        if link in unformattedLinks:   
            spoiledLinkIndex = unformattedLinks.index(link)
            unformattedLinks.remove(link)
            #in a situation like: "||https://x.com/123 how does this work?||" the link will be in spoiler tag, and not have the || at the end
            if(link[len(link)-1] != "|"):
                unformattedLinks.insert(spoiledLinkIndex, (f'{link}||'))
            #In a situation like: "||how does this work? https://x.com||" it already ends in a spoiler tag
            else:
                unformattedLinks.insert(spoiledLinkIndex, link)
    return unformattedLinks

#Simple method to format freeMessages, basically just to string and removes an unnessesary space
def formatFreeMessages(freeMessages):
    completeFreeMessage = ''
    for message in freeMessages:
        if(message != ""):
            if(message[0] == " "):
                completeFreeMessage += f"{message[1:]}\n"
            else:
                completeFreeMessage += f"{message}\n"
    return completeFreeMessage