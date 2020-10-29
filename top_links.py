import json
import re

import pandas as pd
import matplotlib.pyplot as plt

from collections import Counter

df = pd.read_csv("./misc/chanlog.csv")

overall = []
youtube = []
twitter = []
reddit = []

for msg in df["user_msg"]:
    data = re.search("(https?://(www.)?|www.)(?P<link>[^\s]+)", msg)
    if data:
        if re.search("(youtube)", data["link"]):
            youtube.append(data["link"])
        elif re.search("(twitter)", data["link"]):
            twitter.append(data["link"])
        elif re.search("(reddit)", data["link"]):
            reddit.append(data["link"])
        overall.append(data["link"])

overall = dict(Counter(overall).most_common(10))
youtube = dict(Counter(youtube).most_common(10))
twitter = dict(Counter(twitter).most_common(10))
reddit = dict(Counter(reddit).most_common(10))

with open("top_links.json", "w", encoding="utf-8") as f:
    json.dump({"top_links": [{"overall": overall}, {"youtube": youtube},
                             {"twitter": twitter}, {"reddit": reddit}]}, f, indent=4)
