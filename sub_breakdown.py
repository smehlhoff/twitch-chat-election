import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("./misc/chanlog.csv")

subs = df.loc[df["sub_count"] > 0]
subs = subs.groupby(["sub_count"])["username"].nunique()

x = [i for i in range(1, len(subs) + 1)]
y = [val for val in subs]

plt.bar(x, y)
plt.xlabel("Month")
plt.ylabel("Subscriber count")
plt.title("Breakdown of subscribers who spoke by months subscribed consecutively")
plt.tight_layout()
plt.show()
