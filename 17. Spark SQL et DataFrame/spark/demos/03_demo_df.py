from pyspark.sql import SparkSession
from pyspark.sql.functions import col, desc, lit, min, max, avg
from datetime import datetime

# Créer la session Spark
spark = SparkSession.builder.master("local").appName("demo-df").getOrCreate()

df = spark.read \
          .option("header", "true") \
          .option("inferSchema", "true") \
          .option("sep", ",") \
          .csv("./data/friends-with-header.csv")
          
df.show()

# SELECT
df.select("name").show()
df.select("name", "age").show()

# FILTER
df.filter((col("age") > 35) & (col("friendsNumber") > 300)).show()

listePrenoms = ["Weyoun", "Ben", "Will"]
df.filter(col("name").isin(listePrenoms)).sort("name").show()

# Ajouter une colonne
dfWithBirthYear = df.withColumn("BirthYear", lit(datetime.now().year) - col("age"))
dfWithBirthYear.show()

# Agrégations
df.select(
  min("age").alias("age_min"),
  max("age").alias("age_maximum"),
  avg("age").alias("age_avg")
).show()

dfAge = df.select(
  min("age").alias("age_min"),
  max("age").alias("age_maximum"),
  avg("age").alias("age_avg")
).collect()

print(dfAge)

# Enregistrement comme vue temporaire pour utiliser SQL
df.createOrReplaceTempView("personnes")
spark.sql("SELECT * FROM personnes").show()