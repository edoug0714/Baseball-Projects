import pandas as pd
import numpy as np

def main():
    print("2021 Pitching Stats Leaders: \n")
    exit_velo()
    strikeouts()


def exit_velo():
    data = pd.read_csv('Statcast_2021.csv')
    list = ['SI', 'FF']
    data = data[data['pitch_type'].isin(list)]
    data = data[['release_speed', 'player_name']]
    average_velo = data.groupby(['player_name']).mean()
    average_velo = average_velo.sort_values(by='release_speed', ascending=False)
    print("Highest Fastball Exit Velo:")
    print(average_velo.head(5))
    print('\n')

def strikeouts():
    data = pd.read_csv('Statcast_2021.csv')
    data = data[['events', 'player_name']]
    data = data[data['events'] == 'strikeout']
    strikeouts = data.groupby(['player_name']).count().sort_values(by='events', ascending=False)
    print("Strikeout Leaders 2021:")
    print(strikeouts.head())
    print('\n')




main()
