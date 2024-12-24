def main():
    # Spark SQL DataFrame is already loaded as "df"
    # Spark Session is already loaded as "spark"
    # Enter column names in the list defined below
    columns = []
    # pass the float value in n variable for find n_root_mean value
    m = None

    import pyspark.sql.functions as F
    import pyspark.sql.types as T


    if df.isEmpty():
        raise ValueError('Data Loading failed !')
    
    if m > 1:
        m = 1/m
    
    @F.udf(returnType=T.DoubleType())
    def n_root(val):
        return float(val ** m)

    for col in columns:
        if col in df.columns:
            df = df.withColumn(f"{col}_n_root", n_root(F.col(col)))

    return df
