def main():
    # Spark SQL DataFrame is already loaded as "df"
    # Spark Session is already loaded as "spark"
    # Enter column names in the list defined below
    columns = ['ID']
    # pass the integer value in n variable for find square
    n = 3
    import pyspark.sql.functions as F
    import pyspark.sql.types as T
    
    ds=df
    if ds.isEmpty():
        raise ValueError('Data Loading failed !')
    
    @F.udf(returnType=T.DoubleType())
    def get_power(val):
        return float(val ** n)
    
    for col in columns:
        if col in ds.columns:
            ds = ds.withColumn(f"{col}_n_power", get_power(F.col(col)))
    return ds
 return main()
