import pandas as pd, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt, seaborn as sns 
sns.set_theme(style="whitegrid")
df = pd.read_csv("books.csv")

fig, ax = plt.subplots(2, 2, figsize=(13, 9))
fig.suptitle("Books Dashboard", fontsize=16, fontweight="bold")

sns.histplot(df.price, bins=15, kde=True, color="#4C72B0", ax=ax[0,0])
ax[0,0].set(title="Price Distribution", xlabel="Price (£)")

order = df.groupby("category").price.mean().sort_values().index
sns.barplot(data=df, x="price", y="category", order=order, hue="category", hue_order=order, dodge=False, errorbar=None, palette="viridis", legend=False, ax=ax[0,1])
ax[0,1].set(title="Average Price by Category", xlabel="Avg Price (£)", ylabel="")

sns.countplot(data=df, x="rating", hue="rating", palette="rocket", legend=False, ax=ax[1,0])
ax[1,0].set(title="Rating Count", xlabel="Star Rating")

sns.boxplot(data=df, x="rating", y="price", ax=ax[1,1])
ax[1,1].set(title="Price vs Rating", xlabel="Star Rating", ylabel="Price (£)")

plt.tight_layout()
plt.savefig("dashboard.png", dpi=120)
print("Saved: dashboard.png")