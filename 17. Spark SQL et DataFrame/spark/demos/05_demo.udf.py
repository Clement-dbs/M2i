from pyspark.sql import SparkSession, Row
builder: SparkSession.Builder = SparkSession.builder
from pyspark.sql.types import StringType, DoubleType, DataType
from pyspark.sql.functions import udf,col

# Créer la session Spark
spark = SparkSession.builder.master("local").appName("demo-df").getOrCreate()


data = [
    ("Toto", 25, "Ingérieur", 50000.0),
    ("Tata", 38, "Manager", 60000.0),
    ("Titi", 35, "Dev", 30000.0)
]

df = spark.createDataFrame(data,["nom","age","poste","salaire"])

# Définir l'udf
def categorie_age(age):
    if age < 30:
        return "Junior"
    elif age < 40:
        return "Experimenté"
    else:
        return "Senior"
    
def salaire_avec_bonus(salaire):
    return salaire * 1.1


categorieAge = udf(categorie_age, StringType())
salaireBonux = udf(salaire_avec_bonus, DoubleType())

df_with_udf = df.withColumn("categorie_age", categorieAge(col("age"))) \
                    .withColumn("salaire_bonus", salaire_avec_bonus(col("salaire")))

df_with_udf.show()