from collections import Counter

import matplotlib.pyplot as plt
import pandas as pd
from nltk.corpus import stopwords

df = pd.read_csv("./misc/chanlog.csv")

total_words = 0

for msg in df["user_msg"]:
    msg = str(msg)
    msg = msg.lower().split()

    for word in msg:
        total_words += 1

print(f"Total words used: {total_words:,}")

unique_words = set()

for msg in df["user_msg"]:
    msg = str(msg)
    msg = msg.lower().split()

    for word in msg:
        unique_words.add(word)

print(f"Total unique words used: {len(unique_words):,}")

STOPWORDS = set(stopwords.words('english'))

stop_words = 0

for msg in df["user_msg"]:
    msg = str(msg)
    msg = msg.lower().split()

    for word in msg:
        if word in STOPWORDS:
            stop_words += 1

print(f"Total stop words used: {stop_words:,}")

word_count = df["word_count"] = df["user_msg"].apply(lambda x: len(str(x).split(" ")))
word_count = word_count.mean()

print(f"Average word count per message: {word_count:.2f}")

total_users = df["username"].nunique()

print(f"Total unique users who spoke: {total_users:,}")
