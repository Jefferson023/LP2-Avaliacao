from contextlib import redirect_stdout
from re import compile, sub

regular = compile(r"RT (@\S+):.*(http\S+)")
with open("tweets.in", encoding="utf-8") as f:
    tweets = [user+ '\t' + sub('…', '', link) for user, link in regular.findall(f.read())]
    tweets.sort()

with open("tweets.out", "w", encoding="utf-8") as f:
    with redirect_stdout(f):
        print("\n".join(tweets))