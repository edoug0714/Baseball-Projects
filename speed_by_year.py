import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    fastball = ['FF', 'SI', 'FT']

    data_2017 = pd.read_csv('statcast_2017.csv')
    data_2018 = pd.read_csv('Statcast_2018.csv')
    data_2019 = pd.read_csv('Statcast_2019.csv')
    data_2020 = pd.read_csv('Statcast_2020.csv')
    data_2021 = pd.read_csv('Statcast_2021.csv')

    data_2017 = data_2017[data_2017['pitch_type'].isin(fastball)]
    data_2018 = data_2018[data_2018['pitch_type'].isin(fastball)]
    data_2019 = data_2019[data_2019['pitch_type'].isin(fastball)]
    data_2020 = data_2020[data_2020['pitch_type'].isin(fastball)]
    data_2021 = data_2021[data_2021['pitch_type'].isin(fastball)]

    aev_2017 = data_2017['release_speed'].mean()
    aev_2018 = data_2018['release_speed'].mean()
    aev_2019 = data_2019['release_speed'].mean()
    aev_2020 = data_2020['release_speed'].mean()
    aev_2021 = data_2021['release_speed'].mean()

    index = [2017, 2018, 2019, 2020, 2021]
    speed = [aev_2017, aev_2018, aev_2019, aev_2020, aev_2021]

    data = pd.DataFrame(data=speed, index = index, columns = ['Exit Velo'])
    
    ax = data.plot.bar(ylim=(85, 95))
    #plt.plot(ax)
    plt.show()



    


main()