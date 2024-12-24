def main():
    # DataFrame is already loaded as "df"
    # enter the column name which has integer or float datatype
    column_1 = ''
    column_2 = ''
    # Enter the exponent values for the two columns
    m = None
    n = None

    import pandas as pd
    import math
    import json


    if df.empty:
        raise ValueError('Data Loading failed !')

    if column_1 in df.columns and column_2 in df.columns:
        df['exp'] = pow(df[column_1], m) - pow(df[column_2], n)

    return df
