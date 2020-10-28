import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./misc/chanlog.csv")

subs = df.loc[df['sub_count'] > 0]
subs = subs.groupby(["sub_count"])["username"].nunique()

x = [i for i in range(1, len(subs) + 1)]
y = [val for val in subs]

fig, ax = plt.subplots()

ax.bar(x, y)
ax.set_ylabel("User count")
ax.set_xlabel("Months subscribed")
ax.set_title("Subscriber breakdown by months subscribed consecutively")

plt.show()
