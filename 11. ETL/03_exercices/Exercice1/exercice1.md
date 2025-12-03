## Exercice 1 - CSV avec Pandas

**Objectif** : Manipuler un fichier CSV de ventes

**Données** : Créer un fichier `ventes.csv`
```csv
date,produit,quantite,prix_unitaire,vendeur
2024-01-15,Laptop,2,899.99,Alice
2024-01-15,Souris,5,29.99,Bob
2024-01-16,Clavier,3,79.99,Alice
2024-01-16,Laptop,1,899.99,Charlie
2024-01-17,Souris,10,29.99,Alice
```

**Tâches**
1. Charger le fichier avec Pandas
2. Ajouter une colonne `montant_total` (quantite × prix_unitaire)
3. Calculer le total des ventes par vendeur
4. Calculer le total des ventes par produit
5. Identifier le top 3 des ventes (montant le plus élevé)
6. Sauvegarder les résultats dans `ventes_analysees.csv`