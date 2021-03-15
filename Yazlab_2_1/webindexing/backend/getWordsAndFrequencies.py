from .getWords import getWords
from .calculateWordFrequents import calculateWordFrequents


def getWordsAndFrequences(url):
    gw = getWords(url)
    wordList = gw.getWords()
    cwf = calculateWordFrequents(wordList)
    frequents = cwf.getWordFrequents()
    return frequents
