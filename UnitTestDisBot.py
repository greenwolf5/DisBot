from LinkLogic import *
import unittest

class TestDisBot(unittest.TestCase):
    maxDiff = None
    stringToRegex = """
This is a response lmao
https://twitter.com/mikuneki/status/1739660608872857912?t=wz9hZPvqKiGVK7rtvVysZQ&s=19 I have never seen a more better
response than https://x.com/arisu_archive/status/1732371087378542734?t=6g1y7yZGwvLlVzf_a_5p8w&s=19
https://www.instagram.com/p/C1LCFRgoGC6/?igsh=ZjQ5ZGdxYnNucnVt
this baby
https://www.tiktok.com/t/ZT8mmX1o5/
https://vm.tiktok.com/ZIJnBaSLe/
https://www.reddit.com/r/HonkaiStarRail_leaks/s/282NbZbI5N
YEAHHHH
||https://twitter.com/HMBohemond/status/1738941464573272224?t=zlg6f7R_znllW-SsSw_2nA&s=19||
||https://x.com/QuirklessStoner/status/1738609204036784248?t=QDmKw4y99LWxkRwEf0TYYw&s=19||
||https://www.instagram.com/reel/C07ajlnMzOD/?igshid=MzRlODBiNWFlZA==||
||https://www.tiktok.com/t/ZT8aMJt6N/||
||GOD I HATE THIS SO MUCH||
||https://vm.tiktok.com/ZIJnBp5q1/||
||https://www.reddit.com/r/HonkaiStarRail_leaks/s/hvFDwNGAV0||
"""
    regexLinks = regexTwitterLinks(stringToRegex)
    freeMessages, unformattedLinks = regexFreeMessages(stringToRegex)
    #order:
    #regexTwitterLinks
    #regexFreeMessages
    #getFirstMessage
    #getSpoiledMessage
    #spoilSpoiledLinks
    #returnFormattedLinks
    #getFormattedLinks
    #formatFreeMessages
    def test_Regex(self):
        
        correctAnswer = [
                         "twitter.com/mikuneki/status/1739660608872857912?t=wz9hZPvqKiGVK7rtvVysZQ&s=19",
                         "x.com/arisu_archive/status/1732371087378542734?t=6g1y7yZGwvLlVzf_a_5p8w&s=19",
                         "instagram.com/p/C1LCFRgoGC6/?igsh=ZjQ5ZGdxYnNucnVt",
                         "tiktok.com/t/ZT8mmX1o5/",
                         "vm.tiktok.com/ZIJnBaSLe/",
                         "reddit.com/r/HonkaiStarRail_leaks/s/282NbZbI5N",
                         "twitter.com/HMBohemond/status/1738941464573272224?t=zlg6f7R_znllW-SsSw_2nA&s=19||",
                         "x.com/QuirklessStoner/status/1738609204036784248?t=QDmKw4y99LWxkRwEf0TYYw&s=19||",
                         "instagram.com/reel/C07ajlnMzOD/?igshid=MzRlODBiNWFlZA==||",
                         "tiktok.com/t/ZT8aMJt6N/||",
                         "vm.tiktok.com/ZIJnBp5q1/||",
                         "reddit.com/r/HonkaiStarRail_leaks/s/hvFDwNGAV0||"
                         ]
        
        self.assertSequenceEqual(self.regexLinks, correctAnswer)
    
    def test_regexFreeMessages(self):
        correctAnswer = ['\nThis is a response lmao\n', ' I have never seen a more better\n\nresponse than ', '', '\n\n', '', '\n\nthis baby\n', '', '\n\n', '', '\n\n', '', '\n\nYEAHHHH\n||', '', '\n\n||', ...]
        self.assertSequenceEqual(self.freeMessages, correctAnswer)
    
    def test_FirstMessage(self):
        self.assertEqual(1,1)
        
if __name__ == '__main__':
    unittest.main()