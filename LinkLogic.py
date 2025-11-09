import re
#The links the bot supports, in theory can add any link here as long as someone has made a variant that embeds better
TWITTER = 'twitter.com/'
XCOM = 'x.com/'
INSTAGRAM = 'instagram.com/'
TIKTOK = "tiktok.com/"
TIKTOK_TWO = "vm.tiktok.com/"
REDDIT = "reddit.com/"
PIXIV = "pixiv.net/"

#Probably could make this a for loop later
#All the links that the bot supports. must be done otherwise it won't be found in the regex
REGEXLINKS = f"{XCOM}|{TWITTER}|{INSTAGRAM}|{TIKTOK}|{TIKTOK_TWO}|{REDDIT}|{PIXIV}"
#https://regex101.com/r/Xnde5g/1

#These are the links that we are switching the links to.
TWITTER_LINK = "fxtwitter.com/"
XCOM_LINK = "fixupx.com/"
INSTAGRAM_LINK = "www.d.vxinstagram.com/"
TIKTOK_LINK = "d.tnktok.com/"
TIKTOK_TWO_LINK ="d.tnktok.com/"
REDDIT_LINK = "redditez.com/"
PIXIV_LINK = "phixiv.net/"

#This dictonary pairs the og link and the new link together for easy searching.
linkDictionary = {}
linkDictionary[TWITTER] = TWITTER_LINK
linkDictionary[XCOM] = XCOM_LINK
linkDictionary[INSTAGRAM] = INSTAGRAM_LINK
linkDictionary[TIKTOK] = TIKTOK_LINK
linkDictionary[TIKTOK_TWO] = TIKTOK_TWO_LINK
linkDictionary[REDDIT] = REDDIT_LINK
linkDictionary[PIXIV] = PIXIV_LINK

#Simple method that returns all of the links found that are supported
def regexTwitterLinks(stringToRegex):
    #([\s\S]*?)(?P<LinkChecker>(?:http(?:s)?://)+(?:www.)?(?:x|twitter)\.com/(.\S*))([\s\S]*?)(?=(?:(?P=LinkChecker))|$) 
    #in theory this regex grabs all the floating text, and the after link message but I could not figure out how to get the groups to work in python
    return re.findall(fr"(?:http(?:s)?)?://(?:www\.)?((?:{REGEXLINKS})[^\r\n\t\f\v| ]*)", stringToRegex)

#One of the most complicated methods as it returns two variables
#Complete Message, which is the message of who posted it, the first line said by the user, then all of the links
#FreeMessages, which is all of the lines said by the user that is *not* the links, including the first line.
def getFormattedMessage(message, author):
    #Regex to find if the message has either a twitter link or an x.com link the * means any character after the domain
    if(regexTwitterLinks(message.content) != []):
        completeMessage = (f'{author} posted\n')
        nonEmptyFreeMessages, unformattedLinks = regexLinesIntoList(message.content)
        firstMessage = getFirstMessage(nonEmptyFreeMessages)
        if(firstMessage != None):
            completeMessage += firstMessage
        #if discord lets you put one spoil embed in with multiple non spoiler embeds, change the function "removeSpoiledMesages" into "spoiledSpoiledMessages"
        unformattedLinks = spoilSpoiledLinks(unformattedLinks, getSpoiledMessages(message.content))
        completeMessage += returnFormattedLinks(unformattedLinks)
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
def returnFormattedLinks(unformattedLinks):
    completeMessage = ""
    shortedLink = ""
    for singleLink in unformattedLinks:
            isSpoiled = False
            if(singleLink[len(singleLink)-1] == "|"):
                isSpoiled = True
            for originalWebsiteName in linkDictionary: 
                #This checks if link from the start to the length of the name matches; i.e if twitter.com/123 will match twitter by [:7]
                shortedLink = f"[{originalWebsiteName}]"
                if((singleLink[:len(originalWebsiteName)] == originalWebsiteName)):
                    spoilPart = ""
                    if(isSpoiled):
                        spoilPart += "||"
                        shortedLink = "||"+shortedLink+"||"
                    completeMessage += (f'{shortedLink}({spoilPart}https://{linkDictionary[originalWebsiteName]}{singleLink[len(originalWebsiteName):]})\n')
    return completeMessage
    
#This is made for the /embed command
def returnSingleLink(singleLink):
    splitLink = re.split("[ ,]",singleLink) #'single link' is legacy, this is to allow multiple separated by spaces (or I guess comma's too?) i.e x.com/321 x.com/321
    returnedString = ""
    for singledLink in splitLink:
        for originalWebsiteName in linkDictionary: 
                #This checks if link from the start to the length of the name matches; i.e if twitter.com/123 will match twitter by [:7]
                if(originalWebsiteName in singledLink):
                    returnedString += (f'[{originalWebsiteName}](https://{linkDictionary[originalWebsiteName]}{singledLink[len(originalWebsiteName)+8:]})\n')
    return returnedString
    
#This is made for the /spoil command            
def returnSpoiledSingleLink(singleLink):
    splitLink = re.split("[ ,]",singleLink) #'single link' is legacy, this is to allow multiple separated by spaces (or I guess comma's too?) i.e x.com/321 x.com/321
    returnedString = ""
    for singledLink in splitLink:
        for originalWebsiteName in linkDictionary: 
                #This checks if link from the start to the length of the name matches; i.e if twitter.com/123 will match twitter by [:7]
                if(originalWebsiteName in singledLink):
                    returnedString += (f'||[{originalWebsiteName}](https://{linkDictionary[originalWebsiteName]}{singledLink[len(originalWebsiteName)+8:]})||\n')
    return returnedString
#The other most complicated method, as it returns two variables
#FreeMessages, which is all the lines said by the user
#Twitter links which is all of the links said by the user.
[DeprecationWarning]
def regexFreeMessages(stringToRegex):
    #This regex is complicated; as it captures all lines before the link, and after the link, with no overlapping
    regex = fr"([\s\S]*?)(?:http(?:s)?://)+(?:www.)?((?:{REGEXLINKS}).\S*)([\s\S]*?)(?=(?:http(?:s)?://)+(?:www.)?(?:{REGEXLINKS}).\S*|$)([\s\S]*?)"
    matches = re.finditer(regex, stringToRegex, re.MULTILINE)
    freeMessages = []
    twitterLinks = []
    #lastMessages = []
    #There are 3 matches, all messages before the link, the link, then all messages after the link.
    for matchList in matches:
        freeMessages.append(matchList[1])
        twitterLinks.append(matchList[2])
        freeMessages.append(matchList[3])
        #endMessage = matchList[3]
        #if(endMessage != '' and endMessage != "\n" and endMessage != ' ' and endMessage != "||\n||" and endMessage != "\n||" and endMessage != "||\n"):
        #    lastMessages.append(matchList[3])
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
        nonEmptyFreeMessages = []
        for message in freeMessages:
            #This line removes any new line characters that are caught if you do "x.com/123\nx.com/321" freemessage[1] will be \n which is useless to send
            if(message != '' and message != "\n" and message != ' ' and message != "||\n||" and message != "\n||" and message != "||\n"): #please make this better, I don't need to check the first index b/c it is special
                regexSplit = re.split(r"\W+", message)                
                noBadSpaces = " ".join(regexSplit)
                if(noBadSpaces[0] == ' '):
                    noBadSpaces = noBadSpaces[1:]
                if(noBadSpaces[len(noBadSpaces)-1] == ' '):
                    noBadSpaces = noBadSpaces[:len(noBadSpaces)-1]
                nonEmptyFreeMessages.append(noBadSpaces)
        listFreeMessages = getSpoiledFreeMessages(stringToRegex)
        nonEmptyFreeMessages = fixSpoiledMessages(listFreeMessages, nonEmptyFreeMessages)
    return nonEmptyFreeMessages, twitterLinks

def regexLinesIntoList(stringToRegex):
        twitterLinks = []
        freeMessages = []
        testList = stringToRegex.split("\n")
        firstTime = True
        for line in testList:
            if(line.__contains__("http")):
                regex = fr"([\s\S]*?)(?:http(?:s)?://)+(?:www.)?((?:{REGEXLINKS}).\S*)([\s\S]*?)(?=(?:http(?:s)?://)+(?:www.)?(?:{REGEXLINKS}).\S*|$)([\s\S]*?)"
                matches = re.finditer(regex, line, re.MULTILINE)
                for matchList in matches:
                    if(matchList[1] != '' and matchList[1] != '||'):
                        freeMessages.append(matchList[1])
                    elif(firstTime):
                        freeMessages.append('')
                    twitterLinks.append(matchList[2])
                    if(matchList[3] != '' and matchList[3] != '||'):
                        freeMessages.append(matchList[3])
            else:
                #message = re.findall(r'.*', line)
                freeMessages.append(line)
            firstTime = False
                
        nonEmptyFreeMessages = []
        for message in freeMessages:    
            if(message != '' and message != "\n" and message != ' ' and message != "||\n||" and message != "\n||" and message != "||\n" and message != "||" and message != " ||" and message != "|| "): #please make this better, I don't need to check the first index b/c it is special
                regexSplit = re.split(r" |\|", message)                
                noBadSpaces = ""
                for word in regexSplit:
                    if word != "":
                        noBadSpaces += word + " "
                if(noBadSpaces[len(noBadSpaces)-1] == ' '):
                    noBadSpaces = noBadSpaces[:len(noBadSpaces)-1]
                nonEmptyFreeMessages.append(noBadSpaces)
            if(message == ''):
                #in theory, this will only ever happen on the first time, as empty messages are already filtered out
                #the first index being empty means there is no message that comes before the first link- keeping the order
                nonEmptyFreeMessages.append(message)
        listFreeMessages = getSpoiledFreeMessages(stringToRegex)
        nonEmptyFreeMessages = fixSpoiledMessages(listFreeMessages, nonEmptyFreeMessages)
        return nonEmptyFreeMessages, twitterLinks

#Simple method that grabs every single message that is between spoiler. will grab 'freemessage' and 'singlelink' together in one message
def getSpoiledMessages(content):
    spoiled = returnSpoiledList(content)
    completeSpoiledMessages = ''
    for spoiledMessage in spoiled:
        completeSpoiledMessages += spoiledMessage
    #makes the spoiler tag message into one string, I couldn't find their toString probably does exist
    return completeSpoiledMessages

def returnSpoiledList(content):
     spoiled = re.findall('\\|\\|.*?\\|\\|', content) #Grabs *any* message in spoiler tags
     return spoiled

def getSpoiledFreeMessages(content):
    spoiledMessages = returnSpoiledList(content)
    freeMessageList = []
    for message in spoiledMessages:
        if(message[0] == "|" and message[len(message) -1 ] != "|"):
            message = message[2:]
        elif(message[0] != "|" and message[len(message) -1 ] == "|"):
            message = message[:len(message) -2]
        elif(message[0] == "|" and message[len(message) -1 ] == "|"):
            message = message[2:len(message) -2]
        if(message.__contains__("http")):
            separateByWords = message.split()
            if(len(separateByWords) > 1):
                for word in separateByWords:    
                    if(word.__contains__("http")):
                        separateByWords.remove(word)
                message = " ".join(separateByWords)          
                freeMessageList.append(message)
        else:
            freeMessageList.append(message) 
    return freeMessageList
    
def fixSpoiledMessages(listFreeMessages, nonEmptyFreeMessages):
    for sentence in listFreeMessages:
        if(sentence in nonEmptyFreeMessages):
            index = nonEmptyFreeMessages.index(sentence)
            nonEmptyFreeMessages.remove(sentence)
            nonEmptyFreeMessages.insert(index, f"||{sentence}||")
    return nonEmptyFreeMessages

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
 