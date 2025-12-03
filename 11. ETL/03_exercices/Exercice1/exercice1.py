# fichier exercice1.py ou main.py si plusieurs modules
import pandas as pd

# 1. Charger le fichier avec Pandas
df = pd.read_csv("ventes.csv")

# 2. Ajouter une colonne `montant_total` (quantite × prix_unitaire)
df['montant_total'] = df['quantite'] * df['prix_unitaire'] 

# 3. Calculer le total des ventes par vendeur
total_vendeur = df.groupby('vendeur')['montant_total'].sum()
print(total_vendeur)

# 4. Calculer le total des ventes par produit
total_produit = df.groupby('produit')['montant_total'].sum()
print(total_produit)

# 5. Identifier le top 3 des ventes (montant le plus élevé)
top3 = df.sort_values('montant_total',ascending=False).head(3)

top3_v2 = df.sort_values('montant_total',ascending=False).head(3)[['date','produit','vendeur','montant_total']]


top3_v3 = df.nlargest(3,'montant_total')[['date','produit','vendeur','montant_total']]

print(top3)
print(top3_v2)
print(top3_v3)
# 6. Sauvegarder les résultats dans `ventes_analysees.csv`
df.to_csv('ventes_analysees.csv',index=False)