
from .getWordsAndFrequencies import getWordsAndFrequences


def getKeywords(url):
    wordAndFrequents = getWordsAndFrequences(url)
    keywords = []

    for index in range(len(wordAndFrequents)):
        if index < 10:
            keywords.append(wordAndFrequents[index][0])
    return keywords
