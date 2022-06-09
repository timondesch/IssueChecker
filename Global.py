from Repo import *
from User import *

class Global:
    def __init__(self):
        self.users = []
        self.repos = []

    def global_update(self):
        for repo in self.repos:
            repo.issues = repo.updated_issues()
            repo.labels = repo.updated_labels()

        for user in self.users:
            user.update_issues()

    def add_repo(self, repo_url):
        repo = Repo(repo_url)
        self.repos[repo.id] = repo
