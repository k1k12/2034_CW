import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
wine_red = pd.read_csv("datasets/winequality-red.csv",sep=";")
wine_white = pd.read_csv("datasets/winequality-white.csv",sep=";")
wine_red.columns = wine_red.columns.str.strip()
wine_white.columns = wine_white.columns.str.strip()

# Set global style
sns.set_theme(style="whitegrid", font_scale=1.2)
palette_red = sns.color_palette("Reds_r", as_cmap=True)
palette_white = sns.color_palette("Blues", as_cmap=True)

# For Combined plot: red vs white
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Plot set up

# Red
sns.countplot(data=wine_red, x="quality", hue="quality",ax=axes[0],palette="Reds_r",legend=False)
axes[0].set_title("Red Wine Quality",fontsize=14)
axes[0].set_xlabel("Quality Score")
axes[0].set_ylabel("Count")

# White
sns.countplot(data=wine_white, x="quality",hue="quality",ax=axes[1],palette="Blues",legend=False)
axes[1].set_title("White Wine Quality",fontsize=14)
axes[1].set_xlabel("Quality Score")
axes[1].set_ylabel("Count")

# Both plot
plt.suptitle("Quality Distributions: Red vs White Wine", fontsize=16, weight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("figures/wine_quality_comparison.png", dpi=300)
plt.show()

# Red wine plot
plt.figure(figsize=(8, 5))
sns.countplot(data=wine_red, x="quality", hue="quality", palette="Reds_r", legend=False)
plt.title("Red Wine Quality Distribution", fontsize=14)
plt.xlabel("Quality Score")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig('figures/red_wine_quality.png', dpi=300)
plt.show()

# White wine plot
plt.figure(figsize=(8, 5))
sns.countplot(data=wine_white, x="quality", hue="quality", palette="Blues", legend=False)
plt.title("White Wine Quality Distribution", fontsize=14)
plt.xlabel("Quality Score")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("figures/white_wine_quality.png", dpi=300)
plt.show()
