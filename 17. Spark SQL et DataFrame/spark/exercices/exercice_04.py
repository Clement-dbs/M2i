
from pyspark.sql import SparkSession, Row
builder: SparkSession.Builder = SparkSession.builder
from pyspark.sql.types import StringType, DoubleType
from pyspark.sql.functions import udf, col

# Créer la session Spark
spark = SparkSession.builder.master("local").appName("ex04").getOrCreate()

ventesData = [
  ("CMD001", "Alice Martin", "2024-03-15", "Électronique", 1299.99, 1, "Premium", "alice.martin@email.com"),
  ("CMD002", "Bob Durand", "2024-03-16", "Vêtements", 89.50, 3, "Standard", "bob.durand@email.com"),
  ("CMD003", "Claire Dubois", "2024-03-17", "Maison", 45.00, 2, "Premium", "claire.dubois@email.com"),
  ("CMD004", "David Moreau", "2024-03-18", "Sport", 199.99, 1, "Standard", "david.moreau@email.com"),
  ("CMD005", "Emma Petit", "2024-03-19", "Électronique", 799.00, 2, "VIP", "emma.petit@email.com"),
  ("CMD006", "Frank Lambert", "2024-03-20", "Livres", 29.99, 5, "Standard", "frank.lambert@email.com"),
  ("CMD007", "Grace Bernard", "2024-03-21", "Beauté", 156.75, 1, "Premium", "grace.bernard@email.com"),
  ("CMD008", "Henri Rousseau", "2024-03-22", "Électronique", 2199.00, 1, "VIP", "henri.rousseau@email.com")
]

df = spark.createDataFrame(ventesData, ["id_commande", "nom_client", "date_commande", "categorie", "prix_unitaire", "quantite", "statut_client", "email"])

df.show()

# 1
def classifier_vente(prix_unitaire, quantite):
    if (prix_unitaire*quantite) < 50:
        return "Vente faible"
    elif (prix_unitaire*quantite) < 200:
        return "Vente moyenne"
    elif (prix_unitaire*quantite) < 1000:
        return "Vente élevée"
    else:
        return "Ventre premium"


classierVente = udf(classifier_vente, StringType())


df_with_udf = df.withColumn("classier_vente", classierVente(col("prix_unitaire"), col("quantite")))

df_with_udf.show()


# 2
def calculer_montant_total(prix_unitaire, quantite, statut_client):
    if statut_client == "Standard":
        return prix_unitaire*quantite
    elif statut_client == "Premium":
        return (prix_unitaire*quantite) * 0.95
    else:
        return (prix_unitaire*quantite) * 0.9
    

montant_total = udf(calculer_montant_total, DoubleType())

df_with_udf = df.withColumn("montant_total", montant_total(col("prix_unitaire"), col("quantite"), col("statut_client")))

df_with_udf.show()


# 3

def calculer_score_fidelite(statut_client, prix_unitaire, quantite, categorie):
    score = 0
    if statut_client == "Standard":
        score = score + 1
    if statut_client == "Premium":
        score = score + 2
    if statut_client == "VIP":
        score = score + 3

    if categorie == "Électronique":
        score = score + 2
    if categorie == "Sport":
        score = score + 1
    
    bonus_par_tranche = (prix_unitaire*quantite) // 100 

    return score + bonus_par_tranche

score_fidelite = udf(calculer_score_fidelite, DoubleType())

df_with_udf = df.withColumn("score_fidelite", score_fidelite(col("statut_client"), col("prix_unitaire"), col("quantite" \
""), col("categorie")))

df_with_udf.show()
