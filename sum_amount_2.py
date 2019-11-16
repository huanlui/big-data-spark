from __future__ import print_function
from pyspark.sql import SparkSession,types, functions
import sys

    
if __name__=='__main__':
    
    in_ = sys.argv[1]
    out_ = sys.argv[2]
    
    spark = SparkSession.builder.getOrCreate()

    coupons = spark.read.csv(in_).select(['_c0','_c1','_c2','_c3','_c4','_c6'])
    old_names = ['_c0','_c1','_c2','_c3','_c4','_c6']
    new_names = ['tkt_number', 'coupon_number','origin', 'destination', 'carrier', 'amount']

    for old, new in zip(old_names, new_names):
        coupons = coupons.withColumnRenamed(old, new)
    

    coupons = coupons.withColumn('amount_float', coupons['amount'].cast(types.FloatType()))
    
    amounts = coupons.filter(coupons['destination'] == 'MAD')\
       .groupby('origin')\
       .sum('amount_float')

    amounts.write.json(out_)

    spark.stop()
