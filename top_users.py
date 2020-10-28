import pandas as pd
import matplotlib.pyplot as plt

from collections import Counter

df = pd.read_csv("./misc/chanlog.csv")

c = Counter(df["username"]).most_common(10)

usernames = [item[0] for item in c]
freq = [item[1] for item in c]

plt.barh(usernames, freq)
plt.title("Top 10 spoken users")
plt.xlabel("Number of lines spoken")
plt.ylabel("Username")

plt.tight_layout()

plt.show()
