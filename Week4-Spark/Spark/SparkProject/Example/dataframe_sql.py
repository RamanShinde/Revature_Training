import os
import sys

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StringType,IntegerType,StructField

os.environ["JAVA_HOME"] = "C:/Program Files/Java/jdk-21"
os.environ["SPARK_HOME"] = "C:/Users/Shree/OneDrive/Desktop/Training Folder/Week4-Spark/Spark/SparkProject/.venv/Lib/site-packages/pyspark"
os.environ["HADOOP_HOME"]="C:/Hadoop"
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession.builder \
    .appName("CreateRDDExample") \
    .getOrCreate()
sc=spark.sparkContext

schema=StructType([
    StructField("name",StringType(),True),
    StructField("age",IntegerType(),True)
])

# df=spark.read.json(path="../data/file.json",schema=schema)
# df.cleaned=df.filter("name is not null and age is not null")
# df.createOrReplaceTempView("people")
# df.cache()
#
# spark.sql("select name from people where age>20")
# df.show()
# df.printSchema()

# How to create parquet
data=[("alice",25),("Bob",30),("Charlie",35)]
columns=["name","age"]
df=spark.createDataFrame(data, columns)
df.write.mode("Overwrite").parquet("../data/file2.parquet")
df.show()
