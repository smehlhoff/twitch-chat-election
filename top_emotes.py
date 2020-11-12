import json
import re
from collections import Counter

import matplotlib.pyplot as plt
import pandas as pd
import requests

df = pd.read_csv("./misc/chanlog.csv")


def fetch_emotes(url: str, id: str) -> str:
    try:
        resp = requests.get(f"{url}{id}")
        json = resp.json()
    except requests.exceptions.RequestException as e:
        print(e)

    return json


global_emotes = []

with open("global_emotes.txt", "r") as f:
    for line in f.readlines():
        line = line.replace("\n", "")
        global_emotes.append(line)


# https://twitchemotes.com/apidocs
data = fetch_emotes(url="https://api.twitchemotes.com/api/v4/channels/", id="207813352")

channel_emotes = [emote["code"] for emote in data["emotes"]]

# https://www.frankerfacez.com/developers
data = fetch_emotes(url="https://api.frankerfacez.com/v1/room/", id="hasanabi")

_set = str(data["room"]["set"])
frankerz_emotes = [emote["name"] for emote in data["sets"][_set]["emoticons"]]

# https://github.com/pajbot/pajbot/issues/495
data = fetch_emotes(url="https://api.betterttv.net/3/cached/users/twitch/", id="207813352")

betterttv_emotes = [emote["code"] for emote in data["channelEmotes"]]
betterttv_emotes += [emote["code"] for emote in data["sharedEmotes"]]

emotes = []

for msg in df["user_msg"]:
    msg = str(msg)
    msg = msg.split()

    for emote in msg:
        if emote in global_emotes or emote in channel_emotes or emote in frankerz_emotes or emote in betterttv_emotes:
            emotes.append(emote)

emotes = dict(Counter(emotes).most_common(10))

x = list(emotes.keys())
y = list(emotes.values())

plt.barh(x, y)
plt.xlabel("Emote count")
plt.ylabel("Emote code")
plt.title("Top 10 emotes used")
plt.tight_layout()
plt.savefig("top_emotes.png")
