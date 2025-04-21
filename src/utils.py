import pandas as pd
import seaborn as sns

def init_data():
    # Load data
    wine_red = pd.read_csv("datasets/winequality-red.csv",sep=";")
    wine_white = pd.read_csv("datasets/winequality-white.csv",sep=";")
    wine_red.columns = wine_red.columns.str.strip()
    wine_white.columns = wine_white.columns.str.strip()

    # Set global style
    sns.set_theme(style="whitegrid", font_scale=1.2)
    palette_red = sns.color_palette("Reds_r", as_cmap=True)
    palette_white = sns.color_palette("Blues", as_cmap=True)

    return wine_red, wine_white, palette_red, palette_white
