import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

wine_red = pd.read_csv("datasets/winequality-red.csv",sep=";")
wine_white = pd.read_csv("datasets/winequality-white.csv",sep=";")
wine_red.columns = wine_red.columns.str.strip()
wine_white.columns = wine_white.columns.str.strip()

sns.countplot(data=wine_red, x="quality")
plt.title("Red Wine Quality Distribution")
plt.show()

sns.countplot(data=wine_white, x="quality")
plt.title("White Wine Quality Distribution")
plt.show()