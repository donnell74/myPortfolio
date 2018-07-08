from django.shortcuts import render, redirect
from .github.client import GithubV4Client, CLIENT_ID
from .github.stats.issue_stats import IssueStats
from .github.stats.ic_stats import ICStats
from .models import GithubToken
import requests
import json


# Create your views here.
def profile(request):
    context = {'githubTokens': GithubToken.objects.filter(
        user_id=request.user.id)}
    return render(request, 'portfolio/profile.html', context)


def getGithubTokenCode(request):
    return redirect("https://github.com/login/oauth/authorize?client_id=%s" % (CLIENT_ID))


def saveGithubToken(request):
    githubClient = GithubV4Client(request.user)
    githubClient.getAndSaveOAuthToken(request.GET['code'])
    return redirect('/accounts/profile/')


def index(request):
    githubClient = GithubV4Client(request.user)
    context = {
        'projects': [],
        'githubLogin': githubClient.githubToken.github_username,
    }
    if githubClient.atLeastOneTokenFound():
        for eachProject in githubClient.getLast25Projects():
            allIssues = githubClient.getAllIssues(eachProject.get(
                'name'), eachProject.get('owner').get('login'))
            issueStats = IssueStats(
                allIssues, githubClient.githubToken.github_username)
            allCommits = githubClient.getAllCommits(eachProject.get(
                'name'), eachProject.get('owner').get('login'))
            icStats = ICStats(
                allCommits, githubClient.githubToken.github_username)
            context['projects'].append(
                {
                    'repoGeneralData': {
                        'name': eachProject.get('name'),
                        'githubUrl': eachProject.get('url'),
                        'description': eachProject.get('description'),
                    },
                    'timelineData': {
                        'createdAt': eachProject.get('createdAt'),
                        'updatedAt': eachProject.get('pushedAt'),
                    },
                    'icStatsData': icStats.process(),
                    'reviewerStatsData': {
                        'summary': '##data about reviewer stats here##',
                        'codeStats': '##Stats about code changes##',
                        'docStats': '##Stats about doc changes##',
                        'testStats': '##Stats about test changes##',
                    },
                    'issuesStatsData': issueStats.process(),
                },
            )

    return render(request, 'portfolio/index.html', context)
