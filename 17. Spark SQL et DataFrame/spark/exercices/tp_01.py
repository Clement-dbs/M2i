from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql.functions import col, desc, lit, min, max, avg, count, round, udf
from datetime import datetime


spark = SparkSession.builder.master("local").appName("tp_01").getOrCreate()

df = spark.read \
          .option("header", "true") \
          .option("inferSchema", "true") \
          .option("sep", ",") \
          .csv("./spark/data/StudentsPerformance.csv")

# Schema
studentsSchema = StructType([
    StructField("gender", StringType(), nullable=False),
    StructField("race/ethnicity", StringType(), nullable=False),
    StructField("parental level of education", StringType(), nullable=True),
    StructField("lunch", StringType(), nullable=False),
    StructField("test preparation course", StringType(), nullable=False),
    StructField("math score", StringType(), nullable=True),
    StructField("reading score", StringType(), nullable=False),
    StructField("writing score", StringType(), nullable=False)
])

### Exercice 1.1 - Exploration

# # TODO 1: Afficher le schéma
# print(studentsSchema)

# # TODO 2: Compter le nombre d'étudiants
# count_student = df.count()
# print(f"Nombre d'étudiants : {count_student}")

# # TODO 3: Afficher les 10 premières lignes
# df.show(10)

# # TODO 4: Afficher les statistiques descriptives (describe)
# df.describe().show()

# ### Exercice 1.2 - Sélections et Filtres

# # TODO 1: Sélectionner uniquement gender et les 3 scores

# df.select(
#     ("gender"),
#     ("math score"),
#     ("reading score"),
#     ("writing score")
# )

# # TODO 2: Filtrer les étudiants qui ont > 90 en maths

# students = df.filter(col("math score") > 90)
# students.show()

# # TODO 3: Filtrer les étudiants avec lunch = "free/reduced"

# students = df.filter(col("lunch") == "free/reduced")
# students.show()

# # TODO 4: Compter combien d'étudiants ont complété le prep course

# students = df.filter(col("test preparation course") == "completed").count()
# print(f"Nombre d'étudiants qui ont complété le 'prep course' {students}")

# # TODO 5: Trouver les 10 meilleurs scores en lecture

# df.orderBy(desc("reading score")).show(10)

### Exercice 1.3 - Agrégations
# TODO 1: Calculer la moyenne de chaque matière

# df.select(
#     avg("math score"),
#     avg("reading score"),
#     avg("writing score")
# ).show()

# # TODO 2: Compter le nombre d'étudiants par genre

# df.groupBy("gender") \
# .agg(
#     count("gender"),
# ).show()

# # TODO 3: Calculer la moyenne des scores par genre

# df.groupBy("gender") \
#   .agg(
#       avg("math score"),
#       avg("reading score"),
#       avg("writing score")
#   ).show()

# # TODO 4: Trouver le score max et min en maths
# df.select(
#     min("math score"),
#     max("math score")
# ).show()

# # TODO 5: Calculer la moyenne par groupe ethnique (race/ethnicity)

# df.groupBy("race/ethnicity") \
#   .agg(
#       avg("math score"),
#       avg("reading score"),
#       avg("writing score")
#   ).show()


## Niveau 2 : Jointures

# grades_ref = spark.createDataFrame([
#     ("A", 90, 100),
#     ("B", 80, 89),
#     ("C", 70, 79),
#     ("D", 60, 69),
#     ("F", 0, 59)
# ], ["grade", "min_score", "max_score"])

# grades_ref.show()

# departments = spark.createDataFrame([
#     ("group A", "Sciences"),
#     ("group B", "Arts"),
#     ("group C", "Commerce"),
#     ("group D", "Ingénierie"),
#     ("group E", "Médecine")
# ], ["ethnicity", "department"])

# departments.show()

# # TODO 1: Joindre students avec departments
# # Sur la colonne race/ethnicity = ethnicity
# # Afficher : gender, ethnicity, department, math score

# innerDf = df.join(
#     departments,
#     df["race/ethnicity"] == departments["ethnicity"],
#     "inner"
# )

# innerDf.select(
#     col("gender"),
#     col("ethnicity"),
#     col("department"),
#     col("math score")
# ).show()

# # TODO 2: Compter le nombre d'étudiants par département

# innerDf.groupBy("department") \
#     .agg(
#         count("department")
#     ).show()

# # TODO 3: Calculer la moyenne des scores par département

# innerDf.groupBy("department") \
#   .agg(
#       avg("math score"),
#       avg("reading score"),
#       avg("writing score")
#   ).show()


### Exercice 2.2 - Transformation et jointure
# from pyspark.sql.functions import monotonically_increasing_id
# students_with_id = df.withColumn("student_id", monotonically_increasing_id())

# students_with_avg = students_with_id.withColumn(
#     "score_moyen",
#     (col("math score") + col("reading score") + col("writing score")) / 3
# )

# students = students_with_avg.select("student_id", "score_moyen")

# students.show(10)


# students_with_grade = students.join(
#     grades_ref,
#     students.score_moyen.between(grades_ref.min_score, grades_ref.max_score),
#     "inner"
# )

# students_with_grade.show(10)


## Exercice 2.3 - Analyse croisée

# students_departements = df.join(
#     departments,
#     df["race/ethnicity"] == departments["ethnicity"],
#     "inner"
# )

# # TODO 1: Joindre students avec departments
# # Calculer la moyenne par département ET par genre
# students_departements.groupBy("department", "gender").agg(
#         avg("math score"),
#         avg("reading score"),
#         avg("writing score")
#     ).orderBy("department", "gender").show()

# # TODO 2: Identifier le département avec les meilleurs résultats
# students_departements.orderBy(col("math score").desc(), col("reading score").desc(), col("writing score").desc()).show

# # TODO 3: Analyser l'impact du prep course par département
# # Comparer moyenne avec/sans prep course pour chaque département

# prep_analysis = students_departements.groupBy("department", "test preparation course") \
#     .agg(
#         round(avg("math score"),2).alias("avg_math"),
#         round(avg("reading score"),2).alias("avg_reading"),
#         round(avg("writing score"),2).alias("avg_writing")
#     ) \
#     .orderBy("department", "test preparation course")

# prep_analysis.show()

## Niveau 3 : UDF

### Exercice 3.1 - UDF simple

# TODO 1: Créer une UDF pour convertir un score en grade
# A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: 0-59

# Définir l'udf
def convert_score_to_grade(score):
    if score <= 59:
        return "F"
    elif score <= 69:
        return "D"
    elif score <= 79:
        return "C"
    elif score <= 89:
        return "B"
    else:
        return "A"
    

score = udf(convert_score_to_grade, StringType())

# TODO 2: Appliquer cette UDF aux 3 matières
# Créer 3 nouvelles colonnes : math_grade, reading_grade, writing_grade
df_avg = df.withColumn(
    "average_score",
    (col("math score") + col("writing score") + col("reading score")) / 3
)

df_with_udf = df_avg.withColumn("grade", score(col("average_score")))

df_with_udf.show()

# TODO 3: Compter la distribution des grades en maths
df_with_udf.groupBy("math score", "grade") \
.agg(


    count("grade"),
).show()

### Exercice 3.2 - UDF avec plusieurs paramètres
# TODO 1: Créer une UDF pour calculer la moyenne pondérée
# Math: 40%, Reading: 30%, Writing: 30%

df_avg = df.withColumn(
    "average_score",
    col("math score") * 0.40 +
    col("reading score") * 0.30 +
    col("writing score") * 0.30
)

df_avg.show()

df_with_udf = df_avg.withColumn("grade", score(col("average_score")))

df_with_udf.show()