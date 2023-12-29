from LinkLogic import *
import unittest

class TestDisBot(unittest.TestCase):
    maxDiff = None
    stringToRegex = """This is a response lmao
https://twitter.com/mikuneki/status/1739660608872857912?t=wz9hZPvqKiGVK7rtvVysZQ&s=19 I have never seen a more better
response than https://x.com/arisu_archive/status/1732371087378542734?t=6g1y7yZGwvLlVzf_a_5p8w&s=19
https://www.instagram.com/p/C1LCFRgoGC6/?igsh=ZjQ5ZGdxYnNucnVt
this baby
https://www.tiktok.com/t/ZT8mmX1o5/
https://vm.tiktok.com/ZIJnBaSLe/
https://www.reddit.com/r/HonkaiStarRail_leaks/s/282NbZbI5N
YEAHHHH
||https://twitter.com/HMBohemond/status/1738941464573272224?t=zlg6f7R_znllW-SsSw_2nA&s=19||
||https://x.com/QuirklessStoner/status/1738609204036784248?t=QDmKw4y99LWxkRwEf0TYYw&s=19 this is a message but at the end||
||this is a message but at the beginning https://www.instagram.com/reel/C07ajlnMzOD/?igshid=MzRlODBiNWFlZA==||
||https://www.tiktok.com/t/ZT8aMJt6N/||
||GOD I HATE THIS SO MUCH||
||https://vm.tiktok.com/ZIJnBp5q1/ or a random ass awful situation like https://x.com/123||
||https://www.reddit.com/r/HonkaiStarRail_leaks/s/hvFDwNGAV0|| ahhh shit, here we go again
but like 


literally
"""
            
        
    regexLinks = regexTwitterLinks(stringToRegex)
    #freeMessages, unformattedLinks = regexFreeMessages(stringToRegex)
    freeMessages, unformattedLinks = regexLinesIntoList(stringToRegex)
    firstMessage = getFirstMessage(freeMessages)
    spoiledMessages = getSpoiledMessages(stringToRegex)
    spoiledSpoiledLinks = spoilSpoiledLinks(unformattedLinks, spoiledMessages)
    formattedLinkReturn = returnFormattedLinks(unformattedLinks)
    formattedFreeMessages = formatFreeMessages(freeMessages)
    
    #order:
    #regexTwitterLinks
    #regexFreeMessages
    #getFirstMessage
    #getSpoiledMessage
    #spoilSpoiledLinks
    #returnFormattedLinks
    #formatFreeMessages
    def test_Regex(self):
        
        correctAnswer = [
                         "twitter.com/mikuneki/status/1739660608872857912?t=wz9hZPvqKiGVK7rtvVysZQ&s=19",
                         "x.com/arisu_archive/status/1732371087378542734?t=6g1y7yZGwvLlVzf_a_5p8w&s=19",
                         "instagram.com/p/C1LCFRgoGC6/?igsh=ZjQ5ZGdxYnNucnVt",
                         "tiktok.com/t/ZT8mmX1o5/",
                         "vm.tiktok.com/ZIJnBaSLe/",
                         "reddit.com/r/HonkaiStarRail_leaks/s/282NbZbI5N",
                         "twitter.com/HMBohemond/status/1738941464573272224?t=zlg6f7R_znllW-SsSw_2nA&s=19", #these last 5 get marked as spoiler later
                         "x.com/QuirklessStoner/status/1738609204036784248?t=QDmKw4y99LWxkRwEf0TYYw&s=19", 
                         "instagram.com/reel/C07ajlnMzOD/?igshid=MzRlODBiNWFlZA==",
                         "tiktok.com/t/ZT8aMJt6N/",
                         "vm.tiktok.com/ZIJnBp5q1/", 
                         "x.com/123",
                         "reddit.com/r/HonkaiStarRail_leaks/s/hvFDwNGAV0"
                         ]
        
        self.assertSequenceEqual(self.regexLinks, correctAnswer)
    
    def test_regexFreeMessages(self):
        correctAnswer = [
            'I have never seen a more better',
            'response than',
            'this baby',
            'YEAHHHH',
            '||this is a message but at the end||', 
            '||this is a message but at the beginning||', 
            '||GOD I HATE THIS SO MUCH||', 
            '||or a random ass awful situation like||',
            'ahhh shit here we go again',
            'but like',
            'literally'
            ]
        self.assertSequenceEqual(self.freeMessages, correctAnswer)
    
    def test_FirstMessage(self):
        correctAnswer = 'This is a response lmao\n'
        self.assertEqual(self.firstMessage, correctAnswer)
    
    def test_getSpoiledMessages(self):
        correctAnswer = """||https://twitter.com/HMBohemond/status/1738941464573272224?t=zlg6f7R_znllW-SsSw_2nA&s=19||||https://x.com/QuirklessStoner/status/1738609204036784248?t=QDmKw4y99LWxkRwEf0TYYw&s=19 this is a message but at the end||||this is a message but at the beginning https://www.instagram.com/reel/C07ajlnMzOD/?igshid=MzRlODBiNWFlZA==||||https://www.tiktok.com/t/ZT8aMJt6N/||||GOD I HATE THIS SO MUCH||||https://vm.tiktok.com/ZIJnBp5q1/ or a random ass awful situation like https://x.com/123||||https://www.reddit.com/r/HonkaiStarRail_leaks/s/hvFDwNGAV0||"""
        self.assertSequenceEqual(self.spoiledMessages, correctAnswer)
        
    def test_spoilSpoiledLinks(self):
        correctAnswer = [
            'twitter.com/mikuneki/status/1739660608872857912?t=wz9hZPvqKiGVK7rtvVysZQ&s=19',
            'x.com/arisu_archive/status/1732371087378542734?t=6g1y7yZGwvLlVzf_a_5p8w&s=19', 
            'instagram.com/p/C1LCFRgoGC6/?igsh=ZjQ5ZGdxYnNucnVt', 
            'tiktok.com/t/ZT8mmX1o5/', 
            'vm.tiktok.com/ZIJnBaSLe/', 
            'reddit.com/r/HonkaiStarRail_leaks/s/282NbZbI5N',
            'twitter.com/HMBohemond/status/1738941464573272224?t=zlg6f7R_znllW-SsSw_2nA&s=19||', 
            'x.com/QuirklessStoner/status/1738609204036784248?t=QDmKw4y99LWxkRwEf0TYYw&s=19||',
            'instagram.com/reel/C07ajlnMzOD/?igshid=MzRlODBiNWFlZA==||', 
            'tiktok.com/t/ZT8aMJt6N/||', 
            'vm.tiktok.com/ZIJnBp5q1/||',
            'x.com/123||', 
            'reddit.com/r/HonkaiStarRail_leaks/s/hvFDwNGAV0||'
        ]
        self.assertSequenceEqual(self.spoiledSpoiledLinks, correctAnswer)
        
    def test_returnUnformattedLinks(self):
        correctAnswer = """https://fxtwitter.com/mikuneki/status/1739660608872857912?t=wz9hZPvqKiGVK7rtvVysZQ&s=19
https://fixupx.com/arisu_archive/status/1732371087378542734?t=6g1y7yZGwvLlVzf_a_5p8w&s=19
https://ddinstagram.com/p/C1LCFRgoGC6/?igsh=ZjQ5ZGdxYnNucnVt
https://vxtiktok.com/t/ZT8mmX1o5/
https://vxtiktok.com/t/ZIJnBaSLe/
https://rxddit.com/r/HonkaiStarRail_leaks/s/282NbZbI5N
||https://fxtwitter.com/HMBohemond/status/1738941464573272224?t=zlg6f7R_znllW-SsSw_2nA&s=19||
||https://fixupx.com/QuirklessStoner/status/1738609204036784248?t=QDmKw4y99LWxkRwEf0TYYw&s=19||
||https://ddinstagram.com/reel/C07ajlnMzOD/?igshid=MzRlODBiNWFlZA==||
||https://vxtiktok.com/t/ZT8aMJt6N/||
||https://vxtiktok.com/t/ZIJnBp5q1/||
||https://fixupx.com/123||
||https://rxddit.com/r/HonkaiStarRail_leaks/s/hvFDwNGAV0||
"""
        self.assertSequenceEqual(self.formattedLinkReturn, correctAnswer)
        
        
    def test_formatFreeMessage(self):
        correctAnswer = """I have never seen a more better
response than
this baby
YEAHHHH
||this is a message but at the end||
||this is a message but at the beginning||
||GOD I HATE THIS SO MUCH||
||or a random ass awful situation like||
ahhh shit here we go again
but like
literally
"""
        self.assertSequenceEqual(self.formattedFreeMessages, correctAnswer)
        
if __name__ == '__main__':
    unittest.main()