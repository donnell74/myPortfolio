LAST_25_PROJECTS_QUERY = """
query { 
  viewer {
    repositories (first: 25 orderBy: {field: CREATED_AT, direction: DESC} ) {
      nodes {
        id
        name
      }
    }
  }
}
"""
