def main():
    # DataFrame is already loaded as "df"
    # Enter column names in the list defined below
    columns = []
    # pass the integer value in n variable for find square
    n = None
    import pandas as pd
    import math
    import json


    if df.empty:
        raise ValueError('Data Loading failed !')

    for col in columns:
        if col in df.columns:
            df[col + "_n_power"] = df[col] ** n

    return df
