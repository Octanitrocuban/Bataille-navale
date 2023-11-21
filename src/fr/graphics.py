# -*- coding: utf-8 -*-
"""
Ce module compte les fonctions graphiques utilisées pour tracer le plateau de
jeu.
"""
import matplotlib.pyplot as plt
import numpy as np
#=============================================================================
def show_state_ancrage(tablehumain, dicshiphumain, lplaces):
	"""
	Cette fonction est utilisée pour montrer les différentes cellules
	possibles où placer un vaisseau.

	Paramètres
	----------
	tablehumain : numpy.ndarray
		Table de jeu de l'humaine avec les couleurs rvb pour indiquer où sont
		les bateaux.
	dicshiphumain : dict
		Dictionnaire humain où l’état des bateaux est enregistré.
	lplaces : list
		Liste de deux listes de chaînes de caractères. Correspond aux valeurs
		à mettre sur les axes x et y. Provient de la fonction create_pos_pl().

	Retourne
	--------
	Rien.

	"""
	plt.figure(figsize=(8, 8))
	plt.imshow(tablehumain, zorder=1)
	# pour avoir les lignes de la grille et les labels sur les axes décalés
	plt.xticks(range(10), lplaces[1], fontsize=13)
	plt.yticks(range(10), lplaces[0], fontsize=13)
	for i in np.arange(0.5, 9.5, 1):
		plt.hlines(i, -0.5, 9.5, "k", zorder=2)
		plt.vlines(i, -0.5, 9.5, "k", zorder=2)

	for j in list(dicshiphumain.keys()):
		plt.plot(dicshiphumain[j]['y'][0], dicshiphumain[j]['x'][0],
			   's', color=dicshiphumain[j]['rvb'], label=j)

		plt.legend(loc=(1.01, 0.5))

	plt.show()

def show_state_rotation(table_humain, dic_hum, radius, end_cells, indice_boat,
						lplaces, rempl_ship_hum, position_xy, ship_name):
	"""
	Cette fonction est utilisée pour montrer les différentes rotations
	possibles pour le navire sélectionné.

	Paramètres
	----------
	table_humain : numpy.ndarray
		Table de jeu de l'humaine avec les couleurs rvb pour indiquer où sont
		les bateaux.
	dic_hum : dict
		Dictionnaire d'initialisation des bateaux.
	radius : int
		Longueur (en cellule) du bateau.
	end_cells : numpy.ndarray
		Matrice numpy énumérant les positions à l’autre extrémité du bateau
		à la i-ième rotation.
	indice_boat : int
		Position à laquelle le bateau choisi est dans la liste des bateaux.
		Elle sera utilisée pour accéder aux paramètres de ce bateau.
	lplaces : list
		Liste de deux listes de chaînes de caractères. Correspond aux valeurs
		à mettre sur les axes x et y. Provient de la fonction create_pos_pl().
	rempl_ship_hum : dict
		Dictionnaire humain où l’état des bateaux est enregistré.
	position_xy : numpy.ndarray
		Positions du point de pivotement utilisées pour la rotation.
	ship_name : str
		Nom du bateau choisit.

	Retourne
	--------
	Rien.

	"""
	plt.figure(figsize=(8*len(end_cells), 9))
	for i in range(len(end_cells)):
		# créer une représentation pour les rotations possibles
		table_hum_2 = np.copy(table_humain)
		# utilise la cellule de départ et de fin pré-calculée pour éviter une
		# collision avec un autre bateau ou de sortir du cadre
		xh = np.linspace(position_xy[0], end_cells[i, 0], radius+1, dtype=int)
		yh = np.linspace(position_xy[1], end_cells[i, 1], radius+1, dtype=int)
		table_hum_2[xh, yh, :] = dic_hum['Codes rvb'][indice_boat]

		plt.subplot(1, len(end_cells), i+1)
		plt.title("Rotation n°"+str(i))
		plt.imshow(table_hum_2, zorder=1)
		# astuce pour avoir une légende avec la couleur et le nom du bateau
		plt.plot(yh[0], xh[0], 's', label=ship_name,
				color=dic_hum['Codes rvb'][indice_boat], zorder=2)

		# afficher les bateaux déjà placés
		for j in list(rempl_ship_hum.keys()):
			plt.plot(rempl_ship_hum[j]['y'][0], rempl_ship_hum[j]['x'][0],
					 's', color=rempl_ship_hum[j]['rvb'], label=j, zorder=2)

		plt.plot(position_xy[1], position_xy[0], "ro",
				 label="Centre de\nrotation", zorder=2)

		# pour avoir les lignes de grille et les labels sur les axes décalés
		plt.xticks(range(10), lplaces[1], fontsize=13)
		plt.yticks(range(10), lplaces[0], fontsize=13)
		for j in np.arange(0.5, 9.5, 1):
			plt.hlines(j, -0.5, 9.5, "k", zorder=2)
			plt.vlines(j, -0.5, 9.5, "k", zorder=2)

		if i == len(end_cells)-1:
			plt.legend(loc=(1.01, 0.2))

	plt.show()

def show_comp_comp(table_bot1, dico_bot1, watter_bot1, notsink_bot1,
				   sinked_bot1, table_bot2, dico_bot2, watter_bot2,
				   notsink_bot2, sinked_bot2, list_ppl):
	"""
	Fonction pour montrer la partie en cours entre deux bots.

	Paramètres
	----------
	table_bot1 : numpy.ndarray
		Table de jeu du premier bot avec les couleurs rvb pour indiquer
		où sont les bateaux.
	dico_bot1 : dict
		Dictionnaire du premier bot où l’état des bateaux est enregistré.
	watter_bot1 : list
		Liste des tirs du premier bot qui ont touché une cellule contenant
		de l'eau.
	notsink_bot1 : list
		Liste des tirs du premier bot qui ont touché une cellule contenant
		un bateau sans le couler.
	sinked_bot1 : list
		Liste des tirs du premier bot qui ont touché une cellule contenant
		un bateau qui a été coulé.
	table_bot2 : numpy.ndarray
		Table de jeu du second bot avec les couleurs rvb pour indiquer
		où sont les bateaux.
	dico_bot2 : dict
		Dictionnaire du second bot où l’état des bateaux est enregistré.
	watter_bot2 : list
		Liste des tirs du second bot qui ont touché une cellule contenant
		de l'eau.
	notsink_bot2 : list
		Liste des tirs du second bot qui ont touché une cellule contenant
		un bateau sans le couler.
	sinked_bot2 : list
		Liste des tirs du second bot qui ont touché une cellule contenant
		un bateau qui a été coulé.
	list_ppl : list
		Liste de deux listes de chaînes de caractères. Correspond aux valeurs
		à mettre sur les axes x et y. Provient de la fonction create_pos_pl().

	Retourne
	--------
	Rien.

	"""
	plt.figure(figsize=(13, 5))
	plt.subplot(1, 2, 1)
	plt.title("Grille du joueur 1")
	plt.imshow(table_bot1, zorder=1)
	plt.xticks(range(10), list_ppl[1], fontsize=13)
	plt.yticks(range(10), list_ppl[0], fontsize=13)
	for i in np.arange(0.5, 9.5, 1):
		plt.hlines(i, -0.5, 9.5, "k", zorder=2)
		plt.vlines(i, -0.5, 9.5, "k", zorder=2)

	for j in list(dico_bot1.keys()):
		plt.plot(dico_bot1[j]['y'][0], dico_bot1[j]['x'][0], 's',
				 color=dico_bot1[j]['rvb'], label=j, zorder=2)

	for j in range(len(watter_bot1)):
		plt.plot(watter_bot1[j][1], watter_bot1[j][0], 'bo', zorder=2)

	for j in range(len(notsink_bot1)):
		plt.plot(notsink_bot1[j][1], notsink_bot1[j][0], 'ro', zorder=2)

	for j in range(len(sinked_bot1)):
		plt.plot(sinked_bot1[j][1], sinked_bot1[j][0], 'ko', zorder=2)

	plt.legend(loc=(1.01, 0.5))
	plt.subplot(1, 2, 2)
	plt.title("Grille du joueur 2")
	plt.imshow(table_bot2, zorder=1)
	plt.xticks(range(10), list_ppl[1], fontsize=13)
	plt.yticks(range(10), list_ppl[0], fontsize=13)
	for i in np.arange(0.5, 9.5, 1):
		plt.hlines(i, -0.5, 9.5, "k", zorder=2)
		plt.vlines(i, -0.5, 9.5, "k", zorder=2)

	for j in list(dico_bot2.keys()):
		plt.plot(dico_bot2[j]['y'][0], dico_bot2[j]['x'][0],
			   's', color=dico_bot2[j]['rvb'], label=j, zorder=2)

	for j in range(len(watter_bot2)):
		plt.plot(watter_bot2[j][1], watter_bot2[j][0], 'bo', zorder=2)

	for j in range(len(notsink_bot2)):
		plt.plot(notsink_bot2[j][1], notsink_bot2[j][0], 'ro', zorder=2)

	for j in range(len(sinked_bot2)):
		plt.plot(sinked_bot2[j][1], sinked_bot2[j][0], 'ko', zorder=2)

	plt.legend(loc=(1.01, 0.5))
	plt.show()

def show_state_of_the_fight(table_humain, listppl, human_dico, ordi_watter,
							ordi_notsink, ordi_sinked, what_human_see):
	"""
	Fonction pour montrer les grille de l'humaine et de l'ordinateur pendant
	le match. Pour la grille humaine, il y aura :
		-les positions de ses bateaux indiqué par la couleurs des cellules;
		-La mer est coloriée en blanc;
		-la légende avec la couleur correspondant aux navires restant;
		-les positions où l’ordinateur a frappé la mer avec des points bleus;
		-les positions où l’ordinateur a frappé un bateau avec des points rouges;
		-les positions où l’ordinateur a coulé un bateau avec des points noirs;

	Paramètres
	----------
	table_humain : numpy.ndarray
		Table de jeu de l'humaine avec les couleurs rvb pour indiquer où sont
		les bateaux.
	list_ppl : list
		Liste de deux listes de chaînes de caractères. Correspond aux valeurs
		à mettre sur les axes x et y. Provient de la fonction create_pos_pl().
	human_dico : dict
		Dictionnaire humain où l’état des bateaux est enregistré.
	ordi_watter : list
		Liste des tirs de l'ordinateur qui ont touché une cellule contenant
		de l'eau.
	ordi_notsink : list
		Liste des tirs qui ont touché une cellule contenant un bateau sans
		le couler.
	ordi_sinked : list
		Liste des tirs qui ont touché une cellule contenant un bateau qui a
		été coulé.
	what_human_see : numpy.ndarray
		Table de jeu où l'humain peut voir les conséquences de ses tirs contre
		l'ordinateur. C’est un tableau 2d rgb avec : les cellules bleue
		indiquent un coup dans l'eau, les cellules rouge indiquent qu’un
		bateau a été touché mais pas encore coulé, les cellules noires
		indiquent qu’un bateau a été touché et coulé et les cellules blanche
		sont celles qui n'ont pas encore été explorées.

	Retourne
	--------
	Rien.

	"""
	plt.figure(figsize=(19, 9))
	plt.subplot(1, 2, 1)
	plt.title("Table de jeu de l'humain")
	plt.imshow(table_humain, zorder=1)
	plt.xticks(range(10), list_ppl[1], fontsize=13)
	plt.yticks(range(10), list_ppl[0], fontsize=13)
	for i in np.arange(0.5, 9.5, 1):
		plt.hlines(i, -0.5, 9.5, "k", zorder=2)
		plt.vlines(i, -0.5, 9.5, "k", zorder=2)

	for j in list(human_dico.keys()):
		plt.plot(human_dico[j]['y'][0], human_dico[j]['x'][0],
			   's', color=human_dico[j]['rvb'], label=j)

	for j in range(len(ordi_watter)):
		plt.plot(ordi_watter[j][1], ordi_watter[j][0], 'bo')

	for j in range(len(ordi_notsink)):
		plt.plot(ordi_notsink[j][1], ordi_notsink[j][0], 'ro')

	for j in range(len(ordi_sinked)):
		plt.plot(ordi_sinked[j][1], ordi_sinked[j][0], 'ko')

	plt.legend(loc=(1.01, 0.5))
	plt.subplot(1, 2, 2)
	plt.title("Table de jeu de l'orninateur")
	plt.imshow(what_human_see, zorder=1)
	plt.xticks(range(10), list_ppl[1], fontsize=13)
	plt.yticks(range(10), list_ppl[0], fontsize=13)
	for i in np.arange(0.5, 9.5, 1):
		plt.hlines(i, -0.5, 9.5, "k", zorder=2)
		plt.vlines(i, -0.5, 9.5, "k", zorder=2)

	plt.show()

def print_victory(victoire, list_sinked, list_water):
	"""
	Fonction pour afficher le résultat d'un match.

	Paramètres
	----------
	victoire : str
		Chaîne de caractères indiquant qui a remporté le match.
	list_sinked : list
		Liste des tirs qui ont touché une cellule contenant un bateau.
	list_water : list
		Liste des tirs qui ont touché une cellule contenant de l'eau.

	Retourne
	--------
	int
		Nombre de coup réaliser par le joueur durant le match.

	"""
	if victoire == "nulle":
		print("Partie nulle.")

	elif Victoire == "humain":
		print("Victoire humain.")
		print("******    ******     ******     *           *    ******* ")
		print("*     *   *     *   *       *    *         *    *       *")
		print("*     *   *     *   *       *     *       *     *       *")
		print("******    ******    *********      *     *      *       *")
		print("*     *   * *       *       *       *   *       *       *")
		print("*     *   *   *     *       *        * *        *       *")
		print("******    *     *   *       *         *          ******* ")
	
	elif victoire == "ordinateur":
		print("Victoire ordinateur.")

	return len(list_sinked)+len(list_water)

def pretty_dict_print(ship_dico):
	"""
	Fonction pour avoir un bel affichage de l’état des bateau durant de
	leur placement sur le plateau de jeu.

	Paramètres
	----------
	ship_dico : dict
		Dictionnaire où l’état des bateaux est enregistré.

	Retourne
	--------
	Rien.

	"""
	num = ship_dico['Nombre']
	nam = ship_dico['Type']
	sep = '+'+'-'*13+'+'+'-'*9+'+'+'-'*10+'+'+'-'*8+'+'+'-'*9+'+'+'-'*20+'+'
	print(sep)
	print('|     Type    | Numéros | Longueur | Nombre | Couleur |'
		 +'      Codes rvb     |')
	print(sep)
	if 'Porte-avion' in ship_dico['Type']:
		print('| Porte-avion |    0    |     5    |    '
			 +str(num[nam == 'Porte-avion'][0])+'   |  gris   | '
			 +'[0.50, 0.50, 0.50] |')
		print(sep)

	if 'Croiseur' in ship_dico['Type']:
		print('|   Croiseur  |    1    |     4    |    '
			 +str(num[nam == 'Croiseur'][0])+'   | orange  | '
			 +'[1.00, 0.50, 0.00] |')
		print(sep)

	if 'Sous-marin' in ship_dico['Type']:
		print('|  Sous-marin |    2    |     3    |    '
			 +str(num[nam == 'Sous-marin'][0])+'   |   vert  | '
			 +'[0.00, 0.75, 0.00] |')
		print(sep)

	if 'Frégate' in ship_dico['Type']:
		print('|    Frégate  |    3    |     3    |    '
			 +str(num[nam == 'Frégate'][0])+'   |  jaune  | '
			 +'[1.00, 0.90, 0.00] |')
		print(sep)

	if 'Navette' in ship_dico['Type']:
		print('|    Navette  |    4    |     2    |    '
			 +str(num[nam == 'Navette'][0])+'   | violet  | '
			 +'[0.75, 0.00, 0.75] |')
		print(sep)
