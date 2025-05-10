# 3
from utils import init_data
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import (
    classification_report,
    roc_auc_score,
    mean_squared_error,
    mean_absolute_error,
    r2_score,
)


wine_red, wine_white, palette_red, palette_white = init_data()

df = wine_red.copy()

thresholds = [5, 6, 7]
for thresh in thresholds:
    print(f"\n thresh: {thresh}")

    df["quality_label"] = (df["quality"] >= thresh).astype(int)

    x = df.drop(columns=["quality", "quality_label"])
    y = df["quality_label"]

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, stratify=y, random_state=42
    )

    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)

    clf = RandomForestClassifier(random_state=42)

    scores = cross_val_score(clf, x_train_scaled, y_train, cv=5, scoring="f1")
    print(f"F1-score (CV): {scores.mean():.3f}")

    clf.fit(x_train_scaled, y_train)
    y_pred = clf.predict(x_test_scaled)

    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    roc = roc_auc_score(y_test, clf.predict_proba(x_test_scaled)[:, 1])
    print(f"ROC AUC: {roc:.3f}")


print("\n ######### Try with regression #########")

x = df.drop(columns=["quality", "quality_label"])
y = df["quality"]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

reg = RandomForestRegressor(random_state=42)

######## TASK 4

cv_mse = cross_val_score(reg, x_train_scaled, y_train, cv=5, scoring="neg_mean_squared_error")
rmse_scores = np.sqrt(-cv_mse)
print(f"RMSE (CV): {rmse_scores.mean():.3f}")

reg.fit(x_train_scaled, y_train)
y_pred_reg = reg.predict(x_test_scaled)

mse = mean_squared_error(y_test, y_pred_reg)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred_reg)
r2 = r2_score(y_test, y_pred_reg)

print(f"Test Set Evaluation:")
print(f"RMSE: {rmse:.3f}")
print(f"MAE: {mae:.3f}")
print(f"R²: {r2:.3f}")
