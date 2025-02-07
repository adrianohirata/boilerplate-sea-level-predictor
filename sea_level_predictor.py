import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots()

    df.plot(ax=ax, x='Year', y='CSIRO Adjusted Sea Level', kind='scatter')

    # Create first line of best fit
    res = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    # numpy array with years 1850 - 2075
    year_range = np.arange(1850, 2100, 25)

    ax.set_xticks(year_range)

    ax.plot(year_range, res.intercept + res.slope*year_range, 'r')

    # Create second line of best fit
    df_recent = df[( (df['Year'] >= 2000) ) & ( df['Year'] <= df['Year'].max() )]

    res_recent = linregress(x=df_recent['Year'], y=df_recent['CSIRO Adjusted Sea Level'])

    year_range_recent = np.arange(2000, 2100, 25)
    ax.plot(year_range_recent, res_recent.intercept + res_recent.slope*year_range_recent, 'b')

    # Add labels and title
    ax.set_title("Rise in Sea Level")
    ax.set_ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()