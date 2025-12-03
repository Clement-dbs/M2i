

# Tâches 
# 1. Charger le fichier avec Pandas 
# 2. Ajouter une colonne montant_total (quantite × prix_unitaire) 
# 3. Calculer le total des ventes par vendeur 
# 4. Calculer le total des ventes par produit 
# 5. Identifier le top 3 des ventes (montant le plus élevé) 
# 6. Sauvegarder les résultats dans ventes_analysees.csv

import pandas as pd

df = pd.read_csv('data.csv')
print(df)
df["montant_total"] = df['quantite'] * df['prix_unitaire']


total_par_vendeur = df.groupby('vendeur')['quantite'].sum()
print(f"Total des ventes par vendeur : {total_par_vendeur}")

total_vente_produit = df.groupby('produit')['quantite'].sum()
print(f"Total des ventes par produit : {total_vente_produit}")

top_3_vente = df.groupby('produit')['montant_total'].sum().sort_values(ascending=False).head(3)
print(f"Top 3 des ventes : {top_3_vente}")


df.to_csv("ventes_analysees.csv", index=False)

df_result = pd.DataFrame()
df_result['Total des ventes par vendeur'] = total_par_vendeur
df_result['Total des ventes par produit'] = total_vente_produit
df_result['Top 3 des ventes'] = top_3_vente


df_result.to_csv("ventes_analysees.csv", index=False)
