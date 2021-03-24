import matplotlib.pyplot as plt
import numpy as np

from data.clean_data import get_clean_data

def plot_charts():
    #Set variables
    df = get_clean_data()
    #Users
    distinct_users = df['User'].unique()
    y_pos_users = np.arange(len(distinct_users))
    totalspent_peruser = df.groupby(['User'])['Price'].sum()
    users_colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
    #Types
    distinct_types = df['Type'].unique()
    totalspent_pertype = df.groupby('Type').sum()['Price']
    types_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
    y_pos_types = np.arange(len(distinct_types))
    #Matplotlib
    plt.rcParams['font.family'] = "serif"

    #Plot
    plot_users_barchart(y_pos_users, totalspent_peruser, users_colors, distinct_users)
    plot_users_piechart(totalspent_peruser, users_colors, distinct_users)

    plot_types_barchart(y_pos_types, totalspent_pertype, types_colors, distinct_types)
    plot_types_piechart(totalspent_pertype, types_colors, distinct_types)


    '''Users'''
def plot_users_barchart(y_pos, totalspent_peruser, users_colors, distinct_users):
    plt.bar(y_pos, totalspent_peruser, color = users_colors)
    plt.xticks(y_pos, distinct_users)
    plt.ylabel('$ Pesos Argentinos')
    plt.title('Amount of money spent by person', fontsize=20, pad=20)
    plt.savefig('./results/users_barchart.jpg')
    plt.close()


def plot_users_piechart(totalspent_peruser, users_colors, distinct_users):
    #Donut pie chart
    fig1, ax1 = plt.subplots()
    ax1.pie(totalspent_peruser, colors=users_colors, labels=distinct_users, autopct='%1.1f%%', 
            startangle=90, pctdistance=0.85, radius=1)

    #draw circle
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Percentage of money spent by person', fontsize=20, pad=20)
    plt.savefig('./results/users_piechart.jpg')
    plt.close()



    '''Types'''
def plot_types_barchart(y_pos_types,totalspent_pertype, types_colors, distinct_types):
    plt.bar(y_pos_types, totalspent_pertype, color = types_colors)
    plt.xticks(y_pos_types, distinct_types)
    plt.ylabel('$ Pesos Argentinos')
    plt.xlabel('')
    plt.title('Amount of money spent per type', fontsize=20, pad=20)
    plt.savefig('./results/types_barchart.jpg')
    plt.close()


def plot_types_piechart(totalspent_pertype, types_colors, distinct_types):
    #donut piechart
    fig1, ax1 = plt.subplots()
    ax1.pie(totalspent_pertype, colors=types_colors, labels=distinct_types, autopct='%1.1f%%', 
        startangle=90, pctdistance=0.85, radius=1)
    #draw circle
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Percentage of money spent per type', fontsize=20, pad=20)
    plt.savefig('./results/types_piechart.jpg')
    plt.close()

