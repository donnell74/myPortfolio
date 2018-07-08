class IssueStats(object):

    def __init__(self, issues, githubUsername):
        self.issues = issues
        self.githubUsername = githubUsername
        self.statistics = {
            'issuesTotal': 0,
            'issuesClosedForRepo': 0,
            'issuesOpenForRepo': 0,
            'issuesCreatedByUser': 0,
            'issuesClosedByUser': 0,
            'issuesAssignedToUser': 0,
        }

    def process(self):
        for eachIssue in self.issues:
            assignees = [eachAssignee["login"]
                         for eachAssignee in eachIssue.get("assignees").get("nodes")]

            self.statistics['issuesTotal'] += 1

            if eachIssue.get("closed"):
                self.statistics['issuesClosedForRepo'] += 1
                if self.githubUsername in assignees:
                    self.statistics['issuesClosedByUser'] += 1
            else:
                if self.githubUsername in assignees:
                    self.statistics['issuesAssignedToUser'] += 1
                self.statistics['issuesOpenForRepo'] += 1

            if eachIssue.get("author").get("login") == self.githubUsername:
                self.statistics['issuesCreatedByUser'] += 1

        return self.statistics
