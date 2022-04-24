from django.urls import path
from . import views
from django.shortcuts import redirect

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('query/', views.query, name='query'),
    path('covid_experience/', views.covid_experience, name='covid_experience'),
    path('read_experience/', views.read_experience, name='read_experience'),
    path('symtoms_wordcloud/', views.symtoms_wordcloud, name='symtoms_wordcloud'),
]
