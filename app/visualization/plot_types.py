import matplotlib.pyplot as plt
import numpy as np

from data.clean_data import get_clean_data
from core.config import clasif_folders, charts_folders, CHART_PAD_SIZE, CHART_TITLE_SIZE


def plot_types_charts(path):
    #Set variables
    df = get_clean_data()
    #Matplotlib
    plt.rcParams['font.family'] = "serif"
    users_colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99'] 

    #paths -- FIX
    barchart_path = path / clasif_folders[1] / charts_folders[0]
    piechart_path = path / clasif_folders[1] / charts_folders[1]
    
    grouped_month = df.groupby(['Type','Month_year'],as_index=False)['Price'].sum()
    distinct_months = grouped_month['Month_year'].unique()
    types_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

    for i in distinct_months:
        df_month = grouped_month.loc[grouped_month['Month_year'] == i]
        distinct_types = df_month['Type'].unique()
        y_pos = np.arange(len(distinct_types))
        totalspent_pertype = df_month['Price']

        plot_types_barchart(y_pos, totalspent_pertype, distinct_types, barchart_path, types_colors, i )
        plot_types_piechart(totalspent_pertype, distinct_types, piechart_path, types_colors, i)

def plot_types_barchart(y_pos, totalspent_pertype, distinct_types, path, color, date):
    plt.bar(y_pos, totalspent_pertype, color = color)
    plt.xticks(y_pos, distinct_types)
    plt.ylabel('$ Pesos Argentinos')
    plt.title('Bugdet per type for month: ' + date.strftime('%m-%Y'), size = CHART_TITLE_SIZE, pad = CHART_PAD_SIZE)
    plt.savefig(f'{path}/{date}.jpg')
    plt.close()

def plot_types_piechart(totalspent_pertype, distinct_types, path, color, date,):
     #Donut pie chart
    fig1, ax1 = plt.subplots()
    ax1.pie(totalspent_pertype, colors=color, labels=distinct_types, autopct='%1.1f%%', 
            startangle=90, pctdistance=0.85, radius=1)
    #draw circle
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Percentage per type for month: ' + date.strftime('%m-%Y'), size = CHART_TITLE_SIZE, pad = CHART_PAD_SIZE)
    plt.savefig(f'{path}/{date}.jpg')
    plt.close()
