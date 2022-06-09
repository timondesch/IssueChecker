class User:
    def __init__(self):
        self.wordlist = []
        self.repos = {}
        self.issues = {}

    def add_words(self, word_list):
        self.wordlist = list(set(self.wordlist) | set(word_list))
        return self.wordlist

    def add_repos(self, repo_list):
        """Adds repos to user's repos list.
        """
        pass

    def update_issues(self):
        """Updates user's issues list
        """
        pass
