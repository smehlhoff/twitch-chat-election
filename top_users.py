from collections import Counter

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("./misc/chanlog.csv")

c = Counter(df["username"]).most_common(10)

usernames = [item[0] for item in c]
freq = [item[1] for item in c]

plt.barh(usernames, freq)
plt.xlabel("Number of lines")
plt.ylabel("Username")
plt.title("Top 10 most active users")
plt.tight_layout()
plt.show()
