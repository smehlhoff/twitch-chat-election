import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./misc/chanlog.csv")

data = df.loc[(df['command'] == "PRIVMSG") & (df['sub_count'] > 0)]
subs = data.groupby(["sub_count"])["username"].nunique()

x = [i for i in range(1, len(subs) + 1)]
y = [val for val in subs]

fig, ax = plt.subplots()

ax.bar(x, y)
ax.set_ylabel("User count")
ax.set_xlabel("Months subscribed")
ax.set_title("Subscriber breakdown by month")

plt.show()
