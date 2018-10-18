from random import shuffle
from contextlib import redirect_stdout

with open("collation.txt", encoding="utf-8") as f:
    randomized = [line.strip() for line in f.readlines()]
    shuffle(randomized)

with open("collation.in", "w", encoding="utf-8") as f:
    with redirect_stdout(f):
        print("\n".join(randomized))