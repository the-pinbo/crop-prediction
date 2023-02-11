import pandas as pd


def get_rainfall(state, district, month):
    df = pd.read_csv('data/district wise rainfall normal.csv')
    row = df[(df['STATE_UT_NAME'] == state) & (df['DISTRICT'] == district)]
    rainfall = row[month].values[0]
    return rainfall
