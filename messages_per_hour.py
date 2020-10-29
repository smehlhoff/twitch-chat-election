from statistics import mean

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("./misc/chanlog.csv")

df["timestamp"] = pd.to_datetime(df["timestamp"])
df["hour"] = df["timestamp"].dt.hour

series = df.groupby(["hour"])["username"].count()

mean_val = mean(series)

plt.plot(series, marker="o")
plt.axhline(mean_val, color="red", linestyle="--")
plt.locator_params(axis="both", integer=True)
plt.xlabel("Hour")
plt.ylabel("Number of messages")
plt.title("Number of messages per hour")
plt.legend(labels=["Messages", "Mean"], loc=4)
plt.text(18.5, 22000, f"{mean_val}")
plt.tight_layout()
plt.show()
