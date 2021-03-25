from django.shortcuts import render
from .forms import CalculateFrequentsForm, KeywordsForm, IndexRank
from .backend import getWordsAndFrequencies, getWords, similarity, cosine

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
        print(frequents)
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
        'url1': "",
        'url2': "",
        'score': 0
    }

    if form.is_valid():
        url1 = form.cleaned_data.get("url1")
        url2 = form.cleaned_data.get("url2")
        data1 = getWordsAndFrequencies.getWordsAndFrequences(url1)
        data2 = getWordsAndFrequencies.getWordsAndFrequences(url2)

        words1 = getWords.getWords(url1).getWords()
        words2 = getWords.getWords(url2).getWords()
        # for x in data1:
        #     words1.append(x[0])

        # for x in data2:
        #     words2.append(x[0])

        # sim = similarity.calculateSimilarity(data1, data2)
        sim = cosine.get_result(words1, words2)
        data = zip(data1[:10], data2[:10])
        context = {
            'form': form,
            'data': data,
            'url1': url1,
            'url2': url2,
            'score': sim
        }
        return render(request, 'webindexing/keywords.html', context)

    return render(request, 'webindexing/keywords.html', context)


# def getSimilarity(request):
#     form = KeywordsForm(request.POST or None)
#     context = {
#         'form': form,
#         'data': [],
#     }

#     if form.is_valid():
#         url1 = form.cleaned_data.get("url1")
#         url2 = form.cleaned_data.get("url2")
#         print(url1)
#         print(url2)

#     return render(request, 'webindexing/similarity.html', context)


def getIndexAndRank(request):
    global context

    form = IndexRank(request.POST or None)
    context = {
        'form': form,
        'data': [],
        'url1': "",
        'urls': "",
    }
    if form.is_valid():

        result = {}

        url1 = form.cleaned_data.get("url1")
        urls = form.cleaned_data.get("urls")
        url_list = urls.split(",")

        gw = getWords.getWords(url1)
        words1 = gw.getWords()

        for url in url_list:
            gw = getWords.getWords(url)
            words = gw.getWords()
            alturls = gw.getUrlsInPage()
            sim = cosine.get_result(words1, words)
            result[url] = sim
            for alt_url in alturls:
                gw = getWords.getWords(alt_url)
                alt_words = gw.getWords()
                alt_sim = cosine.get_result(words1, alt_words)
                result[alt_url] = alt_sim

        result = sorted(result.items(),  key=lambda x: x[1], reverse=True)
        print(result)

        context = {
            'form': form,
            'url1': url1,
            'urls': urls,
            'data': result
        }
        return render(request, 'webindexing/indexandrank.html', context)

    return render(request, 'webindexing/indexandrank.html', context)


def getSemanticAnalysis(request):
    return render(request, 'webindexing/semanticanalysis.html')
