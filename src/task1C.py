from utils import init_data
import matplotlib.pyplot as plt
import seaborn as sns

# Plot set up

wine_red, wine_white, palette_red, palette_white = init_data()

# Add is sweet category
def define_is_sweet(df):
    mean = df["residual sugar"].mean()
    std = df["residual sugar"].std()
    
    def categorize(sugar):
        if sugar < mean - std:
            return 0
        elif sugar > mean + std:
            return 1
        else:
            return 0
    
    return df.assign(define_is_sweet=df["residual sugar"].apply(categorize))
