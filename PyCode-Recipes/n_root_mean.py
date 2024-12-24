def main():
    # DataFrame is already loaded as "df"
    # Enter column names in the list defined below
    columns = []
    # pass the float value in n variable for find n_root_mean value
    m = None

    import pandas as pd
    import math
    import json


    if df.empty:
        raise ValueError('Data Loading failed !')

    for col in columns:
        if col in df.columns:
            df[col + "_n_root"] = df[col] ** m

    return df
