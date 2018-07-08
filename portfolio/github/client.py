from .queries import *
from portfolio.models import GithubToken
from django.db import IntegrityError
import requests
import json


CLIENT_ID = "1bdd6d92103f8958fb5b"
CLIENT_SECRET = "314d8ecd1736abfe01aca20ceafa8a3b8ce5bdfd"
ACCESS_TOKEN_URL = "https://github.com/login/oauth/access_token"
GITHUB_GRAPHQL_ENDPOINT = "https://api.github.com/graphql"


class GithubV4Client(object):
    """A simple client for github's v4 api."""

    def __init__(self, user):
        self.user = user
        self.githubToken = None
        if self.atLeastOneTokenFound():
            # TODO(donnell74): handle multiple tokens
            self.githubToken = GithubToken.objects.filter(user_id=user.id)[0]

    def atLeastOneTokenFound(self):
        return GithubToken.objects.filter(user_id=self.user.id).count() > 0

    def getAndSaveOAuthToken(self, clientCode):
        """Gets an OAuth token based on the code returned by authorize."""
        accessTokenRequest = requests.post(
            ACCESS_TOKEN_URL,
            data={
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
                'code': clientCode
            },
            headers={
                'accept': 'application/json'
            }
        )

        accessTokenRequest.raise_for_status()
        accessToken = accessTokenRequest.json().get('access_token')
        self.githubToken = GithubToken(
            user_id=self.user.id,
            token=accessToken,
        )

        self.githubToken.github_username = self.getGithubLogin()
        maybePreviousGithubToken = GithubToken.objects.filter(
            user_id=self.user.id,
            github_username=self.githubToken.github_username,
        )

        if maybePreviousGithubToken.count() == 1:
            self.githubToken = maybePreviousGithubToken[0]
            self.githubToken.token = accessToken
        elif maybePreviousGithubToken.count() > 1:
            raise IntegrityError(
                "There is more than one github token for the user id %d and username %s",
                self.user.id,
                github_username,
            )

        self.githubToken.save()

    def getGithubLogin(self):
        githubLoginRequest = self.query(VIEWERS_NAME)
        githubLoginRequest.raise_for_status()
        print("Get github login response: %s" %
              githubLoginRequest.json())
        return githubLoginRequest.json().get("data").get("viewer").get("login")

    def getLast25Projects(self):
        """Gets the last 25 projects for the current user."""
        getProjectsRequest = self.query(LAST_25_PROJECTS_QUERY)

        getProjectsRequest.raise_for_status()
        print("Get last 25 projects response: %s" %
              getProjectsRequest.json())
        return getProjectsRequest.json().get("data").get("viewer").get("repositories").get("nodes")

    def getAllIssues(self, repoName, ownerName):
        # TODO(donnell74): Store this in the database and do incremental gets
        getLast100IssuesRequest = self.query(
            LAST_100_ISSUES_QUERY % (ownerName, repoName))

        getLast100IssuesRequest.raise_for_status()
        print("Get last 100 issues response: %s" %
              getLast100IssuesRequest.json())
        return getLast100IssuesRequest.json().get("data").get("repository").get("issues").get("nodes")

    def getAllCommits(self, repoName, ownerName):
        # TODO(donnell74): Store this in the database and do incremental gets
        getLast100CommitsRequest = self.query(
            LAST_100_COMMITS_QUERY % (ownerName, repoName))

        getLast100CommitsRequest.raise_for_status()
        print("Get last 100 commits response: %s" %
              getLast100CommitsRequest.json())
        return [eachEdge.get("node") for eachEdge in getLast100CommitsRequest.json().get("data").get("repository").get("ref").get("target").get("history").get("edges")]

    def query(self, queryString):
        """Queries Github with queryString and correct auth."""
        # TODO(gdonnell): If this throws an unauthorized error delete the token
        # from the database.
        print('Running query: %s' % (queryString))
        return requests.post(
            GITHUB_GRAPHQL_ENDPOINT,
            json={
                'query': queryString
            },
            headers={
                'Authorization': "bearer %s" % (self.githubToken.token)
            }
        )
