from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("SparkTesteMinimo") \
    .master("local[1]") \
    .getOrCreate()

print("Spark iniciado com sucesso!")

df = spark.createDataFrame([(1, "João"), (2, "Maria")], ["id", "nome"])
df.show()