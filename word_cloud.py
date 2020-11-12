import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import STOPWORDS, WordCloud

df = pd.read_csv("./misc/chanlog.csv")

STOPWORDS = set(STOPWORDS)

words = ""

for msg in df["user_msg"]:
    msg = str(msg)
    tokens = msg.split()

    words += " ".join(tokens) + " "

wordcloud = WordCloud(width=1920, height=1080, background_color="black", random_state=1,
                      collocations=False, stopwords=STOPWORDS, min_font_size=12).generate(words)

plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout()
plt.savefig("word_cloud.png")
