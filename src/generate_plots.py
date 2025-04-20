import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

wine_red = pd.read_csv("datasets/winequality-red.csv",sep=";")
wine_white = pd.read_csv("datasets/winequality-white.csv",sep=";")
wine_red.columns = wine_red.columns.str.strip()
wine_white.columns = wine_white.columns.str.strip()

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.countplot(data=wine_red, x="quality",ax=axes[0])
axes[0].set_title("Red Wine Quality Distribution")

sns.countplot(data=wine_white, x="quality",ax=axes[1])
axes[1].set_title("White Wine Quality Distribution")

plt.tight_layout()
plt.savefig('figures/wine_quality_comparison.png')
plt.show()

sns.countplot(data=wine_red, x="quality")
plt.savefig('figures/red_wine_quality.png')
plt.title("Red Wine Quality Distribution")
plt.show()

sns.countplot(data=wine_red, x="quality")
plt.savefig('figures/white_wine_quality.png')
plt.title("White Wine Quality Distribution")
plt.show()
