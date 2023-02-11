import pandas as pd
import numpy as np

def get_temperature(state, district, month):
    # state_district = df[df['STATE_UT_NAME'].values == state and df['DISTRICT'].values == district]
    # index = int(np.argwhere(df['STATE_UT_NAME'].values == state and df['DISTRICT'].values == district))
    df = pd.read_csv('data/district wise rainfall normal.csv')
    index = int(np.intersect1d(np.argwhere(df['STATE_UT_NAME'].values == state), np.argwhere(df['DISTRICT'].values == district)))
    temperature = df[month].values[index] 
       
    return temperature
