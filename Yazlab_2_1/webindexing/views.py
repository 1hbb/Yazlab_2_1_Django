from django.shortcuts import render
from django.http import HttpResponse
from .forms import CalculateFrequentsForm, KeywordsForm
from .backend import getWords, calculateWordFrequents

# Create your views here.
posts = [
    "adsad",
    "adasdsad",
    "adasdadad",
    "asdafffh",
    "asgfgrg"
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'webindexing/home.html', context)


def getFrequents(request):
    global context

    form = CalculateFrequentsForm(request.POST or None)

    context = {
        'form': form,
        'data': []
    }

    if form.is_valid():
        website_url = form.cleaned_data.get("url")
        gw = getWords.getWords(website_url)
        wordList = gw.getWords()
        cwf = calculateWordFrequents.calculateWordFrequents(wordList)
        frequents = cwf.getWordFrequents()
        context = {
            'form': form,
            'data': frequents
        }
        return render(request, 'webindexing/frequent.html', context)

    return render(request, 'webindexing/frequent.html', context)


def getKeywords(request):
    form = KeywordsForm(request.POST or None)
    context = {
        'form': form,
        'data': []
    }

    if form.is_valid():
        url1 = form.cleaned_data.get("url1")
        url2 = form.cleaned_data.get("url2")
        print(url1)
        print(url2)

    return render(request, 'webindexing/keywords.html', context)


def getSimilarity(request):
    form = KeywordsForm(request.POST or None)
    context = {
        'form': form,
        'data': []
    }

    if form.is_valid():
        url1 = form.cleaned_data.get("url1")
        url2 = form.cleaned_data.get("url2")
        print(url1)
        print(url2)

    return render(request, 'webindexing/similarity.html', context)


def getIndexAndRank(request):
    return render(request, 'webindexing/indexandrank.html')


def getSemanticAnalysis(request):
    return render(request, 'webindexing/semanticanalysis.html')
