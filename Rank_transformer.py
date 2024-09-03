def main():
    # DataFrame is already loaded as "df"
    # Enter the column names in the list below
    col = []

    import pandas as pd
    from numpy import log
    from numpy import sqrt


    if df.empty:
        raise ValueError('Data Loading failed !')

    for c in col:
        if c in df:
            df[c + 'rank_col'] = df[c].rank()

    return df