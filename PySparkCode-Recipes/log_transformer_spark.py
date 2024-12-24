def main():
    # Spark SQL DataFrame is already loaded as "df"
    # Spark Session is already loaded as "spark"
    # Enter column which has integer or float data type
    column = ''
    
    import pyspark.sql.functions as F
    import pyspark.sql.types as T
    import numpy as np
    

    if df.isEmpty():
        raise ValueError('Data Loading failed !')
    
    @F.udf(returnType=T.DoubleType())
    def log_10(val):
        return float(np.log10(val))

    if column in df.columns:
        df = df.withColumn("logarithm_base10", log_10(F.col(column)))

    return df
