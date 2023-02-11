import pandas as pd


def get_rainfall(state, district, month):
    df = pd.read_csv('data/district wise rainfall normal.csv')
    row = df[(df['STATE_UT_NAME'] == state) & (df['DISTRICT'] == district)]
    rainfall = row[month].values
    if rainfall.shape[0] == 0:
        raise Exception(
            f"Unable to match month:{month} with the state:{state} and district:{district}")
    return rainfall
