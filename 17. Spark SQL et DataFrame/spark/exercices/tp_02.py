from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql.functions import col, year, udf, count
from datetime import datetime


spark = SparkSession.builder.master("local").appName("tp_02").getOrCreate()

df = spark.read \
          .option("header", "true") \
          .option("inferSchema", "true") \
          .option("sep", ",") \
          .csv("./spark/data/Sample - Superstore.csv")

### Partie 1 : Chargement et exploration
df.printSchema()
df.show(20)
total_rows = df.count()
print(f"Total de lignes : {total_rows}")
df.select("Region").distinct().show()

### Partie 2 : Transformations simples

df = df.withColumn("Profit_Margin", col("Profit") / col("Sales"))
df = df.withColumn("Year", year(col("Order Date")))
df = df.withColumn("Total_Value", col("Sales") - col("Discount"))
df.show(10)

### Partie 3 : UDF - Catégorisation des ventes

def categorizeSale(sales):
    if sales < 100:
        return "Petite vente"
    elif sales < 500:
        return "Vente moyenne"
    else:
        return "Grosse vente"

categorize_sale = udf(categorizeSale, StringType())

df_with_udf = df.withColumn("categorie_de_vente", categorize_sale(col("Sales")))

df.show()

### Partie 4 : UDF - Niveau de remise

# def discountLevel(discount):
#      if discount < 100:
#         return "Petite vente"
#     elif discount < 500:
#         return "Vente moyenne"
#     else:
#         return "Grosse vente"




