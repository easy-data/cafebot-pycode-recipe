def main():
    # DataFrame is already loaded as "df"
    # Enter the column name in a list columns
    columns = []
    # Enter 'add' or'sub'or'mul' or 'div' in oper
    oper = ''

    import pandas as pd
    import json


    if df.empty:
        raise ValueError('Data Loading failed !')

    for col in columns[0:1]:
        if oper == 'add':
            df['add'] = df[col]
        elif oper == 'sub':
            df['sub'] = df[col]
        elif oper == 'mul':
            df['mul'] = df[col]
        elif oper == 'div':
            df['div'] = df[col]
        else:
            pass
            # Uncomment the line below to get your data
            # return

        for _col in columns[1:]:
            if oper == 'add':
                df['add'] += df[_col]

            elif oper == 'sub':
                df['sub'] -= df[_col]

            elif oper == 'mul':
                df['mul'] *= df[_col]

            elif oper == 'div':
                df['div'] /= df[_col]

            else:
                pass
                # Uncomment the line below to get your data
                # return

    return df
