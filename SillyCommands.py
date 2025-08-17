
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
greenId = int(config['USERS']['GreenId'])
reshId = int(config['USERS']['ReshId'])
slyId = int(config['USERS']['SlyId'])
ponId = int(config['USERS']['PonId'])
kodahnId = int(config['USERS']['KodahnId'])
katId = int(config['USERS']['KatId'])
jerbId = int(config['USERS']['JerbId'])
listKnownUsers = [greenId, reshId, slyId, ponId, kodahnId, katId]

keyWordDictionary = {}
responseDictonary = {}

keyWordDictionary[0] = ["jerby"]
responseDictonary[0] = [[False, jerbId, "https://media.discordapp.net/attachments/1096302219990663289/1406668974611239082/image.png?ex=68a34e12&is=68a1fc92&hm=1de68b6091f812cc1a83bddfef4d6fc31a3c57cc4ac7f38c6ddbc5bad14e6170&=&format=webp&quality=lossless"]]

keyWordDictionary[greenId] = ["bitch bot", "いただきます", '<a:SilvGasms:1040264733737095299>']
responseDictonary[greenId] = ["You fuckin' called?\n", "Fucking simp\n", [True, '<:WTF:637454072164646922>']]

keyWordDictionary[reshId] = ["hell yeah brother", "frfr", "on god", "no cap", "straight facts", "bruh", '<:SmugCat:784283846447202314>']
responseDictonary[reshId] = ["hell yeah indeed brother\n", "frfr", "on god", "no cap", "straight facts", "bruh", [True, '<:SmugCat:784283846447202314>']]

keyWordDictionary[slyId] = ["tldr"]
responseDictonary[slyId] = ["OH GOD NOT A SLY TLDR!"]

keyWordDictionary[ponId] = ["ope", "chipi chipi"]
responseDictonary[ponId] = ["HE SAID OPE!", "https://tenor.com/view/chipi-chapa-chipi-chipi-chipi-chipi-cat-chipi-chipi-dancing-cat-gif-10997735880837555564"]

keyWordDictionary[kodahnId] = ["oh shit", "chipi chipi", '🫠', "nini","fix pls"]
responseDictonary[kodahnId] = ["shit oh?", "https://tenor.com/view/chipi-chapa-chipi-chipi-chipi-chipi-cat-chipi-chipi-dancing-cat-gif-10997735880837555564", [True, '🫠'], "https://tenor.com/view/have-a-nice-day-good-sunday-gif-1674652217239459225","how about you get off instagram, nerd"]

keyWordDictionary[katId] = ["chipi chipi"]
responseDictonary[katId] = ["https://tenor.com/view/chipi-chapa-chipi-chipi-chipi-chipi-cat-chipi-chipi-dancing-cat-gif-10997735880837555564"]

def checkKnownUser(id):
    if(id in listKnownUsers):
        return True
    else:
        return False
    
def containsKeyword(message, id):
    message = str.lower(message)
    isReaction = False
    responseMessage = ""
    listOfKeywords = keyWordDictionary[0]
    for i in range(0,len(listOfKeywords)):
        if(message.__contains__(str.lower(listOfKeywords[i]))):
            if(responseDictonary[0][i][1] != id):
                if(responseDictonary[0][i][0] != True):
                    responseMessage += f"{responseDictonary[0][i][2]} "
                else:
                    isReaction = True
                    responseMessage = f"{responseDictonary[0][i][2]}" 
    if(responseMessage == ""):    
        listOfKeywords = keyWordDictionary[id]
        for i in range(0,len(listOfKeywords)):
            if(message.__contains__(str.lower(listOfKeywords[i]))):
                if(responseDictonary[id][i][0] != True):
                    responseMessage += f"{responseDictonary[id][i]} "
                else:
                    isReaction = True
                    responseMessage = f"{responseDictonary[id][i][1]}" 
        return responseMessage, isReaction
    else:
        return responseMessage, isReaction

#How go about saving keyWords and responses?
#I want something like 
#listOfKeywords = []
#responseMessage = ""
#for keyWord in listOfKeyWords
#if(message.__contains__(keyWord)):
#responseMessage += 


"""#I want:
# A list that has a key, preferibly user
# The value can be all the keywords attatched to that user
# i.e key: greenId, value = ["bitch bot", "いただきます"]
# Then how response? I could do greenId_bitch bot
# but spaces will ruin that idea if the message has one hmm...
# Maybe I have the responseList be key greenId, value match index: ["You fuckin' called?", "Stop simping already"]
# """