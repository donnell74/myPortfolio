from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'projects': [
            {
                'name': 'Project 1',
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
            {
                'name': 'Project 2',
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
            {
                'name': 'Project 3',
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
        ]
    }
    return render(request, 'portfolio/index.html', context)
