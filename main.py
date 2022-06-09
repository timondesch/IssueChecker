from Global import *

# url = "https://api.github.com/repos/asciinema/asciinema/issues"
test_url = "https://github.com/pallets/flask/issues"

wordlist = ['review', 'cli']

repo = Repo(test_url)
# repo.print_issues()
# repo.print_labels()

repo.filter_issues(wordlist)
print(len(repo.filtered_issues))
