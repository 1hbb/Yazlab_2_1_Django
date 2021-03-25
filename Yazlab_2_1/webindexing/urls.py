from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home-page"),
    path('frequent', views.getFrequents, name="frequent-page"),
    path('keywords', views.getKeywords, name="keywords-page"),
    # path('similarity', views.getSimilarity, name="similarity-page"),
    path('indexandrank', views.getIndexAndRank, name="indexandrank-page"),
    path('semanticanalysis', views.getSemanticAnalysis, name="semanticanalysis-page"),

]
