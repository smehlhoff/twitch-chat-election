import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("./misc/chanlog.csv")

biden = 0
trump = 0

for msg in df["user_msg"]:
    msg = str(msg)
    msg = msg.lower().split()

    for word in msg:
        if "biden" in word:
            biden += 1
        # ensure TTrump emote is not counted
        elif "trump" in word and word != "ttrump":
            trump += 1

biden_emotes = 0
trump_emotes = 0

# include these emotes because their usage represents biden or trump
_biden_emotes = ["MALARKEY"]
_trump_emotes = ["CHYNA", "DonaldPls", "TTrump"]

for msg in df["user_msg"]:
    msg = str(msg)
    msg = msg.split()

    for word in msg:
        if word in _biden_emotes:
            biden_emotes += 1
        elif word in _trump_emotes:
            trump_emotes += 1

sizes = [biden, trump]
sizes2 = [biden_emotes, trump_emotes]

plt.style.use('fivethirtyeight')

fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle("Which candidate had more mentions?")

ax1.pie(sizes, autopct="%1.1f%%", explode=(0.1, 0), wedgeprops={"edgecolor": "black"})
ax1.axis("equal")
ax1.title.set_text("Words")
ax1.legend(labels=["Biden", "Trump"], loc=4)

ax2.pie(sizes2, autopct="%1.1f%%", explode=(0.1, 0), wedgeprops={"edgecolor": "black"})
ax2.axis("equal")
ax2.title.set_text("Emotes")
ax2.legend(labels=["Biden", "Trump"], loc=4)

plt.tight_layout()
plt.show()
