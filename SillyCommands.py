
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
sageId = int(config["USERS"]['SageId'])
listKnownUsers = [greenId, reshId, slyId, ponId, kodahnId, katId, jerbId, ashleyId,sageId]

keyWordDictionary = {}
responseDictonary = {}


uwuDict = ["<a:6728_DiscordUwU:679524982493020168>",
           "https://cdn.discordapp.com/attachments/1164308207733313586/1408269045534294038/image.png?ex=68a92040&is=68a7cec0&hm=13267cef467a10bc473a176be40d6ebdd11d91759102734c2bf0408686ea3455&",
           "https://media.discordapp.net/attachments/1164308207733313586/1408271170054262794/image.png?ex=68a9223b&is=68a7d0bb&hm=28ad4b617043ea807ed9fdc25b239bb28405cfe2999eee89678b02b168260a95&=&format=webp&quality=lossless",
           "https://media.discordapp.net/attachments/1164308207733313586/1408273374643359884/image.png?ex=68a92448&is=68a7d2c8&hm=3fb5d6c87db0ba7d85c524e0546c7f6624f06c3d7880ce3fc6142de89f918195&=&format=webp&quality=lossless",
           "https://media.discordapp.net/attachments/1164308207733313586/1408279902981062858/image.png?ex=68a92a5d&is=68a7d8dd&hm=420cc7234c3b8b799a0c3e1f56f5f7e794a6cb353cf1f12453bd8c306f9e6783&=&format=webp&quality=lossless",
           "https://media.discordapp.net/attachments/635667155320569856/1410049332945621074/image.png?ex=68af9a46&is=68ae48c6&hm=3d8281a8c1e122f0238dc967d52dc4fde4c33eefec86c5f55ba53ece917f9265&=&format=webp&quality=lossless",
           "https://media.discordapp.net/attachments/1164308207733313586/1410051672272539788/image.png?ex=68af9c74&is=68ae4af4&hm=f9901fe60d81bde11145a04cb6aea9efb3420edc194bf7345edcf11eab037cf0&=&format=webp&quality=lossless",
           "https://cdn.discordapp.com/attachments/1164308207733313586/1431673874814341311/image.png?ex=68fe45b2&is=68fcf432&hm=65790bd9c26da0478a3c5cb1974df393cbff1906f7f6b00e931dd10d7044751e&"]

keyWordDictionary[0] = ["jerby","Chaos","Skill issue",'uwu',"Shit","yr'oue"]
responseDictonary[0] = [[False, jerbId, ["https://media.discordapp.net/attachments/1096302219990663289/1406668974611239082/image.png?ex=68a34e12&is=68a1fc92&hm=1de68b6091f812cc1a83bddfef4d6fc31a3c57cc4ac7f38c6ddbc5bad14e6170&=&format=webp&quality=lossless"]],[False,0,["https://tenor.com/bIkyP.gif"]],[True,0,["<:childeSkillIssue:939656128684498994>"]],[False,0,uwuDict],[True,0,[[50,"<:letsfuckingshit:1221664187797868634>"]]],[False,0,["https://images-ext-1.discordapp.net/external/BdI9_cMx6oXrm8vkX84ac_IZ7E3QLnMKX_KxDxEg8qo/https/media.tenor.com/8JitADa-FIAAAAPo/youre-your.mp4"]]]

keyWordDictionary[greenId] = ["bitch bot", "いただきます", '<a:SilvervaleGasms:1040264733737095299>',"お前はゲーだよ","skill issueだよ","おっぱい","しょうがない","残念だ","ザーコ","太ももを見て！"]
responseDictonary[greenId] = ["You fuckin' called?\n", "Fucking simp\n", [True, '<:WTF:637454072164646922>'],"He called you gay btw","(you have a skill issue)","Yeah I'm not translating that one","It can't be helped","What a shame","Noob","Pon look, there's thighs!"]

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
responseDictonary[ashleyId] = ["SHE SAID OPE!"]

keyWordDictionary[sageId] = ["Ope"]
responseDictonary[sageId] = ["SHE SAID OPE!"]


def checkKnownUser(id):
    if(id in listKnownUsers):
        return True
    else:
        return False
    
def containsKeyword(message, id):
    message = str.lower(message)
    isReaction = False
    passCheck = False
    responseMessage = ""
    listOfKeywords = keyWordDictionary[0]
    for i in range(0,len(listOfKeywords)):
        if(isinstance(listOfKeywords[i],str)):
            if(message.__contains__(str.lower(listOfKeywords[i]))):
                passCheck = True
        if(passCheck):
            if(responseDictonary[0][i][1] != id):
                random_number = random.randint(1,len(responseDictonary[0][i][2]))
                random_number = random_number - 1
                if(isinstance(responseDictonary[0][i][2][random_number][0], int)):
                    random_number2 = random.randint(1,responseDictonary[0][i][2][random_number][0])
                    if(random_number2 == responseDictonary[0][i][2][random_number][0]):
                        isReaction = responseDictonary[0][i][0]
                        responseMessage += responseDictonary[0][i][2][random_number][1]
                        return responseMessage, isReaction
                    else:
                        return "", False
                else:
                    isReaction = responseDictonary[0][i][0]
                    responseMessage += f"{responseDictonary[0][i][2][random_number]}"
                    return responseMessage, isReaction
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