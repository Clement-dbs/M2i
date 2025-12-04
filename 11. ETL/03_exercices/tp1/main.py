import pandas as pd
import openpyxl

df1 = pd.read_csv('magasin_A.csv')
df2 = pd.read_csv('magasin_B.csv')
df3 = pd.read_csv('magasin_C.csv')

# Ajouter une colonne `magasin` 
df1['magasin'] = 'A'
df2['magasin'] = 'B'
df3['magasin'] = 'C'

# Concaténer tous les DataFrames
df_global = pd.concat([df1, df2, df3], ignore_index=True)

# Nettoyer (doublons, valeurs manquantes)
df_global.drop_duplicates(inplace=True)
df_global.fillna('valeur manquante', inplace=True)

# Calculer `montant_total`
df_global['montant_total'] = df_global['quantite'] * df_global['prix_unitaire']


print(f'Montant total des ventes: \n {df_global}')
print(df_global)


# Totaux par magasin
df_par_magasin = df_global.groupby('magasin')['montant_total'].sum()
# Totaux par vendeurs
df_par_vendeur = df_global.groupby('vendeur')['montant_total'].sum()
# Top produits
df_top_produits = df_global.groupby('produit')['quantite'].sum().sort_values(ascending=False)

# - Feuille "Consolidé" : Toutes les données
# - Feuille "Par magasin" : Totaux par magasin
# - Feuille "Par vendeur" : Performance des vendeurs
# - Feuille "Top produits" : 10 produits les plus vendus
with pd.ExcelWriter('rapport_ventes.xlsx') as writer:
    df_global.to_excel(writer, sheet_name='Consolidé', index=False)
    df_par_magasin.to_excel(writer, sheet_name='Par magasin')
    df_par_vendeur.to_excel(writer, sheet_name='Par vendeur')
    df_top_produits.to_excel(writer, sheet_name='Top produits')