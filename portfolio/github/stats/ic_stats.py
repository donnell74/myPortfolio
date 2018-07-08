class ICStats(object):

    def __init__(self, commits, githubUsername):
        self.commits = commits
        self.githubUsername = githubUsername
        self.statistics = {
            'userStats': {
                'additions': 0,
                'deletions': 0,
            },
            'docStats': {
                'additions': 0,
                'deletions': 0,
            },
            'testStats': {
                'additions': 0,
                'deletions': 0,
            },
            'repoStats': {
                'additions': 0,
                'deletions': 0,
            }
        }

    def process(self):
        print(self.commits)
        for eachCommit in self.commits:
            self.statistics['repoStats'][
                'additions'] += eachCommit.get('additions')
            self.statistics['repoStats'][
                'deletions'] += eachCommit.get('deletions')
            if eachCommit.get('committer').get('user') != None and eachCommit.get('committer').get('user').get('login') == self.githubUsername:
                self.statistics['userStats'][
                    'additions'] += eachCommit.get('additions')
                self.statistics['userStats'][
                    'deletions'] += eachCommit.get('deletions')

        return self.statistics
