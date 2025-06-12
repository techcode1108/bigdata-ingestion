from pysprk.sql import SparkSession
from pyspark.sql import functions as F

class readData{

spark = SparkSession.builder.master("yarn").appName("readData").getOrCreate()
df1 = spark.read.format("orc").option("header",True).load("filePath")
df1.show()
}
