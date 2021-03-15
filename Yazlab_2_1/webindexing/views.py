from django.shortcuts import render
from .forms import CalculateFrequentsForm, KeywordsForm
from .backend import getWordsAndFrequencies, getKeywords as keywords
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'webindexing/home.html')


def getFrequents(request):
    global context

    form = CalculateFrequentsForm(request.POST or None)

    context = {
        'form': form,
        'data': []
    }

    if form.is_valid():
        website_url = form.cleaned_data.get("url")
        frequents = getWordsAndFrequencies.getWordsAndFrequences(website_url)
        context = {
            'form': form,
            'data': frequents
        }
        return render(request, 'webindexing/frequent.html', context)

    return render(request, 'webindexing/frequent.html', context)


def getKeywords(request):
    global context

    form = KeywordsForm(request.POST or None)
    context = {
        'form': form,
        'data1': [],
        'data2': [],
        'url1' : "",
        'url2': "",
    }

    if form.is_valid():
        url1 = form.cleaned_data.get("url1")
        url2 = form.cleaned_data.get("url2")
        data1 = getWordsAndFrequencies.getWordsAndFrequences(url1)
        data2 = getWordsAndFrequencies.getWordsAndFrequences(url2)
        data = zip(data1[:10], data2[:10])
        context = {
            'form': form,
            'data': data,
            'url1': url1,
            'url2': url2,
        }
        return render(request, 'webindexing/keywords.html', context)

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
