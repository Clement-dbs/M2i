from pyspark.sql import SparkSession
from pyspark.sql.functions import col, desc, lit, min, max, avg
from datetime import datetime

# Créer la session Spark
spark = SparkSession.builder.master("local").appName("demo-df").getOrCreate()

df = spark.read \
          .option("header", "true") \
          .option("inferSchema", "true") \
          .option("sep", ",") \
          .csv("./spark/data/housing.csv")
          
df.show()

df.select(
    min("median_house_value").alias("min_value"),
    max("median_house_value").alias("max_value"),
    avg("median_house_value").alias("avg_value")
)

df.select(
    min("housing_median_age").alias("min_value"),
    max("housing_median_age").alias("max_value"),
    avg("housing_median_age").alias("avg_value")
)

count = df.filter(col("population") > 5000).count()

print(count)

df.groupBy("ocean_proximity") \
.agg(
    avg("median_house_value").alias("prix_moyen"),
    avg("median_income").alias("revenu_moyen"),
    avg("housing_median_age").alias("age_moyen"),
    avg("population").alias("population_moyen"),
).orderBy(col("prix_moyen")).show()
