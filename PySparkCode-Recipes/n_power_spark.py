def main():
    # Spark SQL DataFrame is already loaded as "df"
    # Spark Session is already loaded as "spark"
    # Enter column names in the list defined below
    columns = []
    # pass the integer value in n variable for find square
    n = None
    import pyspark.sql.functions as F
    import pyspark.sql.types as T
    
    
    if df.isEmpty():
        raise ValueError('Data Loading failed !')
    
    @F.udf(returnType=T.DoubleType())
    def get_power(val):
        return float(val ** n)

    for col in columns:
        if col in df.columns:
            df = df.withColumn(f"{col}_n_power", get_power(F.col(col)))

    return df