from utils import init_data
import matplotlib.pyplot as plt
import seaborn as sns

# Plot set up

wine_red, wine_white, palette_red, palette_white = init_data()

# Add alcohol category
def add_alcohol_category(df):
    mean = df["alcohol"].mean()
    std = df["alcohol"].std()
    
    def categorize(alc):
        if alc < mean - std:
            return "low"
        elif alc > mean + std:
            return "high"
        else:
            return "mid"
    
    return df.assign(alcohol_cat=df["alcohol"].apply(categorize))

# Apply to both datasets
wine_red = add_alcohol_category(wine_red)
wine_white = add_alcohol_category(wine_white)

# Red wine
plt.figure(figsize=(10, 5))
sns.boxplot(data=wine_red, x="alcohol_cat", y="quality", palette="Reds", hue="alcohol_cat")
plt.title("Red Wine Quality by Alcohol Category")
plt.savefig("figures/red_quality_by_alcohol.png")
plt.show()

# White wine
plt.figure(figsize=(10, 5))
sns.boxplot(data=wine_white, x="alcohol_cat", y="quality", palette="Blues", hue="alcohol_cat")
plt.title("White Wine Quality by Alcohol Category")
plt.savefig("figures/white_quality_by_alcohol.png")
plt.show()
