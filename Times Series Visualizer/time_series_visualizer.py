import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def draw_line_plot():
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

    df_cleaned = df[
        (df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))
    ]

    plt.figure(figsize=(14, 6))
    plt.plot(df_cleaned.index, df_cleaned['value'], color='r')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.savefig('line_plot.png')
    plt.close()

    return None

def draw_bar_plot():
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

    df_cleaned = df[
        (df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))
    ]

    df_cleaned['year'] = df_cleaned.index.year
    df_cleaned['month'] = df_cleaned.index.month_name()

    df_pivot = df_cleaned.pivot_table(values='value', index='year', columns='month', aggfunc='mean')
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    ax = df_pivot.plot(kind='bar', figsize=(14, 6))
    plt.legend(title='Months', labels=month_order)
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.title('Average Daily Page Views for Each Month Grouped by Year')

    plt.savefig('bar_plot.png')
    plt.close()

    return None


def draw_box_plot():
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

    df_cleaned = df[
        (df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))
    ]

    df_cleaned['year'] = df_cleaned.index.year
    df_cleaned['month'] = df_cleaned.index.month_name()
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    fig, axes = plt.subplots(1, 2, figsize=(20, 10))
    sns.boxplot(x='year', y='value', data=df_cleaned, ax=axes[0])
    sns.boxplot(x='month', y='value', data=df_cleaned, order=month_order, ax=axes[1])

    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    plt.savefig('box_plot.png')
    plt.close()

    return None

draw_line_plot()
draw_bar_plot()
draw_box_plot()
