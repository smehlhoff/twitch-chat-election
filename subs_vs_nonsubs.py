import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("./misc/chanlog.csv")

nonsubs = df.loc[df["sub_count"] == 0]
subs = df.loc[df["sub_count"] > 0]

sizes = [len(nonsubs), len(subs)]

plt.style.use('fivethirtyeight')
plt.pie(sizes, autopct="%1.1f%%", explode=(0.1, 0), wedgeprops={"edgecolor": "black"})
plt.axis("equal")
plt.title("Which group spoke more frequently?")
plt.legend(labels=["Non-subscribers", "Subscribers"], loc=4)
plt.tight_layout()
plt.show()
