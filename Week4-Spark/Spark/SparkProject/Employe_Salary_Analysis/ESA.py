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



data=[
     (101,"Raman","HR",35000),
     (102,"Raj","It",58000),
     (103,"Sunil","It",52000),
     (104,"Avdhut","Network",40000),
     (105,"Dipak","Finace",3500)
]

column=["id","ename","dept","salary"]

emp_df=spark.createDataFrame(data,column)
emp_df.createOrReplaceTempView("employee")

# aggreation
agg=spark.sql("""
    select dept as department,
           avg(salary) as avg_salary,
           sum(salary) as total_salary
    from employee group by dept
""").show()    # these show() does not store the value in dataframe that why we can create  output file

# Employye above avg salary
high_salar=spark.sql("""
    select e.ename,e.dept,e.salary
    from employee e
    join(
     select dept,AVG(salary) as avg_salary
     from employee
     group by dept
    ) d
    on e.dept=d.dept
    where e.salary>d.avg_salary
""")

high_salar.show()
# 3. Save results
high_salar.write.mode("overwrite").option("header","true").csv("..data/high_earners")










