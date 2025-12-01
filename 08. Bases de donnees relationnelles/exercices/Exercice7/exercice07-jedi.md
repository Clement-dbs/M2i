# Exercice 07 - Jedi

L'école des Jedi de Tatooine souhaite gérer les résultats des apprentis lors du passage des obstacles du parcours de la force (sorte de parcours du combattant). Voici les détails :

1. **Contexte Général :**

   - Les futurs Jedi passent plusieurs fois ce rituel au cours de leur carrière. 
   - Chaque fois qu’un padawan passe un obstacle, un instructeur lui attribue une note (note instructeur).
   - Le parcours comporte 20 obstacles, chaque élève reçoit donc 20 notes (si l’élève ne passe pas l’obstacle, la note 0 lui est attribuée).

2. **Niveaux de Difficulté et Bonus :**

   - Chaque obstacle a un niveau de difficulté (facile, moyen, difficile, etc.).
   - Un bonus de points est attribué en fonction du niveau de difficulté (par exemple, un bonus de 2 points pour les niveaux difficiles).

3. **Calcul de la Note Finale :**

   - La note finale pour le passage d’un obstacle est égale à :  
     **Note attribuée par l’instructeur + Bonus de difficulté**
   - Une note minimale à obtenir est définie pour chaque obstacle, indiquant le niveau minimum à atteindre. Cela permet de déterminer sur quels obstacles un élève doit axer en priorité son entraînement.

4. **Exemple Concret :**
   - **Obstacle :** Fosse
   - **Niveau de difficulté :** Difficile (bonus attribué : 2 points)
   - **Note minimale à atteindre :** 10
   - **Note de l'instructeur :** 6
   - **Note finale :** 6 + 2 = 8
   - **Conclusion :** Le niveau sur cet obstacle est jugé insuffisant, et l’élève doit parfaire son entraînement.

Les responsables souhaitent:

- Obtenir la liste de tous les obstacles ainsi que leur niveau de difficulté.
- Obtenir la liste de toutes les notes attribuées sur chaque obstacle.
- Avoir un récapitulatif des notes obtenues par un padawan donné pour retracer sa progression.
- Connaître le temps total et les temps intermédiaires mis par un padawan pour effectuer un parcours complet.

Réaliser le MCD pour permettre une gestion efficace des performances et de l’entraînement des apprentis Jedi.
