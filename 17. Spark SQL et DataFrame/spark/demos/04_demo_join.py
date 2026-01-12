from pyspark.sql import SparkSession, Row
from pyspark.sql.types import StructType, StructField, StringType


spark = SparkSession.builder.master("local").appName("demo-join").getOrCreate()

livresSchema = StructType([
    StructField("livre_id", StringType(), nullable=False),
    StructField("titre", StringType(), nullable=False),
    StructField("auteur_id", StringType(), nullable=True),
])

livresData = [
    Row("L1", "Livre 1", "A1"),
    Row("L2", "Livre 2", "A2"),
    Row("L3", "Livre 3", "A1"),
    Row("L4", "Livre 4", "A3"),
    Row("L5", "Livre 5", None)
]

livresRdd = spark.sparkContext.parallelize(livresData)
dfLivres = spark.createDataFrame(livresRdd, livresSchema)

# Auteur

auteurSchema = StructType([
    StructField("auteur_id", StringType(), nullable=False),
    StructField("nom", StringType(), nullable=False),
])

auteurData = [
    Row("A1", "Toto"),
    Row("A2", "Tata"),
    Row("A3", "Titi"),
    Row("A4", "Tutu")
]

auteurRdd = spark.sparkContext.parallelize(auteurData)
dfauteur = spark.createDataFrame(auteurRdd, auteurSchema)


dfLivres.show()
dfauteur.show()

print("INNER JOIN :")

innerDf = dfLivres.join(dfauteur, ["auteur_id"], "inner")
innerDf.show()

leftJoin = dfLivres.join(dfauteur, dfLivres["auteur_id"] == dfauteur["auteur_id"])
leftJoin.show()

antiDf = dfLivres.join(dfauteur,["auteur_id"],"anti")
antiDf.show()