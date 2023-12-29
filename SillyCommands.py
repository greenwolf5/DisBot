greenId = 150793267703840769
reshId = 378704627132006400
slyId = 158396544838664192
ponId = 243925562085736449
kodahn = 1064069125531500574
listKnownUsers = [greenId, reshId, slyId, ponId, kodahn]

keyWordDictionary = {}
responseDictonary = {}

keyWordDictionary[greenId] = ["bitch bot", "いただきます"]
responseDictonary[greenId] = ["You fuckin' called?\n", "How many do you simp for?!\n"]

keyWordDictionary[reshId] = ["hell yeah brother", "fr fr", "no cap", '<:SmugCat:784283846447202314>']
responseDictonary[reshId] = ["hell yeah indeed brother\n", "fr fr", "no cap", '<:SmugCat:784283846447202314>']

keyWordDictionary[slyId] = ["tldr"]
responseDictonary[slyId] = ["OH GOD NOT A SLY TLDR!"]

keyWordDictionary[ponId] = ["ope", "chipi chipi"]
responseDictonary[ponId] = ["ope", "https://tenor.com/view/chipi-chapa-chipi-chipi-chipi-chipi-cat-chipi-chipi-dancing-cat-gif-10997735880837555564"]

keyWordDictionary[kodahn] = ["oh shit", "chipi chipi"]
responseDictonary[kodahn] = ["shit oh?", "https://tenor.com/view/chipi-chapa-chipi-chipi-chipi-chipi-cat-chipi-chipi-dancing-cat-gif-10997735880837555564"]

def checkKnownUser(id):
    if(id in listKnownUsers):
        return True
    else:
        return False
    
def containsKeyword(message, id):
    listOfKeywords = keyWordDictionary[id]
    responseMessage = ""
    message = str.lower(message)
    for i in range(0,len(listOfKeywords)):
        if(message.__contains__(str.lower(listOfKeywords[i]))):
            responseMessage += f"{responseDictonary[id][i]} "
    return responseMessage

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