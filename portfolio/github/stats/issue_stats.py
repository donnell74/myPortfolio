class IssueStats(object):

    def __init__(self, issues, githubUsername):
        self.issues = issues
        self.githubUsername = githubUsername
        self.issuesTotal = 0
        self.issuesOpenForRepo = 0
        self.issuesClosedForRepo = 0
        self.issuesCreatedByUser = 0
        self.issuesClosedByUser = 0
        self.issuesAssignedToUser = 0
        self.process()

    def process(self):
        for eachIssue in self.issues:
            assignees = [eachAssignee["login"]
                         for eachAssignee in eachIssue.get("assignees").get("nodes")]

            self.issuesTotal += 1

            if eachIssue.get("closed"):
                self.issuesClosedForRepo += 1
                if self.githubUsername in assignees:
                    self.issuesClosedByUser += 1
            else:
                if self.githubUsername in assignees:
                    self.issuesAssignedToUser += 1
                self.issuesOpenForRepo += 1

            if eachIssue.get("author").get("login") == self.githubUsername:
                self.issuesCreatedByUser += 1
