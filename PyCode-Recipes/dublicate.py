def main(f):
    import pandas as pd 
    import numpy as np 
    df = df.astype(str)
    df.replace(['NULL', 'nan', '','null','NaN'], np.nan, inplace=True)
    delete_duplicat = df.drop_duplicates(subset=['cola','colb','colc'], keep='first')

    if delete_duplicat.empty:
        raise ValueError('No unique records remain after dropping all duplicates from selected column!')
    else:
        cols = list(delete_duplicat.columns)
        delete_duplicat = delete_duplicat.drop_duplicates(subset=cols, keep='first')

    return delete_duplicat
