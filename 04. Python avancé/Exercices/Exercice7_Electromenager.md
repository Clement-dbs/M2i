# Exercice 7 - Duck typing - Electroménager

## Objectifs

Utiliser des méthodes qui sont communs entre plusieurs classes sans parentées.

## Taches 

1. Créer les classes suivantes :
    - `Mixeur` : possède la méthode `allumer()`, `mixer()`, `broyer()`
    - `Broyeur` : possède la méthode `allumer()`, `broyer()`
    - `Cookeo` : possède la méthode `allumer()`, `mixer()`, `cuire()`, `rechauffer()`
    - `Four` : possède la méthode `allumer()`, `cuire()`, `rechauffer()`

2. La classe `Cookeo` héritera de la classe `Mixeur`.

3. Créer une liste possédant au moins un objet de chaucune des classes du (1)

4. Dans une boucle: 
    - utilisez la méthode allumer() de chacun des éléments.
    - utilisez la méthode cuire() et mixer() des classes ayant cette méthodes.