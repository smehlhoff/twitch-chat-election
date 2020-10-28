import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./misc/chanlog.csv")

users = df.groupby(["sub_count"])["username"].nunique()

nonsubs = users[:1].sum()
subs = users[1:].sum()

fig, ax = plt.subplots()

ax.pie([nonsubs, subs], autopct="%1.1f%%",
       explode=(0.1, 0), wedgeprops={"edgecolor": "black"})
ax.axis("equal")
ax.set_title("Which group spoke more frequently?")

plt.legend(labels=["Non-subscribers", "Subscribers"], loc=4)
plt.tight_layout()
plt.show()
