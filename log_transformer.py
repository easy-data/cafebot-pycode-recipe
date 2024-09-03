def main():
    # DataFrame is already loaded as "df"
    # Enter column which has integer or float data type
    column = ''
    import pandas as pd
    import math
    import numpy as np
    import json


    if df.empty:
        raise ValueError('Data Loading failed !')

    if column in df:
        df['logarithm_base10'] = np.log10(df[column])

    return df
