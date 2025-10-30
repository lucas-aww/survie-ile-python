# Jeu de survie sur une île

## Objectif
Survivre 12 jours sur une île déserte en gérant vos ressources vitales.

## Jauges vitales
- Faim : 0 = rassasié, 100 = affamé → game over
- Soif : 0 = hydraté, 100 = déshydraté → game over
- Énergie : 0 = épuisé → game over
- PV : points de vie

## Actions possibles
- `aller` : se déplacer entre zones
- `inventaire` : afficher l’inventaire
- `utiliser` : utiliser un objet (poisson, fruit, eau)
- `chasser` : obtenir de la nourriture
- `pecher` : obtenir de la nourriture
- `se_reposer` : regagner de l’énergie (si faim et soif < 50)
- `explorer` : déclenche événements aléatoires (pluie, rencontre animale, découverte de fruits)
- `sauvegarder` : sauvegarder la partie dans un fichier JSON
- `charger` : charger la partie depuis le fichier JSON
- `quitter` : quitter le jeu

## Lancer le jeu
```bash
python main.py
