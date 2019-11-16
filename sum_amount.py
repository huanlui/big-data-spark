from __future__ import print_function
from pyspark.sql import SparkSession,types, functions
import sys

    
if __name__=='__main__':
    
    in_ = sys.argv[1]
    out_ = sys.argv[2]
    
    spark = SparkSession.builder.getOrCreate()

    df = spark.sql(f'''SELECT  
            _c0 AS tft_number,
            _c1 AS coupon_number,
            _c2 AS origin,
            _c3 AS destination,
            _c4 AS carrier,
            CAST(_c6 AS double) AS amount
            FROM csv.`{in_}`''')

    amounts = (
    df
    .where(df['origin'] == 'MAD')
    .groupBy('destination')
    .sum('amount')
    .withColumnRenamed('sum(amount)','sum_amount') 
    )

    amounts.write.json(out_)
    spark.stop()
