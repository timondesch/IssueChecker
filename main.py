import pycurl
import certifi
from io import BytesIO
import json


class Repo:
    def __init__(self, url):
        self.base_url = url
        self.transformed_url = self.url_transformer()
        self.label_url = self.url_transformer(True)
        self.issues = json.loads(self.get_from_url(self.transformed_url).getvalue().decode('iso-8859-1'))
        self.labels = json.loads(self.get_from_url(self.label_url).getvalue().decode('iso-8859-1'))

    @staticmethod
    def get_from_url(url):
        buffer = BytesIO()
        curl = pycurl.Curl()
        curl.setopt(curl.URL, url)
        curl.setopt(curl.WRITEDATA, buffer)
        curl.setopt(curl.CAINFO, certifi.where())

        curl.perform()
        curl.close()
        return buffer

    def url_transformer(self, for_labels=False):
        url = self.base_url
        split_url = url.split('/')
        user, repo = split_url[-3], split_url[-2]
        url = f"https://api.github.com/repos/{user}/{repo}/"
        return url + "labels" if for_labels else url + "issues"

    def print_issues(self):
        for issue in self.issues:
            if issue['labels']:
                print(issue['labels'])

    def print_labels(self):
        for label in self.labels:
            print(label['name'])


# url = "https://api.github.com/repos/asciinema/asciinema/issues"
test_url = "https://github.com/pallets/flask/issues"
curl_object = pycurl.Curl()

repo = Repo(test_url)
repo.print_issues()
repo.print_labels()
