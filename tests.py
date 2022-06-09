from Global import *


def test_user():
    user = User()
    user.add_words(['1', '2', '3'])
    user.add_words(['2', '3', '4'])
    assert set(user.wordlist) == set(['1', '2', '3', '4'])
    print("Passed user tests.")


test_user()
