def get_rainfall(state, district, month):
    df = pd.read_csv('data/district wise rainfall normal.csv')
    index = int(np.intersect1d(np.argwhere(df['STATE_UT_NAME'].values == state), np.argwhere(df['DISTRICT'].values == district)))
    rainfall = df[month].values[index] 
    return rainfall
