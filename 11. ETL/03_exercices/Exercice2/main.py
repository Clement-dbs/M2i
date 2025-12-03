import pandas as pd
import openpyxl

df = pd.read_excel('ventes_janvier.xlsx')

df = df.drop_duplicates() # Supprimer les doublons

df = df.fillna('Non spécifié') # Remplir les valeurs manquantes de `region` par "Non spécifié"
df['date'] = pd.to_datetime(df['date']) # Convertir `date` en datetime
df['montant_total'] = df['quantite'] * df['prix_unitaire'] # Créer `montant_total` = quantite × prix_unitaire
df['jour'] = df['date'].dt.day_name('french') # Extraire le `jour` (nom du jour de la semaine)
df['jour_semaine'] = df['date'].dt.day_of_week # Extraire le `jour` (numéro du jour de la semaine))


df2 = df.groupby('region')['montant_total'].sum().sort_values(ascending=False).reset_index() # Total des ventes par région
df3 = df.groupby('produit')['quantite'].sum().sort_values(ascending=False).reset_index() # Produit le plus vendu (en quantité)
jour_avec_le_plus_de_ventes = df.groupby('jour')['montant_total'].sum().sort_values(ascending=False).reset_index() # Jour de la semaine avec le plus de ventes


print(df)

with pd.ExcelWriter('rapport.xlsx') as writer:
    df.to_excel(writer, sheet_name='Données', index=False)
    df2.to_excel(writer, sheet_name='Par région', index=False)
    df3.to_excel(writer, sheet_name='Par Produit', index=False)

