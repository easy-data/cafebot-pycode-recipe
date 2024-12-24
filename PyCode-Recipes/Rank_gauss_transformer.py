def main():
    # DataFrame is already loaded as "df"
    # Enter columns name  in col which have numerical values
    col = []
    
    from gauss_rank_scaler.gauss_rank_scaler import GaussRankScaler
    import pandas as pd
    
    
    if df.empty:
        raise ValueError('Data Loading failed !')
    
    for c in col:
        if c in df:
            scaler = GaussRankScaler()
            X = scaler.fit_transform(df[[c]])
            X_ = pd.DataFrame(X, columns=[c + '_gauss_rank'])
            df = df.join(X_)
    
    return df
