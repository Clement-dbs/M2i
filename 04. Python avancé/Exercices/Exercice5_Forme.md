# Forme (abstraction)

**Exercice :** Créez une classe abstraite `Forme` représentant une forme géométrique. Elle aura un attribut `nom` qui stockera le nom de la forme. Elle possédera également les méthodes suivantes : 

- `calculer_aire()` (abstraite) qui calcul l'aire de la forme. 
- `calculer_perimetre()` (abstraite) qui calcul son périmètre. 
- `infos()` qui donnera les informations de la forme. 

Vous créerai ensuite 2 classe qui héritent de Forme : 

- `Rectangle`, avec les attributs longueur et largeur
- `Cercle`, avec l'attribut rayon 

Puis vous implémenterai les méthodes en conséquences. 

Enfin créez un objet `rectangle` et un objet `cercle` à l'aide de leur constructeur puis affichez leur infos (nom, propriété, perimetre, aire). 