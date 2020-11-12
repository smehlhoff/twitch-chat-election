from collections import Counter

import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import STOPWORDS

df = pd.read_csv("./misc/chanlog.csv")

char_count = df["char_count"] = df["user_msg"].str.len()
char_count = char_count.mean()

print(f"Average character count: {char_count:.2f}")

word_count = df["word_count"] = df["user_msg"].apply(lambda x: len(str(x).split(" ")))
word_count = word_count.mean()

print(f"Average word count: {word_count:.2f}")

total_words = 0

for msg in df["user_msg"]:
    msg = str(msg)
    msg = msg.lower().split()

    for word in msg:
        total_words += 1

print(f"Total words used: {total_words:,}")

stop_words = 0

for msg in df["user_msg"]:
    msg = str(msg)
    msg = msg.lower().split()

    for word in msg:
        if word in STOPWORDS:
            stop_words += 1

print(f"Total stop words used: {stop_words:,}")


unique_words = set()

for msg in df["user_msg"]:
    msg = str(msg)
    msg = msg.lower().split()

    for word in msg:
        unique_words.add(word)

print(f"Total unique words used: {len(unique_words):,}")

total_users = df["username"].nunique()

print(f"Total unique users who spoke: {total_users:,}")
