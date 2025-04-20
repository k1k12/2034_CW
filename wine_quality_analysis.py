import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

wine_red = pd.read_csv('datasets/winequality-red.csv')
wine_white = pd.read_csv('datasets/winequality-white.csv')

sns.countplot(data=wine_red, x='quality')
sns.countplot(data=wine_white, x='quality')
