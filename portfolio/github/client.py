from .queries import *
import requests
import json



CLIENT_ID = "1bdd6d92103f8958fb5b"
CLIENT_SECRET = "314d8ecd1736abfe01aca20ceafa8a3b8ce5bdfd"
ACCESS_TOKEN_URL = "https://github.com/login/oauth/access_token"
GITHUB_GRAPHQL_ENDPOINT = "https://api.github.com/graphql"


class GithubV4Client(object):
    """A simple client for github's v4 api."""

    def __init__(self, code):
        self.accessToken = self.getOAuthToken(code)

    def getOAuthToken(self, clientCode):
        """Gets an OAuth token based on the code returned by authorize."""
        accessTokenRequest = requests.post(
                ACCESS_TOKEN_URL, 
                data = {
                    'client_id': CLIENT_ID,
                    'client_secret': CLIENT_SECRET,
                    'code': clientCode
                },
                headers = {
                    'accept': 'application/json'
                }
            )

        accessTokenRequest.raise_for_status()
        return accessTokenRequest.json().get('access_token')

    def getLast25Projects(self):
        """Gets the last 25 projects for the current user."""
        getProjectsRequests = self.query(LAST_25_PROJECTS_QUERY)

        getProjectsRequests.raise_for_status()
        return getProjectsRequests.json().get("data").get("viewer").get("repositories").get("nodes")

    def query(self, queryString):
        """Queries Github with queryString and correct auth."""
        return requests.post(
                GITHUB_GRAPHQL_ENDPOINT, 
                json = {
                    'query': queryString
                },
                headers = {
                    'Authorization': "bearer %s" % (self.accessToken)
                }
            )
