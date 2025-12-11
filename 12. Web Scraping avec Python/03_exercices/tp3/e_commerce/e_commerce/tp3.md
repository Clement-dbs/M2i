## Projet - E-commerce Scraper


**Objectif** : Créer un scraper e-commerce complet

**Site** : http://books.toscrape.com

**Fonctionnalités requises**

1. **Spider multi-niveaux**
   - Page d'accueil → Catégories
   - Catégories → Pages de livres
   - Pages de livres → Détails

2. **Données à extraire**
   - Informations livre (titre, prix, rating, description)
   - Catégorie
   - Nombre d'avis
   - Image du livre

3. **Traitement**
   - Pipeline de nettoyage des prix
   - Pipeline de dédoublonnage
   - Pipeline de sauvegarde en base SQLite (bonus)

4. **Export**
   - Fichier Excel avec 2 feuilles : "Livres" et "Catégories"
   - JSON pour archivage

5. **Configuration**
   - Rate limiting approprié
   - User-Agent custom