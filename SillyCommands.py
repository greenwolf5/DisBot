
import configparser
import random
config = configparser.ConfigParser()
config.read('config.ini')
greenId = int(config['USERS']['GreenId'])
reshId = int(config['USERS']['ReshId'])
slyId = int(config['USERS']['SlyId'])
ponId = int(config['USERS']['PonId'])
kodahnId = int(config['USERS']['KodahnId'])
katId = int(config['USERS']['KatId'])
jerbId = int(config['USERS']['JerbId'])
ashleyId = int(config["USERS"]['AshleyId'])
listKnownUsers = [greenId, reshId, slyId, ponId, kodahnId, katId, jerbId,ashleyId]

keyWordDictionary = {}
responseDictonary = {}

keyWordDictionary[0] = ["jerby","Chaos","Skill issue",'uwu',"Shit"]
responseDictonary[0] = [[False, jerbId, ["https://media.discordapp.net/attachments/1096302219990663289/1406668974611239082/image.png?ex=68a34e12&is=68a1fc92&hm=1de68b6091f812cc1a83bddfef4d6fc31a3c57cc4ac7f38c6ddbc5bad14e6170&=&format=webp&quality=lossless"]],[False,0,["https://images-ext-1.discordapp.net/external/fqP6WElHyUq2-mCKklSVdTQlYGUQ0kNcmd8mT71mElU/https/media.tenor.com/z_KoI0-y7rEAAAPo/chaos.mp4"]],[True,0,"<:childeSkillIssue:939656128684498994>"],[False,0,["<a:6728_DiscordUwU:679524982493020168>","https://cdn.discordapp.com/attachments/1164308207733313586/1408269045534294038/image.png?ex=68a92040&is=68a7cec0&hm=13267cef467a10bc473a176be40d6ebdd11d91759102734c2bf0408686ea3455&","https://media.discordapp.net/attachments/1164308207733313586/1408271170054262794/image.png?ex=68a9223b&is=68a7d0bb&hm=28ad4b617043ea807ed9fdc25b239bb28405cfe2999eee89678b02b168260a95&=&format=webp&quality=lossless"]],[True,0,"<:letsfuckingshit:1221664187797868634>"]]

keyWordDictionary[greenId] = ["bitch bot", "いただきます", '<a:SilvervaleGasms:1040264733737095299>',"<a:HUH:1049736597551194162>"]
responseDictonary[greenId] = ["You fuckin' called?\n", "Fucking simp\n", [True, '<:WTF:637454072164646922>'],"<:uneedjesus:662380798279680013>"]

keyWordDictionary[reshId] = ["hell yeah brother", "frfr", "on god", "no cap", "straight facts", "bruh", '<:SmugCat:784283846447202314>']
responseDictonary[reshId] = ["hell yeah indeed brother\n", "frfr", "on god", "no cap", "straight facts", "bruh", [True, '<:SmugCat:784283846447202314>']]

keyWordDictionary[slyId] = ["tldr"]
responseDictonary[slyId] = ["OH GOD NOT A SLY TLDR!"]

keyWordDictionary[ponId] = ["ope", "chipi chipi","Sat rex","Little shit"]
responseDictonary[ponId] = ["HE SAID OPE!", "https://tenor.com/view/chipi-chapa-chipi-chipi-chipi-chipi-cat-chipi-chipi-dancing-cat-gif-10997735880837555564","https://tenor.com/view/jane-doe-zenless-zone-zero-gif-16720528248315404314", "yeah, you tell 'em!"]

keyWordDictionary[kodahnId] = ["oh shit", "chipi chipi", '🫠', "nini","fix pls"]
responseDictonary[kodahnId] = ["shit oh?", "https://tenor.com/view/chipi-chapa-chipi-chipi-chipi-chipi-cat-chipi-chipi-dancing-cat-gif-10997735880837555564", [True, '🫠'], "https://tenor.com/view/have-a-nice-day-good-sunday-gif-1674652217239459225","how about you get off instagram, nerd"]

keyWordDictionary[katId] = ["chipi chipi"]
responseDictonary[katId] = ["https://tenor.com/view/chipi-chapa-chipi-chipi-chipi-chipi-cat-chipi-chipi-dancing-cat-gif-10997735880837555564"]

keyWordDictionary[jerbId] = []
responseDictonary[jerbId] = []

keyWordDictionary[ashleyId] = ["Ope"]
keyWordDictionary[ashleyId] = ["SHE SAID OPE!"]

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
                    random_number = random.randint(1,len(responseDictonary[0][i][2]))
                    random_number = random_number - 1
                    responseMessage += f"{responseDictonary[0][i][2][random_number]}"
                else:
                    isReaction = True
                    responseMessage = f"{responseDictonary[0][i][2]}" 
    if(responseMessage == ""):    
        listOfKeywords = keyWordDictionary[id]
        for i in range(0,len(listOfKeywords)):
            if(message.__contains__(str.lower(listOfKeywords[i]))):
                if(responseDictonary[id][i][0] != True):
                    responseMessage += f"{responseDictonary[id][i]}"
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