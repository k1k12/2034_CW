
from utils import init_data
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from scipy.stats import ttest_ind

# Load data
wine_red, wine_white, _, _ = init_data()

# 1. Plot quality vs alcohol_cat and isSweet (for both red and white)
for wine_df, name in [(wine_red, "Red"), (wine_white, "White")]:
    print(f"Plotting quality vs alcohol_cat and isSweet for {name} wine...")
    sns.boxplot(data=wine_df, x="alcohol_cat", y="quality", hue="isSweet")
    plt.title(f"{name} Wine Quality by Alcohol Category and Sweetness")
    plt.show()

# 2. Compare red vs white quality statistically
print("Comparing quality between red and white wines...")
print("Mean Quality (Red):", wine_red["quality"].mean())
print("Mean Quality (White):", wine_white["quality"].mean())

t_stat, p_val = ttest_ind(wine_red["quality"], wine_white["quality"])
print(f"T-test result: t={t_stat:.3f}, p={p_val:.3e}")

# 3. Combine datasets and see if 'type' affects prediction
print("\nCombining red and white data into one model...")

wine_red["type"] = "red"
wine_white["type"] = "white"
wine_all = pd.concat([wine_red, wine_white])

# One-hot encode 'type'
wine_all = pd.get_dummies(wine_all, columns=["type"], drop_first=True)

# Binary classification with threshold >= 6
wine_all["quality_label"] = (wine_all["quality"] >= 6).astype(int)
X = wine_all.drop(columns=["quality", "quality_label"])
y = wine_all["quality_label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

clf = RandomForestClassifier(random_state=42).fit(X_train_scaled, y_train)
y_pred = clf.predict(X_test_scaled)
print("Accuracy with wine type as feature:", accuracy_score(y_test, y_pred))

# 4. Drop one highly correlated feature (e.g. total sulfur dioxide) and retrain
print("Dropping 'total sulfur dioxide' to reduce redundancy...")
X_dropped = wine_red.drop(columns=["quality", "quality_label", "total sulfur dioxide"])
y = wine_red["quality_label"]

X_train, X_test, y_train, y_test = train_test_split(X_dropped, y, stratify=y, random_state=42)
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

clf = RandomForestClassifier(random_state=42).fit(X_train_scaled, y_train)
y_pred = clf.predict(X_test_scaled)
print("Accuracy without total sulfur dioxide:", accuracy_score(y_test, y_pred))

# 5. Multi-class classification (predict all quality labels)
print("Multi-class classification: predicting all quality labels (red wine)...")
X = wine_red.drop(columns=["quality_label", "quality"])
y = wine_red["quality"]

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

clf = RandomForestClassifier(random_state=42).fit(X_train_scaled, y_train)
y_pred = clf.predict(X_test_scaled)

print("Classification report (multi-class):")
print(classification_report(y_test, y_pred))
