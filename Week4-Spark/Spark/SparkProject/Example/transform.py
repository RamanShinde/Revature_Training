from pyspark.sql import SparkSession

import sys
import os
os.environ["JAVA_HOME"] = "C:/Program Files/Java/jdk-21"
os.environ["SPARK_HOME"] = "C:/Users/Shree/OneDrive/Desktop/Training Folder/Week4-Spark/Spark/SparkProject/.venv/Lib/site-packages/pyspark"
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession.builder \
    .appName("CreateRDDExample") \
    .getOrCreate()

sc=spark.sparkContext

# numbers=[1,3,10,54,22]
# rdd=sc.parallelize(numbers)
# print("print Rdd:-",rdd.collect())
# print("Find max:-",rdd.max())
# print("Find Sum:-",rdd.sum())

# data=[("a",1),("b",2),("c",3)]=>op is same beacuse it do sum of matched key
# data=[("a",10),("b",20),("a",5),("b",10)]
# # It give the Reduced:  [('b', 30), ('a', 15)] it return the sum
# pairRDD=sc.parallelize(data)
#
# print("Original: ",pairRDD.collect())
#
# sumByKEy=pairRDD.reduceByKey(lambda  x,y:x+y)
# print("Reduced: ",sumByKEy.collect())

# --------------------------------------------------------------------------
# How to read external file
stopwords = ["is", "a", "the", "and", "of"]
b_stop = spark.sparkContext.broadcast(stopwords)

rdd = spark.sparkContext.textFile("../data/article.txt")
words = rdd.flatMap(lambda x: x.lower().split())
filtered = words.filter(lambda w: w not in b_stop.value)
pairs = filtered.map(lambda w: (w, 1))
wordCount = pairs.reduceByKey(lambda a, b: a + b)

# wordCount.saveAsTextFile("../output/wordcount")
print(wordCount.collect())