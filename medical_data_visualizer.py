import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def draw_cat_plot():
    df = pd.read_csv('medical_examination.csv')

    df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

    df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
    df['gluc'] = (df['gluc'] > 1).astype(int)

    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    sns.catplot(x='variable', hue='value', data=df_cat, kind='count', col='cardio')

    plt.show()

    return None

def draw_heat_map():
    df = pd.read_csv('medical_examination.csv')

    df = df[(df['ap_lo'] <= df['ap_hi'])
            & (df['height'] >= df['height'].quantile(0.025))
            & (df['height'] <= df['height'].quantile(0.975))
            & (df['weight'] >= df['weight'].quantile(0.025))
            & (df['weight'] <= df['weight'].quantile(0.975))]

    corr_matrix = df.corr()

    mask = np.triu(corr_matrix)
    sns.heatmap(corr_matrix, annot=True, fmt='.1f', cmap='hot', mask=mask)

    plt.show()

    return None

# Uncommit or commit to see each one plot
draw_cat_plot()
draw_heat_map()