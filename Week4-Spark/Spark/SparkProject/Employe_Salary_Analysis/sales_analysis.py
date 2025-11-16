import os
import sys

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StringType,IntegerType,StructField
from unicodedata import category

os.environ["JAVA_HOME"] = "C:/Program Files/Java/jdk-21"
os.environ["SPARK_HOME"] = "C:/Users/Shree/OneDrive/Desktop/Training Folder/Week4-Spark/Spark/SparkProject/.venv/Lib/site-packages/pyspark"
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession.builder \
    .appName("CreateRDDExample") \
    .getOrCreate()
sc=spark.sparkContext

sales_data = [
    ("2025-01-01", "TV", "Electronics", 3, 45000),
    ("2025-01-02", "Fridge", "Electronics", 2, 52000),
    ("2025-01-03", "Shoes", "Fashion", 10, 30000),
    ("2025-01-03", "Watch", "Fashion", 5, 25000),
    ("2025-01-04", "Mobile", "Electronics", 7, 70000)
]
columns = ["Date", "Product", "Category", "Quantity", "Revenue"]

sales_df = spark.createDataFrame(sales_data, columns)
sales_df.createOrReplaceTempView("sales")

# Daily total:
daily_revenue_df = spark.sql("""
SELECT Date, SUM(Revenue) AS Total_Revenue
FROM sales GROUP BY Date ORDER BY Date
""").show()

# Category share
category_revenue_df = spark.sql("""
SELECT Category, SUM(Revenue) AS Revenue,
       ROUND(SUM(Revenue) * 100 / (SELECT SUM(Revenue) FROM sales), 2) AS Percentage
FROM sales GROUP BY Category
""").show()

# 3. Top product
top_product_df = spark.sql("""
SELECT Product, SUM(Revenue) AS Total
FROM sales
GROUP BY Product
ORDER BY Total DESC
LIMIT 1
""").show()
