import requests
from bs4 import BeautifulSoup
import re
from bs4.element import Comment

stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up',
              'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

# avoid this tags because we want only text in html page like <p> tag <h> tag
blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head',
    # there may be more elements you don't want
]


class getWords:
    def __init__(self, url) -> None:
        self.url = url
        # get webpage
        res = requests.get(self.url)
        html_page = res.content

        # parse html with bs4
        self.soup = BeautifulSoup(
            html_page, 'html.parser')

    def getWords(self):

        def tag_visible(element):
            if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
                return False
            if isinstance(element, Comment):
                return False
            return True

        text = self.soup.find_all(text=True)
        visible_texts = filter(tag_visible, text)
        words = []
        for t in visible_texts:
            if t.parent.name not in blacklist:
                # use regex for getting every word "[a-zA-Z]+" means regex only excepts capital words and avoiding numbers
                # res = re.findall(r'[a-zA-Z0-9]+', t)
                res = re.findall(r'\w+', t)
                if res:
                    for word in res:
                        if word not in stop_words:
                            words.append(word.lower())
        return words

    def getUrlsInPage(self):
        urls = []
        for link in self.soup.find_all('a'):
            lnk = link.get('href')
            urls.append(lnk)
        print(urls)
