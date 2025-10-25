
import configparser
import random
from typing import List, Tuple
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

class KeywordObject:
    def __init__(self):
        pass
class ResponseObject:
    def __init__(self, WhoCanTrigger: int, ListOfTriggers: list ,ListOfResponses: list, IsReaction = False, ProbabilityForResponse = 1, IdToIgnore = 0):
        self.WhoCanTrigger = WhoCanTrigger
        self.ListOfTriggers = ListOfTriggers
        self.ListOfResponses = ListOfResponses
        self.IsReaction = IsReaction
        self.ProbabilityForResponse = ProbabilityForResponse
        self.IdToIgnore = IdToIgnore
#?, IdToIgnore, List of responses, probability for a response

uwuDict = ["<a:6728_DiscordUwU:679524982493020168>",
           "https://cdn.discordapp.com/attachments/1164308207733313586/1408269045534294038/image.png?ex=68a92040&is=68a7cec0&hm=13267cef467a10bc473a176be40d6ebdd11d91759102734c2bf0408686ea3455&",
           "https://media.discordapp.net/attachments/1164308207733313586/1408271170054262794/image.png?ex=68a9223b&is=68a7d0bb&hm=28ad4b617043ea807ed9fdc25b239bb28405cfe2999eee89678b02b168260a95&=&format=webp&quality=lossless",
           "https://media.discordapp.net/attachments/1164308207733313586/1408273374643359884/image.png?ex=68a92448&is=68a7d2c8&hm=3fb5d6c87db0ba7d85c524e0546c7f6624f06c3d7880ce3fc6142de89f918195&=&format=webp&quality=lossless",
           "https://media.discordapp.net/attachments/1164308207733313586/1408279902981062858/image.png?ex=68a92a5d&is=68a7d8dd&hm=420cc7234c3b8b799a0c3e1f56f5f7e794a6cb353cf1f12453bd8c306f9e6783&=&format=webp&quality=lossless",
           "https://media.discordapp.net/attachments/635667155320569856/1410049332945621074/image.png?ex=68af9a46&is=68ae48c6&hm=3d8281a8c1e122f0238dc967d52dc4fde4c33eefec86c5f55ba53ece917f9265&=&format=webp&quality=lossless",
           "https://media.discordapp.net/attachments/1164308207733313586/1410051672272539788/image.png?ex=68af9c74&is=68ae4af4&hm=f9901fe60d81bde11145a04cb6aea9efb3420edc194bf7345edcf11eab037cf0&=&format=webp&quality=lossless",
           "https://cdn.discordapp.com/attachments/1164308207733313586/1431673874814341311/image.png?ex=68fe45b2&is=68fcf432&hm=65790bd9c26da0478a3c5cb1974df393cbff1906f7f6b00e931dd10d7044751e&"]

everyoneDictionary = [
        #Everyone
    ResponseObject(0, ["jerby"],["https://media.discordapp.net/attachments/1096302219990663289/1406668974611239082/image.png?ex=68a34e12&is=68a1fc92&hm=1de68b6091f812cc1a83bddfef4d6fc31a3c57cc4ac7f38c6ddbc5bad14e6170&=&format=webp&quality=lossless"],False, 100,jerbId),
    ResponseObject(0, ["Chaos"],["https://tenor.com/bIkyP.gif"]),
    ResponseObject(0, ["Skill issue"],["<:childeSkillIssue:939656128684498994>"],True),
    ResponseObject(0, ["uwu"],uwuDict),
    ResponseObject(0, ["Shit"],["<:letsfuckingshit:1221664187797868634>"],True,50),
    ResponseObject(0, ["yr'oue"],["https://tenor.com/view/youre-your-gif-22328611"]),
]
testDictionary = [
    #Green
    ResponseObject(greenId, ["bitch bot"],["You fuckin' called?"]),
    ResponseObject(greenId, ["いただきます"],["Fucking simp"]),
    ResponseObject(greenId, ['<a:SilvervaleGasms:1040264733737095299>'],['<:WTF:637454072164646922>'],True),
    ResponseObject(greenId, ["お前はゲーだよ"],["He called you gay btw"], False),
    ResponseObject(greenId, ["skill issueだよ","スキールイッシューだよ","スキール問題だよ"],["(you have a skill issue)"]),
    ResponseObject(greenId, ["おっぱい"],["Yeah, I'm not translating that one","You can translate that one yourself","..."]),
    ResponseObject(greenId, ["しょうがない"],["It can't be helped"]),
    ResponseObject(greenId, ["残電だ"],["What a shame","Unfortunate"]),
    ResponseObject(greenId, ["ザーコ"],["Noob"],False),
    ResponseObject(greenId, ["太ももを見て","太もも見て"],["Look, thighs!"]),

    #Resh
    ResponseObject(reshId, ["hell yeah brother"],["hell yeah indeed brother"]),
    ResponseObject(reshId, ["frfr"],["frfr"]),
    ResponseObject(reshId, ["on god"], ["on god"]),
    ResponseObject(reshId, ["no cap"],["no cap"]),
    ResponseObject(reshId, ["straight facts"],["straight facts"]),
    ResponseObject(reshId, ["bruh"],["bruh"]),
    ResponseObject(reshId, ['<:SmugCat:784283846447202314>',],['<:SmugCat:784283846447202314>'],True),
    ResponseObject(reshId, ["67"],["🤮"]),

    #Sly
    ResponseObject(slyId, ["tldr"],["OH GOD NOT A SLY TLDR!"]),

    #Pon
    ResponseObject(ponId, ["ope"],["HE SAID OPE!"]),
    ResponseObject(ponId, ["chipi chipi"],["https://tenor.com/view/chipi-chapa-chipi-chipi-chipi-chipi-cat-chipi-chipi-dancing-cat-gif-10997735880837555564"]),
    ResponseObject(ponId, ["Sat rex"], ["https://tenor.com/view/jane-doe-zenless-zone-zero-gif-16720528248315404314"]),
    ResponseObject(ponId, ["Little shit"], ["Yeah, you tell 'em!"]),

    #Kodahn
    ResponseObject(kodahnId, ["oh shit"], ["shit oh?"]),
    ResponseObject(kodahnId, ["chipi chipi"], ["https://tenor.com/view/chipi-chapa-chipi-chipi-chipi-chipi-cat-chipi-chipi-dancing-cat-gif-10997735880837555564"]),
    ResponseObject(kodahnId, ["🫠"],["🫠"],True),
    ResponseObject(kodahnId, ["nini"], ["https://tenor.com/view/have-a-nice-day-good-sunday-gif-1674652217239459225"]),
    ResponseObject(kodahnId, ["fix plz"],["How about you get off instagram, you nerd"]),

    #Kat
    ResponseObject(katId, ["chipi chipi"], ["https://tenor.com/view/chipi-chapa-chipi-chipi-chipi-chipi-cat-chipi-chipi-dancing-cat-gif-10997735880837555564"]),

    #Ashley
    ResponseObject(ashleyId, ["Ope"], ["SHE SAID OPE!"]),

    #Sage
    ResponseObject(sageId, ["Ope"], ["SHE SAID OPE"]),
    ]


def containsKeyword2(message, id):
    message = message.lower()
    response = ""
    isReaction = False
    # check everyone
    for i in range(len(everyoneDictionary)):
        resp, is_reaction = FindResponseHelper(message, everyoneDictionary, i)
        if resp:
            return resp, is_reaction
    # check user-specific
    for i in range(len(testDictionary)):
        if testDictionary[i].WhoCanTrigger == id:
            resp, is_reaction = FindResponseHelper(message, testDictionary, i)
            if resp:
                response += resp + " "
                isReaction = is_reaction
    return response, isReaction

def FindResponseHelper(message: str, listToCheck: List['ResponseObject'], i: int) -> Tuple[str, bool]:
    triggers = listToCheck[i].ListOfTriggers
    for j in range(len(triggers)):
        if str(triggers[j]).lower() in message:
            prob = listToCheck[i].ProbabilityForResponse or 1
            if random.randint(1, prob) == prob:
                responses = listToCheck[i].ListOfResponses
                if not responses:
                    return "", listToCheck[i].IsReaction
                return random.choice(responses), listToCheck[i].IsReaction
            return "", False
    return "", False