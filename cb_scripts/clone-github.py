#!/usr/bin/env python3

"""Clone GitHub Repos.

Inspired by https://github.com/realpython/python-scripts/blob/master/scripts/34_git_all_repos.py.
"""

import sys
from pathlib import Path
import requests  # pip install requests
from git import Repo  # pip install GitPython

URL = 'https://api.github.com/{0}/{1}/repos?per_page=100&page={2}'
PER_PAGE = 100


def git_repos(group: str = "users", user: str = None):
    """GitHub Repos generator."""
    page = 1
    while True:
        url = URL.format(group, user, page)
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            for repo in data:
                yield repo['clone_url']
            if len(data) >= PER_PAGE:
                page += 1
            else:
                print("All repos returned.")
                break
        else:
            print(r)
    return []


def clone(clone_url: str, repo_dir: str):
    """Clone repo."""
    repo_name = clone_url.rpartition('/')[-1]
    print(f"Cloning '{repo_name}' to '{repo_dir}/{repo_name}'...", end="")
    Repo.clone_from(clone_url, f"{repo_dir}/{repo_name}")
    print("DONE")


def main(group: str, user: str, repo_dir: str):
    """Clone GitHub Repos to local machine."""
    for i in git_repos(group=group, user=user):
        clone(clone_url=i, repo_dir=repo_dir)


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        main(group=sys.argv[1], user=sys.argv[2], repo_dir=sys.argv[3])
    else:
        print(
            f'python {__file__} ["USERS","ORG"] [Github Username or Org Name] [local dir Location]')
