import matplotlib.pyplot as plt
import numpy as np

from data.clean_data import get_clean_data

def plot_types():
    #Set variables
    df = get_clean_data()
    types_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']    
    distinct_types = df['Type'].unique()
    distinct_types.sort()

    #Matplotlib
    plt.rcParams['font.family'] = "serif"

    #Plot
    plot_types_barchart(df, types_colors)
    plot_types_piechart(df, types_colors, distinct_types)


def plot_types_barchart(df, types_colors):
    df.groupby('Type').sum()['Price'].plot.bar(color = types_colors)
    plt.xticks(rotation=0)
    plt.ylabel('$ Pesos Argentinos')
    plt.xlabel('')
    plt.title('Amount of money spent per type', fontsize=20)
    plt.savefig('./results/types_barchart.jpg')

def plot_types_piechart(df, types_colors, distinct_types):
    #donut piechart
    plt.pie(df.groupby('Type').sum()['Price'], labels=distinct_types, autopct='%1.1f%%', colors = types_colors,startangle=90, pctdistance=0.85)

    #draw circle
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig('./results/types_piechart.jpg')
