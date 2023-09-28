from pyspark.sql import SparkSession

my_spark = SparkSession \
    .builder \
    .appName("app") \
    .config("spark.mongodb.read.connection.uri", "mongodb://127.0.0.1/gpus.tori") \
    .config("spark.mongodb.write.connection.uri", "mongodb://127.0.0.1/gpus.tori") \
    .config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.12:10.2.0") \
    .getOrCreate()

my_spark.sparkContext.setLogLevel("ERROR")
df = my_spark.read.format("mongodb").load()
df.show()