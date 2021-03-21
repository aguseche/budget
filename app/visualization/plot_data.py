import matplotlib.pyplot as plt
import numpy as np

from data.clean_data import get_clean_data

def plot_users():
    #Set variables
    df = get_clean_data()
    distinct_users = df['User'].unique()
    y_pos = np.arange(len(distinct_users))
    totalspent_peruser = df.groupby(['User'])['Price'].sum()
    users_colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

    #Plot
    plot_users_barchart(y_pos, totalspent_peruser, users_colors, distinct_users)
    plot_users_piechart(totalspent_peruser, users_colors, distinct_users)



def plot_users_barchart(y_pos, totalspent_peruser, users_colors, distinct_users):
    plt.bar(y_pos, totalspent_peruser, color = users_colors)
    plt.xticks(y_pos, distinct_users)
    plt.ylabel('$ Pesos Argentinos')
    plt.title('Amount of money spent by person')
    plt.savefig('./results/users_barchart.jpg')


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
    plt.savefig('./results/users_piechart.jpg')
