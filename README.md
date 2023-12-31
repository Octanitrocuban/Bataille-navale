# Battleship / Bataille-navale

## English (Français en-dessous):
Own implementation of battleship game.

### Files and functions:

#### game_loop:
Module containing functions to make a human race against the computer or two bots between them.

  - main_loop_human_bot: Main function that allows a human to do a battle game against a bot of the chosen difficulty.
    
  - bot_match: Function to make 2 fighting algorithms.

  - bot_analyse: Function to play a single bot to analyze the number of shots needed to sink all the boats of a random map.


#### execute:
Module containing functions to make a human fight against the computer, two bots between them or to test the effectiveness of a bot.

  - 'humain': starts a match between a human and a bot.

  - 'bot vs bot': allows one bot to compete against another to test the difference in strength between the two.

  - 'test bot': Test the number of shots a bot needs to complete a random card and see which phase of the bot is the strongest.


#### graphics:
This module countain the graphical functions used to plot the game board.

  - show_state_ancrage: This function is used to show the different possibles cells where to put a ship.

  - show_state_rotation: This function is used to show the different possibles rotations for the selected ship.

  - show_comp_comp: Function to show the fight between two bots.

  - show_state_of_the_fight: Function to show the human and computer grid during the fight.

  - print_victory: Function to print the result of a game.

  - pretty_dict_print: Function to have a nice print of the state of your boat when placing them.


#### ia_hard:
Module containing the functions specific to the hard difficulty bot.

  - opening: This function is used to generate an opening library for the bot so you don’t have to recalculate the pdf at the beginning of each game.

  - map_one_boat: This function calculated the probability density function of the repartition of a ship on a given map.

  - approx_density: This function is used to calculated the probability density function of the possible repartion of ship on a given map.

  - inner: Function to select the position from list_keep that are on the 0 cell value of the damier.

  - choice_appx_dens_map: This function is used to determine which cell should be targeted.

  - sink_proba_map: Function to calculate the probability map by boat.

  - proba_sinker: Function to calculate probability map for each boat remaining on the map.


#### ia_general:
Module containing general functions.

  - create_possible_places: Function to create two list containing the possibles positions on the plate.

  - random_positiong_ships: Function to randomly fill a plate with the boats.

  - look_loop_pth: Function to remove cells that were already explored.

  - look_first_hit: Function to choose a surrounding cell to those that contain a unsunk boat.

  - look_end_cell: Function to extract the positions at the other end of the boat at the i-th rotation.

  - damier_positions: Created a list of coordinates so that they form a checkerboard.

  - random_hit: Function to choose a random position from a list of possible target.

  - conseq_fire: Function to update the state of the differents variables after the human and the computer plays.


#### ia_medium:
Module containing the functions specific to the medium difficulty bot.

  - neighbor_search: Function to search around the found boat to complete it.


#### interface:
Module for the human actions.

  - placing_human_boats: Function with witch the human will place its boats.

  - choice_difficulty: Function with wich the human will choose the difficulty level.

  - human_play: Function to make the human player choose where to fires at the computer plate.


### Version 1.0.0
There are three bots against which it is possible to play. For each of them, their activity is separated into two phases: hunting and destruction.

  - easy: in the hunting phase, the bot randomly fires on an unexplored square. In the phase of destruction, the bot takes the four direct neighbors of all the cells where there is a sunken boat. He only keeps the cells unexplored, then randomly chooses one of them.

  - medium: in the hunting phase, the bot randomly chooses an unexplored cell that is part of a pre-calculated cell list. This list contains the positions of every other cell, so that they correspond to the white or black squares of a checkerboard. In the phase of destruction, the bot looks for whether the cells containing an affected boat line up horizontally or vertically in order to continue in the same extension.

  - hard: in the hunting phase, the bot approximates the probability density function of the ships according to those already sunk and cells already explored. For this purpose it adds all valid positions for each vessel independently. In the destruction phase, the bot approximates the probability density function of distribution of the boats in the same way as in the hunting phase, but in such a way as to target the cells around those that have already touched a boat.



## Français :

### Fichiers et fonctions :

#### boucle_de_jeu :
Module contenant les fonctions permetant de faire s'affonter un humain contre l'ordinateur ou deux bots entre eux.

  - main_loop_human_bot : Fonction principale qui permet à un humain de faire une partie de bataille contre un bot de la difficulté choisit.
    
  - bot_match : Fonction pour faire 2 algorithmes de combat.

  - bot_analyse : Fonction pour faire jouer un bot seul afin d'analyser le nombre de tir nécessaire pour couler tous les bateaux d'une carte aléatoire.


#### execute :
Module contenant les fonctions permetant de faire s'affonter un humain contre l'ordinateur, deux bots entre eux ou pour tester l'efficacité d'un bot.

  - 'humain': enclenche un matche entre un humain et un bot.

  - 'bot vs bot' : permet de faire s'affronter un bot contre un autre pour tester la différence de force entre les deux.

  - 'test bot' : Permets de tester le nombre de tirs nécessaires à un bot pour compléter une carte aléatoire et voir quelle phase du bot est la plus forte.


#### graphics :
Ce module compte les fonctions graphiques utilisées pour tracer le plateau de jeu.

  - show_state_ancrage : Cette fonction est utilisée pour montrer les différentes cellules possibles où placer un vaisseau.

  - show_state_rotation : Cette fonction est utilisée pour montrer les différentes rotations possibles pour le navire sélectionné.

  - show_comp_comp : Fonction pour montrer la partie en cours entre deux bots.

  - show_state_of_the_fight : Fonction pour montrer les grille de l'humaine et de l'ordinateur pendant le match.

  - print_victory : Fonction pour afficher le résultat d'un match.

  - pretty_dict_print : Fonction pour avoir un bel affichage de l’état des bateau durant de leur placement sur le plateau de jeu.


#### ia_difficile :
Module contenant les functions spécifiques au mode de difficulté difficile.

  - opening : Cette fonction sert à générer une biblithèque d'ouverture pour le bot afin de ne pas avoir à recalculer la pdf à chaque début de jeu.

  - map_one_boat : Cette fonction sers a calculé la fonction de densité de probabilité de la répartition d’un navire sur une carte donnée.

  - approx_density : Cette fonction est utilisée pour calculer la fonction de densité de probabilité de la répartition possible du navire sur une carte donnée.

  - inner : Fonction pour sélectionner les positions de list_keep qui sont sur des cellules valant 0 dans le damier fournit.

  - choice_appx_dens_map : Cette fonction est utiliser pour déterminer quelle cellule doit être ciblée.

  - sink_proba_map : Fonction pour calculer la carte de probabilité par bateau.

  - proba_sinker : Fonction pour calculer la case à cibler en fonction de la probabilité pour chaque bateau restant sur la carte.


#### ia_general :
Module contant les functions générales.

  - create_possible_places : Fonction pour créer deux listes contenant les positions possibles sur le plateau de jeu.

  - random_positiong_ships : Fonction pour remplir aléatoirement le plateau de jeu avec les bateaux.

  - look_loop_pth : Fonction pou enlever les cellules qui ont déjà été explorées.

  - look_first_hit : Fonction pour choisir une cellule environante à celles qui contiennent un bateau non coulé.

  - look_end_cell : Fonction pour extraire les positions à l’autre extrémité du bateau à la i-ième rotation.

  - damier_positions : Créé une liste de coordonnées de manière à ce que celles-ci forment un damier.

  - random_hit : Fonction pour choisir une position aléatoire dans une liste de cibles possibles.

  - conseq_fire : Fonction pour mettre à jour l’état des différentes variables après les tours de jeu de l’humain et de l’ordinateur.


#### ia_moyen :
Module contenant les fonctions spécifiques au bot de difficulté moyen.

  - neighbor_search : Fonction de faire la recherche autour du bateau trouvé pour l'achever.


#### interface :
Module pour les actions de l'humain.

  - placing_human_boats : Fonction avec laquelle l’humain placera ses bateaux.

  - choice_difficulty : Fonction avec laquelle l’humain choisira le niveau de difficulté.

  - human_play : Fonction pour faire choisir au joueur humain choisir où tirer sur la table de jeu d’ordinateur.


### Version 1.0.0
Il y a trois bots contres lesquels il est possible de jouer. Pour chacun d'entre eux, leur activité est separé en deux phases : la chasse et la destruction. Les 

  - facile : en phase de chasse, le bot tir aléatoirement sur une case non explorée. En phase de destruction, le bot prend les quatre voisines directes de toutes les cellules où se trouve un bateau non coulé. Il ne garde que les cellules non explorées, puis choisit aléatoirement l'une d'entre elles.

  - moyen : en phase de chasse, le bot choisit aléatoirement une cellule non explorée qui fait partie d'une liste de cellules précalculée. Cette liste contient les positions d'une cellule sur deux, de sorte que ces dernières correspondent aux cases blanches ou noires d'un damier. En phase de destruction, le bot cherche si les cellules contenant un bateau touché s'alignent horizontalement ou verticalement afin de continuer dans le même prolongement.

  - difficile : en phase de chasse, le bot approxime la fonction de densité de probabilité de répartition des bateaux en fonction de ceux déjà coulés et des cellules déjà explorées. Pour cela il additionne toutes les positions valides pour chaque navire de façon indépendante. En phase de destruction, le bot approxime la fonction de densité de probabilité de répartition des bateaux de la même manière qu'en phase de chasse, mais de manière à cibler les cellules autour de celles ayant déjà touché  un bateau.
