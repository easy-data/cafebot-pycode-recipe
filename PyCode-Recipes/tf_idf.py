def main():
    # DataFrame is already loaded as "df"
    # Enter the column which has string data type
    column = ''
    import pandas as pd
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.feature_extraction.text import TfidfTransformer
    import json


    if df.empty:
        raise ValueError('Data Loading failed !')

    tfidf = TfidfVectorizer()
    if column in df:
        tf_idf_data = tfidf.fit_transform(df[column])
        tfidf_list = tf_idf_data.toarray()
        df_tfidf = pd.DataFrame(tfidf_list)

    return df_tfidf
