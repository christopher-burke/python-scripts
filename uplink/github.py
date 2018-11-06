#!/usr/bin/env python3

"""GitHub consumer using uplink package.

Demo of the uplink package (https://uplink.readthedocs.io).
`pip install -U uplink`
"""

from uplink import Consumer, Query, get


class GitHub(Consumer):

    @get("repositories")
    def get_repo(): pass

    @get("users/{username}")
    def get_user(self, username): pass

    @get("users/{username}/repos")
    def get_user_repos(self, username): pass


def print_info(user, all_user_repos):
    """Print the user login and repos."""
    print(f"# {user.json()['login']}\n")

    user_repos_json = all_user_repos.json()
    forked_user_repos = [repo['name']
                         for repo in user_repos_json
                         if repo['fork'] is True]
    user_repos = [repo['name']
                  for repo in user_repos_json
                  if repo['fork'] is False]

    print('## User Repos\n')
    for repo in user_repos:
        print(f'* {repo}')
    print('\n')
    print('## Forked Repos\n')
    for repo in forked_user_repos:
        print(f'* {repo}')


def main():
    """Working with uplink to get GitHub info."""
    github = GitHub(base_url="https://api.github.com/")
    user = github.get_user(username='christopher-burke')
    all_user_repos = github.get_user_repos(username='christopher-burke')
    print_info(user, all_user_repos)


if __name__ == "__main__":
    main()
