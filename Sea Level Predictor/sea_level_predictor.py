import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')

    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='b', label='Data')
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years = range(1880, 2051)
    plt.plot(years, slope * years + intercept, 'r', label='Best Fit Line (1880-2050)')
    df_recent = df[df['Year'] >= 2000]

    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

    years_recent = range(2000, 2051)
    plt.plot(years_recent, slope_recent * years_recent + intercept_recent, 'g', label='Best Fit Line (2000-2050)')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    plt.savefig('sea_level_plot.png')

  
    return plt

draw_plot()