LAST_25_PROJECTS_QUERY = """
query { 
  viewer {
    repositories (first: 25 orderBy: {field: CREATED_AT, direction: DESC} ) {
      nodes {
        id
        name
        owner {
          login
        }
        description
        url
        createdAt
        pushedAt
      }
    }
  }
}
"""

VIEWERS_NAME = """
query {
    viewer {
        login
    }
}
"""

LAST_100_ISSUES_QUERY = """
query { 
  repository(owner:"%s", name:"%s") {
    id
    issues (last: 100 orderBy: {field: CREATED_AT, direction: DESC}) {
      nodes {
        id
        title
        author {
          login
        }
        assignees (first: 25) {
          nodes {
            login
          }
        }
        closed
      }
    }
  }
}
"""

LAST_100_COMMITS_QUERY = """
query { 
  repository(owner:"%s", name:"%s") {
    defaultBranchRef {
      target {
        ... on Commit {
          history(first: 100) {
            pageInfo {
              hasNextPage
              endCursor
            }
            edges {
              node {
                oid
                messageHeadline
                additions
                deletions
                committer {
                  user {
                    login
                  }
                }
                pushedDate
                
              }
            }
          }
        }
      }
    }
  }
}
"""
