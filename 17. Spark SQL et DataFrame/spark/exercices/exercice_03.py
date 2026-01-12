from pyspark.sql import SparkSession, Row
builder: SparkSession.Builder = SparkSession.builder
from pyspark.sql.functions import col, desc, lit, min, max, avg, count

# Créer la session Spark
spark = SparkSession.builder.master("local").appName("demo-df").getOrCreate()

df_movies = spark.read \
          .option("header", "true") \
          .option("inferSchema", "true") \
          .option("sep", ",") \
          .csv("./spark/data/movie.csv")

df_ratings = spark.read \
          .option("header", "true") \
          .option("inferSchema", "true") \
          .option("sep", ",") \
          .csv("./spark/data/rating.csv")

print("INNER JOIN :")

innerDf = df_movies.join(df_ratings, ["movieId"], "inner")
innerDf.show()

# # Compter le nombre de notes : 
# rating_number = innerDf.count()


# print(f"Nombre de notes : {rating_number}")

# # Rating + Titre

# innerDf.select("title", "rating").show()

# # Moyenne
# innerDf.groupBy("title").agg(
#         count("rating").alias("nombre_de_notes"),
#         avg("rating").alias("note_moyenne")
#     ).orderBy(desc("nombre_de_notes")).show()

# 4. 
# a) films qui ont au moins une note
leftSemiDf = df_movies.join(
    df_ratings,
    df_movies["movieId"] == df_ratings["movieId"],
    "left_semi"
)

# b) films sans aucune note
leftAntiDf = df_movies.join(
    df_ratings,
    df_movies["movieId"] == df_ratings["movieId"],
    "left_anti"
)

# c) liste complète des films avec stats si disponibles
leftOuterDf = df_movies.join(
    df_ratings,
    df_movies["movieId"] == df_ratings["movieId"],
    "left_outer"
)

# d) diagnostic des clés présentes uniquement dans l’un des deux

fullOuterDf = df_movies.join(
    df_ratings,
    df_movies["movieId"] == df_ratings["movieId"],
    "full_outer"
)

print("LEFT SEMI")
leftSemiDf.show()

print("LEFT ANTI")
leftAntiDf.show()

print("LEFT OUTER")
leftOuterDf.show()

print("FULL OUTER")
fullOuterDf.show()

# 5.

innerDf.groupBy("title").agg(
        max("rating").alias("note_max"),
        avg("rating").alias("note_moyenne")
    ).orderBy(desc("nombre_de_notes")).show()