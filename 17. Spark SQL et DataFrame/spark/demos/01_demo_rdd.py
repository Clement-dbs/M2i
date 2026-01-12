from pyspark.sql import SparkSession

# Créer la session Spark
spark = SparkSession.builder.master("local").appName("demo-rdd").getOrCreate()

# Récupérer le SparkContext
sc = spark.sparkContext

# Création d'un RDD
firstRDD = sc.parallelize([1, 2, 3])

# Transformer le premier RDD
secondRDD = firstRDD.map(lambda e: e * 5)

# Collecter les résultats
result = secondRDD.collect()

print(result)