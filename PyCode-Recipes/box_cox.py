def main():
    # DataFrame is already loaded as "df"
    from scipy import stats
    import pandas as pd
    import json

    # Enter the column which has integer data type.Column should be >=0
    col = ''


    if df.empty:
        raise ValueError('Data Loading failed !')

    if col in df:
        transform = df[col].values
        # transform values and store as "dft"
        dft = stats.boxcox(transform)
        df['box_cox'] = dft[0]

    return df
