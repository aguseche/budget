import matplotlib.pyplot as plt
import numpy as np

from data.clean_data import get_clean_data
from core.config import clasif_folders, charts_folders, CHART_PAD_SIZE, CHART_TITLE_SIZE

def plot_users_charts(path):
    #Set variables
    df = get_clean_data()
    #Matplotlib
    plt.rcParams['font.family'] = "serif"
    users_colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99'] 

    #paths -- FIX
    barchart_path = path / clasif_folders[0] / charts_folders[0]
    piechart_path = path / clasif_folders[0] / charts_folders[1]
    
    grouped_month = df.groupby(['User','Month_year'],as_index=False)['Price'].sum()
    distinct_months = grouped_month['Month_year'].unique()
    for i in distinct_months:
        df_month = grouped_month.loc[grouped_month['Month_year'] == i]
        distinct_users = df_month['User'].unique()
        y_pos = np.arange(len(distinct_users))
        totalspent_peruser = df_month['Price']

        plot_users_barchart(y_pos, totalspent_peruser, distinct_users, barchart_path, users_colors, i )
        plot_users_piechart(totalspent_peruser, distinct_users, piechart_path, users_colors, i)
    return distinct_months

def plot_users_barchart(y_pos, totalspent_peruser, distinct_users, path, color, date):
    plt.bar(y_pos, totalspent_peruser, color = color)
    plt.xticks(y_pos, distinct_users)
    plt.ylabel('$ Pesos Argentinos')
    plt.title('Bugdet per person for month: ' + date.strftime('%m-%Y'), size = CHART_TITLE_SIZE, pad = CHART_PAD_SIZE)
    plt.savefig(f'{path}/{date}.jpg')
    plt.close()

def plot_users_piechart(totalspent_peruser, distinct_users, path, color, date,):
     #Donut pie chart
    fig1, ax1 = plt.subplots()
    ax1.pie(totalspent_peruser, colors=color, labels=distinct_users, autopct='%1.1f%%', 
            startangle=90, pctdistance=0.85, radius=1)
    #draw circle
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Percentage per person for month: ' + date.strftime('%m-%Y'), size = CHART_TITLE_SIZE, pad = CHART_PAD_SIZE)
    plt.savefig(f'{path}/{date}.jpg')
    plt.close()

