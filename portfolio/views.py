from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'projects': [
            {
                'name': 'Project 1',
                'githubLink': 'https://github.com/donnell74/myPortfolio',
                'timelineData': '##data about timeline here##',
                'icStatsData': '##data about ic stats here##',        
                'reviewerStatsData': '##data about reviewer stats here##'
            },
            {
                'name': 'Project 2',
                'githubLink': 'https://github.com/donnell74/myPortfolio',
                'timelineData': '##data about timeline here##',
                'icStatsData': '##data about ic stats here##',        
                'reviewerStatsData': '##data about reviewer stats here##'
            },
            {
                'name': 'Project 3',
                'githubLink': 'https://github.com/donnell74/myPortfolio',
                'timelineData': '##data about timeline here##',
                'icStatsData': '##data about ic stats here##',        
                'reviewerStatsData': '##data about reviewer stats here##'
            },
        ]
    }
    return render(request, 'portfolio/index.html', context)
