import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("./misc/chanlog.csv")

biden = []
trump = []

for msg in df["user_msg"]:
    msg = msg.lower().split()

    for word in msg:
        if "biden" in word:
            biden.append(word)
        elif "trump" in word and word != "ttrump":
            trump.append(word)

sizes = [len(biden), len(trump)]

plt.pie(sizes, autopct="%1.1f%%", explode=(0.1, 0), wedgeprops={"edgecolor": "black"})
plt.axis("equal")
plt.title("Which candidate was referenced more?")
plt.legend(labels=["Biden", "Trump"], loc=4)
plt.tight_layout()
plt.show()
