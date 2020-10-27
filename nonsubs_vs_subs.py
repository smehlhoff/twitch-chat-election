import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./misc/chanlog.csv")

data = df.loc[df['command'] == "PRIVMSG"]
users = data.groupby(["sub_count"])["username"].nunique()

nonsubs = users[:1].sum()
subs = users[1:].sum()

fig, ax = plt.subplots()

ax.pie([nonsubs, subs], autopct="%1.1f%%")
ax.axis("equal")
ax.set_title("Which group spoke more frequently?")

plt.legend(labels=["Non-subscribers", "Subscribers"], loc=4)
plt.show()
