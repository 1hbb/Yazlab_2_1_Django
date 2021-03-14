from getWords import getWords
from calculateWordFrequents import calculateWordFrequents

url = "https://www.hackingwithswift.com/"

gw = getWords(url)
wordList = gw.getWords()

gw.getUrlsInPage()
cwf = calculateWordFrequents(wordList)

frequents = cwf.getWordFrequents()

print(frequents)
