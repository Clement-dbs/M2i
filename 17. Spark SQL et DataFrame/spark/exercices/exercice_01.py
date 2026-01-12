from pyspark.sql import SparkSession

# Créer la session Spark
spark = SparkSession.builder.master("local").appName("exercice01").getOrCreate()

# Récupérer le SparkContext
sc = spark.sparkContext

rddAchats = sc.textFile("./data/achats_clients.csv")

firstline = rddAchats.first()

rdd = rddAchats.filter(lambda ligne: ligne != firstline)


def extract_client_montant(line):
  fields = line.split(",")
  return fields[0], float(fields[2])

rddClients = rdd.map(extract_client_montant)

montantClients = rddClients.reduceByKey(lambda a, b: a + b)
result = montantClients.collect()

for idClient, montant in result:
  print(f"Client n°{idClient} | montant : {montant} €")