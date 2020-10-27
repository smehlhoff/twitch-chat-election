import pandas as pd
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS

df = pd.read_csv("./misc/chanlog.csv")

data = df.loc[df['command'] == "PRIVMSG"]

words = ""
stopwords = set(STOPWORDS)

for val in data.user_msg:
    val = str(val)
    tokens = val.split()

    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()

    words += " ".join(tokens) + " "

wordcloud = WordCloud(width=1920, height=1080, background_color="black", random_state=1,
                      collocations=False, stopwords=stopwords, min_font_size=14).generate(words)

plt.imshow(wordcloud)
plt.axis("off")
plt.show()
