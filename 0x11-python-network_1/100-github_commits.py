#!/usr/bin/python3
"""
Module 100-github_commits
Lists 10 commits (from the most recent to oldest) of the repository "rails"
by the user "rails".
Prints commits as <sha>: <author name>
"""
import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url, params={'per_page': 10})
    commits = response.json()
    for commit in commits:
        sha = commit.get('sha')
        author_name = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author_name}")
