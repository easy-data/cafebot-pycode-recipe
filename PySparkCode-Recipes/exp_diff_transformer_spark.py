def main():
    # Spark SQL DataFrame is already loaded as "df"
    # Spark Session is already loaded as "spark"
    # enter the column name which has integer or float datatype
    column_1 = ''
    column_2 = ''
    # Enter the exponent values for the two columns
    m = None
    n = None
    
    import pyspark.sql.functions as F
    import pyspark.sql.types as T


    if df.isEmpty():
        raise ValueError('Data Loading failed !')
    
    @F.udf(returnType=T.DoubleType())
    def expdiff(val1, val2):
        return float(val1**m - val2**n)

    if column_1 in df.columns and column_2 in df.columns:
        df = df.withColumn("exp", expdiff(F.col(column_1), F.col(column_2)))

    return df
