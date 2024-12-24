def main():
    # dfFrame is already loaded as "df"
    # Enter the positive or negative or both in var
    var = ''

    import pandas as pd
    import math
    import numpy as np
    import json


    if df.empty:
        raise ValueError('df Loading failed !')

    if var == 'positive':
        df['positive_count'] = df.select_dtypes(include='number').ge(1).sum(axis=1)

    elif var == 'negative':
        df['negative_count'] = df.select_dtypes(include='number').lt(0).sum(axis=1)

    elif var == 'both':
        df['positive_count'] = df.select_dtypes(include='number').ge(1).sum(axis=1)
        df['positive_count'] = df.select_dtypes(include='number').lt(0).sum(axis=1)

    return df
