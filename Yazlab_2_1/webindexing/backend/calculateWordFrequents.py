
class calculateWordFrequents:

    def __init__(self, wordList) -> None:
        self.wordList = wordList

    def getWordFrequents(self):

        worldFreq = []

        wordlist = self.wordList

        # calculate frequent for every word and append list
        for w in wordlist:
            worldFreq.append(wordlist.count(w))

        # create word and frequent zip list like ("word", 10)
        worldAndFrequentList = sorted(
            list(zip(wordlist, worldFreq)), key=lambda x: x[1], reverse=True)

        result = []

        # remove same elements in list and return
        [result.append(x) for x in worldAndFrequentList if x not in result]

        return result
