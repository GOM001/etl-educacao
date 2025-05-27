import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Inicializa uma sessão Spark com suporte ao S3
spark = SparkSession.builder \
    .appName("ETL Educacao") \
    .config("spark.driver.memory", "2g") \
    .config("spark.hadoop.fs.s3a.aws.credentials.provider", "com.amazonaws.auth.DefaultAWSCredentialsProviderChain") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .getOrCreate()

# Caminho do arquivo no S3
raw_data_path = "s3a://etl-educacao/raw/microdados_ed_basica_2024.csv"

# Lê o dataset
raw_df = spark.read.option("header", True).csv(raw_data_path)

# Exemplo de transformação: filtrar registros com valores válidos em uma coluna importante
clean_df = raw_df.filter(col("NU_ANO_CENSO").isNotNull())

# Exemplo de seleção de colunas relevantes
selected_df = clean_df.select(
    "NU_ANO_CENSO",
    "CO_MUNICIPIO",
    "NO_MUNICIPIO",
    "TP_DEPENDENCIA",
    "QT_MATRICULAS"
)

# Conversão de tipos, se necessário
transformed_df = selected_df.withColumn("QT_MATRICULAS", col("QT_MATRICULAS").cast("int"))

# Exibe uma amostra
transformed_df.show(10)

# Salva em formato Parquet no S3
output_path = "s3a://etl-educacao/processed/educacao_transformado.parquet"
transformed_df.write.mode("overwrite").parquet(output_path)

print("ETL concluído com sucesso!")

# Encerra a sessão Spark
spark.stop()