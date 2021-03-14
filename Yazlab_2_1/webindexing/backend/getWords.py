import requests
from bs4 import BeautifulSoup
import re

# avoid this tags because we want only text in html page like <p> tag <h> tag
blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head',
    'input',
    'script',
    'div',
    'img',
    # there may be more elements you don't want
]


class getWords:
    def __init__(self, url) -> None:
        self.url = url
        # get webpage
        res = requests.get(self.url)
        html_page = res.content

        # parse html with bs4
        self.soup = BeautifulSoup(html_page, 'html.parser')

    def getWords(self):
        text = self.soup.find_all(text=True)
        words = []
        for t in text:
            if t.parent.name not in blacklist:
                # use regex for getting every word "[a-zA-Z]+" means regex only excepts capital words and avoiding numbers
                res = re.findall(r'[a-zA-Z]+', t)
                if res:
                    for word in res:
                        words.append(word.lower())
        return words

    def getUrlsInPage(self):
        urls = []
        for link in self.soup.find_all('a'):
            lnk = link.get('href')
            urls.append(lnk)
        print(urls)
