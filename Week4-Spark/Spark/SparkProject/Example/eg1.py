from pyspark.sql import SparkSession

import sys
import os
os.environ["JAVA_HOME"] = "C:/Program Files/Java/jdk-21"
os.environ["SPARK_HOME"] = "C:/Users/Shree/OneDrive/Desktop/Training Folder/Week4-Spark/Spark/SparkProject/.venv/Lib/site-packages/pyspark"
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession.builder \
    .appName("Local PySpark") \
    .getOrCreate()

#Get SparkContext
sc = spark.sparkContext

numbers = [1,2,3,4,5]
rdd = sc.parallelize(numbers)
print("Original RDD: ", rdd.collect())

#Transformations
doubled = rdd.map(lambda x: x * 2)
print('type : ', type(doubled))
print("Doubled: ", doubled.collect())

even_num= rdd.filter(lambda x: x%2==0)
print('type : ', type(even_num))
print("Even num: ", even_num.collect())

total = rdd.reduce(lambda x, y: x + y)
print('type : ', type(total))
print("Total Sum: ", total)