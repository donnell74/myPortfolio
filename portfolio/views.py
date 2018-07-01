from django.shortcuts import render, redirect
from .github.client import GithubV4Client, CLIENT_ID
from .models import GithubToken
import requests
import json


# Create your views here.
def profile(request):
    context = {'githubTokens': GithubToken.objects.filter(user_id = request.user.id)}
    return render(request, 'portfolio/profile.html', context)

def getGithubTokenCode(request):
    return redirect("https://github.com/login/oauth/authorize?client_id=%s" % (CLIENT_ID))
    
def saveGithubToken(request):
    githubClient = GithubV4Client(request.user)
    githubClient.getAndSaveOAuthToken(request.GET['code'])
    return redirect('/accounts/profile/')

def index(request):
    githubClient = GithubV4Client(request.user)
    context = {'projects': []}
    if githubClient.atLeastOneTokenFound():
        for eachProject in githubClient.getLast25Projects():
            context['projects'].append(
                {
                    'name': eachProject.get("name"),
                    'githubLink': 'https://github.com/donnell74/myPortfolio',
                    'timelineData': '##data about timeline here##',
                    'icStatsData': {
                        'summary': '##data about ic stats here##',
                        'codeStats': '##Stats about code changes##',
                        'docStats': '##Stats about doc changes##',
                        'testStats': '##Stats about test changes##',
                    },   
                    'reviewerStatsData': {
                        'summary': '##data about reviewer stats here##',
                        'codeStats': '##Stats about code changes##',
                        'docStats': '##Stats about doc changes##',
                        'testStats': '##Stats about test changes##',
                    },
                    'bugStatsData': {
                        'summary': '##data about bug stats here##',
                        'bugsClosed': '120',
                        'bugsOpen': '32',
                    }
                },                
            )

    return render(request, 'portfolio/homepage.html', context)

