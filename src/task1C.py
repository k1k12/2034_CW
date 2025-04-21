from utils import init_data
import matplotlib.pyplot as plt
import seaborn as sns

# Plot set up

wine_red, wine_white, palette_red, palette_white = init_data()

# Add is sweet category
def add_is_sweet(df):
    threshold = df["residual sugar"].median()
    return df.assign(isSweet=(df["residual sugar"] >= threshold).astype(int))

# Apply to both datasets
wine_red = add_is_sweet(wine_red)
wine_white = add_is_sweet(wine_white)

# Red wine
plt.figure(figsize=(10, 5))
sns.boxplot(data=wine_red, x="isSweet", y="quality", palette="Reds", hue="isSweet")
plt.title("Red Wine Quality by Sweet Category")
plt.savefig("figures/red_quality_by_sugar.png")
plt.show()

# White wine
plt.figure(figsize=(10, 5))
sns.boxplot(data=wine_white, x="isSweet", y="quality", palette="Blues", hue="isSweet")
plt.title("White Wine Quality by Sweet Category")
plt.savefig("figures/white_quality_by_sugar.png")
plt.show()
