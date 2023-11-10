# Bataille-navale
Own implementation of battleship game.

## Files and functions:
### boucle_de_jeu:
Module contenant les fonctions permetant de faire s'affonter un humain contre l'ordinateur ou deux bots entre eux.

  - main_loop_human_bot: Fonction principale qui permet à un humain de faire une partie de bataille contre un bot de la difficulté choisit.
    
  - bot_match: Fonction pour faire 2 algorithmes de combat.

  - bot_analyse: Fonction pour faire jouer un bot seul afin d'analyser le nombre de tir nécessaire pour couler tous les bateaux d'une carte aléatoire.


### execute:
Module contenant les fonctions permetant de faire s'affonter un humain contre l'ordinateur, deux bots entre eux ou pour tester l'efficacité d'un bot.

### graphics:
Ce module compte les fonctions graphiques utilisées pour tracer le plateau de jeu.

  - show_state_ancrage: Cette fonction est utilisée pour montrer les différentes cellules possibles où placer un vaisseau.

  - show_state_rotation: Cette fonction est utilisée pour montrer les différentes rotations possibles pour le navire sélectionné.

  - show_comp_comp: Fonction pour montrer la partie en cours entre deux bots.

  - show_state_of_the_fight: Fonction pour montrer les grille de l'humaine et de l'ordinateur pendant le match.

  - print_victory: Fonction pour afficher le résultat d'un match.

  - pretty_dict_print: Fonction pour avoir un bel affichage de l’état des bateau durant de leur placement sur le plateau de jeu.


### ia_difficile:


### ia_general:


### ia_moyen:


### interface:




There are 3 possibilities :

  - Human vs bot

  - Bot vs bot

  - Bot solo

Version 1.0.0
Implemented easy (facile), medium (moyen) and hard (difficile) bot.







