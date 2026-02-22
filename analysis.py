import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
data = pd.read_csv("happiness.csv")

# Sort data by avg_income (highest first)
data = data.sort_values("avg_income", ascending=False)

# Filter: keep countries with avg_income > 10000
filtered = data[data["avg_income"] > 10000]

# Plot
plt.figure(figsize=(8,6))
plt.scatter(filtered["avg_income"], filtered["happyScore"], alpha=0.7)

# Label a few interesting countries (top 3 happiest)
top_happy = filtered.sort_values("happyScore", ascending=False).head(3)

for i, row in top_happy.iterrows():
    plt.text(row["avg_income"], row["happyScore"], row["country"])

# Axis labels
plt.xlabel("Average Income")
plt.ylabel("Happiness Score")

plt.title("Happiness vs Average Income")
plt.show()