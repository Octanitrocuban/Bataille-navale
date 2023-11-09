# -*- coding: utf-8 -*-
"""
@author: Nougaret Matthieu

Module contant les functions générales.

"""
import numpy as np
from copy import deepcopy
#=============================================================================
def create_possible_places():
	"""
	Fonction pour créer deux listes contenant les positions possibles sur le
	plateau de jeu.

	Retourne
	--------
	axes : liste
		Liste de 2 listes contenant le nom des lignes et colonnes.
	poss_places : liste
		Liste de chaînes de caractaîres. Elle correspond à toutes les
		combinaisons possibles de position lorsque l’humain les rentre :
		(['A0', 'A1', ..., '8J', '9J']).

	"""
	axes = [list("ABCDEFGHIJ"), list("0123456789")]
	poss_1 = np.sort(axes[0]*10).astype(object)+np.array(axes[1]*10,
														 dtype=object)

	poss_2 = np.sort(axes[1]*10).astype(object)+np.array(axes[0]*10,
														 dtype=object)

	poss_places = np.concatenate((poss_1, poss_2)).tolist()
	return axes, poss_places

def random_positiong_ships(ships_dico, computer_table=None):
	"""
	Fonction pour remplir aléatoirement le plateau de jeu avec les bateaux.

	Paramètres
	----------
	ships_dico : dict
		Dictionnaire d'initialisation des navires. :
			Bateaux = {
				'Type':np.array(['Porte-avion', 'Croiseur', 'Sous-marin',
								 'Frégate', 'Navette']),
				'Longueur': np.array([5, 4, 3, 3, 2]),
				'Nombre': np.array([1, 1, 1, 1, 1]),
				'Couleur': np.array(['gris', 'orange', 'vert', 'jaune',
									 'violet']),
				'Codes rvb':np.array([[0.50, 0.50, 0.50], [1.00, 0.50, 0.00],
									  [0.00, 0.75, 0.00], [1.00, 0.90, 0.00],
									  [0.75, 0.00, 0.75]])}

	Retourne
	--------
	navig_ordi : dict
		Dictionnaire décrivant l'état des navires.
	computer_table : np.ndarray
		Matrice np.array à 3 dimensions. Elle indiques les positions des
		navires à travers leur valeur de code rvb.

	Example
	-------
	In [0] : random_positiong_ships(Boats)
	Out [0]: ({'Navette':{'x':array([2, 3]), 'y':array([7, 7]),
			   'Couleur':'violet', 'rvb':array([0.75, 0., 0.75])},
			   'Sous-marin':{'x':array([2, 2, 2]), 'y': array([2, 1, 0]),
			   'Couleur':'vert', 'rvb':array([0., 0.75, 0.])},
			   'Porte-avion':{'x':array([1, 1, 1, 1, 1]),
			   'y':array([8, 7, 6, 5, 4]), 'Couleur':'gris',
			   'rvb':array([0.5, 0.5, 0.5])},
			   'Croiseur':{'x':array([6, 6, 6, 6]), 'y':array([1, 2, 3, 4]),
			   'Couleur':'orange', 'rvb':array([1., 0.5, 0.])},
			   'Frégate':{'x':array([2, 2, 2]), 'y':array([3, 4, 5]),
			   'Couleur':'jaune', 'rvb':array([1., 0.9, 0.])}},
			 array([[[1. , 1.  , 1. ], [1.  , 1.  , 1.  ], [1. , 1.  , 1. ],
					 [1. , 1.  , 1. ], [1.  , 1.  , 1.  ], [1. , 1.  , 1. ],
					 [1. , 1.  , 1. ], [1.  , 1.  , 1.  ], [1. , 1.  , 1. ],
					 [1. , 1.  , 1. ]],
					[[1. , 1.  , 1. ], [1.  , 1.  , 1.  ], [1. , 1.  , 1. ],
					 [1. , 1.  , 1. ], [0.5 , 0.5 , 0.5 ], [0.5, 0.5 , 0.5],
					 [0.5, 0.5 , 0.5], [0.5 , 0.5 , 0.5 ], [0.5, 0.5 , 0.5],
					 [1. , 1.  , 1. ]],
					[[0. , 0.75, 0. ], [0.  , 0.75, 0.  ], [0. , 0.75, 0. ],
					 [1. , 0.9 , 0. ], [1.  , 0.9 , 0.  ], [1. , 0.9 , 0. ],
					 [1. , 1.  , 1. ], [0.75, 0.  , 0.75], [1. , 1.  , 1. ],
					 [1. , 1.  , 1. ]],
					[[1. , 1.  , 1. ], [1.  , 1.  , 1.  ], [1. , 1.  , 1. ],
					 [1. , 1.  , 1. ], [1.  , 1.  , 1.  ], [1. , 1.  , 1. ],
					 [1. , 1.  , 1. ], [0.75, 0.  , 0.75], [1. , 1.  , 1. ],
					 [1. , 1.  , 1. ]],
					[[1. , 1.  , 1. ], [1.  , 1.  , 1.  ], [1. , 1.  , 1. ],
					 [1. , 1.  , 1. ], [1.  , 1.  , 1.  ], [1. , 1.  , 1. ],
					 [1. , 1.  , 1. ], [1.  , 1.  , 1.  ], [1. , 1.  , 1. ],
					 [1. , 1.  , 1. ]],
					[[1. , 1.  , 1. ], [1.  , 1.  , 1.  ], [1. , 1.  , 1. ],
					 [1. , 1.  , 1. ], [1.  , 1.  , 1.  ], [1. , 1.  , 1. ],
					 [1. , 1.  , 1. ], [1.  , 1.  , 1.  ], [1. , 1.  , 1. ],
					 [1. , 1.  , 1. ]],
					[[1. , 1.  , 1. ], [1.  , 0.5 , 0.  ], [1. , 0.5 , 0. ],
					 [1. , 0.5 , 0. ], [1.  , 0.5 , 0.  ], [1. , 1.  , 1. ],
					 [1. , 1.  , 1. ], [1.  , 1.  , 1.  ], [1. , 1.  , 1. ],
					 [1. , 1.  , 1. ]],
					[[1. , 1.  , 1. ], [1.  , 1.  , 1.  ], [1. , 1.  , 1. ],
					 [1. , 1.  , 1. ], [1.  , 1.  , 1.  ], [1. , 1.  , 1. ],
					 [1. , 1.  , 1. ], [1.  , 1.  , 1.  ], [1. , 1.  , 1. ],
					 [1. , 1.  , 1. ]],
					[[1. , 1.  , 1. ], [1.  , 1.  , 1.  ], [1. , 1.  , 1. ],
					 [1. , 1.  , 1. ], [1.  , 1.  , 1.  ], [1. , 1.  , 1. ],
					 [1. , 1.  , 1. ], [1.  , 1.  , 1.  ], [1. , 1.  , 1. ],
					 [1. , 1.  , 1. ]],
					[[1. , 1.  , 1. ], [1.  , 1.  , 1.  ], [1. , 1.  , 1. ],
					 [1. , 1.  , 1. ], [1.  , 1.  , 1.  ], [1. , 1.  , 1. ],
					 [1. , 1.  , 1. ], [1.  , 1.  , 1.  ], [1. , 1.  , 1. ],
					 [1. , 1.  , 1. ]]]))

	"""
	kpa = np.array([[[ 0,  0], [ 0,  1], [ 0,  2], [ 0,  3], [ 0,  4]],
					[[ 0,  0], [ 1,  0], [ 2,  0], [ 3,  0], [ 4,  0]],
					[[ 0,  0], [ 0, -1], [ 0, -2], [ 0, -3], [ 0, -4]],
					[[ 0,  0], [-1,  0], [-2,  0], [-3,  0], [-4,  0]]],
				   dtype=int)

	kcr = np.array([[[ 0,  0], [ 0,  1], [ 0,  2], [ 0,  3]],
					[[ 0,  0], [ 1,  0], [ 2,  0], [ 3,  0]],
					[[ 0,  0], [ 0, -1], [ 0, -2], [ 0, -3]],
					[[ 0,  0], [-1,  0], [-2,  0], [-3,  0]]], dtype=int)

	ksm = np.array([[[ 0,  0], [ 0,  1], [ 0,  2]], [[ 0,  0], [ 1,  0],
					 [ 2,  0]], [[ 0,  0], [ 0, -1], [ 0, -2]], [[ 0,  0],
					 [-1,  0], [-2,  0]]], dtype=int)

	knv = np.array([[[ 0,  0], [ 0,  1]], [[ 0,  0], [ 1,  0]], [[ 0,  0],
					[ 0, -1]], [[ 0,  0], [-1,  0]]], dtype=int)

	copy_dico = deepcopy(ships_dico)
	if type(computer_table) == type(None):
		computer_table = np.ones((10, 10, 3), dtype=float)

	navig_ordi = {}
	for i in range(np.sum(copy_dico['Nombre'] > 0)):
		ship = np.random.choice(
				copy_dico['Type'][copy_dico['Nombre'] > 0], 1)[0]
		id_type = np.where(copy_dico['Type'] == ship)[0][0]
		ancres = np.argwhere((computer_table[:, :, 0] == 1)&(
							  computer_table[:, :, 1] == 1)&(
							  computer_table[:, :, 2] == 1))

		ray = copy_dico['Longueur'][id_type]
		if ray == 2:
			kernel = np.copy(knv)
		elif ray == 3:
			kernel = np.copy(ksm)
		elif ray == 4:
			kernel = np.copy(kcr)
		elif ray == 5:
			kernel = np.copy(kpa)

		possibles = np.concatenate(
							(ancres[:, np.newaxis, np.newaxis]+kernel))
		possibles = possibles[np.sum((possibles[:, :, 0] <= 9)&(
									  possibles[:, :, 1] <= 9)&(
									  possibles[:, :, 0] >= 0)&(
									  possibles[:, :, 1] >= 0),
									  axis=1) == ray]

		possibles = possibles[np.sum(np.sum(computer_table[
						possibles[:, :, 0], possibles[:, :, 1]], axis=1),
						axis=1) == 3*ray]

		choice = possibles[np.random.randint(len(possibles))]
		navig_ordi[ship] = {}
		navig_ordi[ship]['x'] = choice[:, 0]
		navig_ordi[ship]['y'] = choice[:, 1]
		navig_ordi[ship]['Couleur'] = copy_dico['Couleur'][id_type]
		navig_ordi[ship]['rvb'] = copy_dico['Codes rvb'][id_type]
		computer_table[choice[:, 0], choice[:, 1]] = navig_ordi[ship]['rvb']
		copy_dico['Nombre'][id_type] -= 1

	return navig_ordi, computer_table

def look_loop_pth(possib_try, water, notsink, sinked):
	"""
	Fonction pou enlever les cellules qui ont déjà été explorées.

	Paramètres
	----------
	possib_try : numpy.ndarray
		Liste de position de cellules.
	water : list
		Liste des cellules qui ont déjà été explorées et contiennent de
		l'eau.
	notsink : list
		Liste des cellules qui ont déjà été explorées et qui contiennent un
		bateau qui n'a pas encore été coulé.
	sinked : list
		Liste des cellules qui ont déjà été explorées et qui contiennent un
		bateau qui a été coulé.

	Retourne
	--------
	PossibTryHit_2 : list
		Liste de la position de la cellule qui pourrait faire partie du
		navire qui est déjà toucher mais pas encore coulé.

	"""
	not_in = water+notsink+sinked
	possib_try_2 = []
	for i in range(len(possib_try)):
		if possib_try[i] not in not_in:
			possib_try_2.append(possib_try[i])

	return possib_try_2

def look_first_hit(water, notsink, sinked):
	"""
	Fonction pour choisir une cellule environante à celles qui contiennent un
	bateau non coulé.

	Paramètres
	----------
	water : list
		Liste des cellules qui ont déjà été explorées et contiennent de
		l'eau.
	notsink : list
		Liste des cellules qui ont déjà été explorées et qui contiennent un
		bateau qui n'a pas encore été coulé.
	sinked : list
		Liste des cellules qui ont déjà été explorées et qui contiennent un
		bateau qui a été coulé.

	Retourne
	--------
	x_ch : int
		Ligne de la cellule choisit.
	y_ch : int
		Colonne de la cellule choisit.

	"""
	poss_try = []
	for i in range(len(notsink)):
		if notsink[i][0] < 9:
			poss_try.append([notsink[i][0]+1, notsink[i][1]])
		if notsink[i][0] > 0:
			poss_try.append([notsink[i][0]-1, notsink[i][1]])
		if notsink[i][1] < 9:
			poss_try.append([notsink[i][0], notsink[i][1]+1])
		if notsink[i][1] > 0:
			poss_try.append([notsink[i][0], notsink[i][1]-1])

	poss_try = look_loop_pth(poss_try, water, notsink, sinked)
	if len(poss_try) == 1:
		x_ch, y_ch = poss_try[0]
	elif len(poss_try) > 1:
		x_ch, y_ch = poss_try[np.random.randint(len(poss_try))]
	else:
		raise

	return x_ch, y_ch

def look_end_cell(radius, xy, play_table):
	"""
	Fonction pour extraire les positions à l’autre extrémité du bateau à la
	i-ième rotation.

	Paramètres
	----------
	radius : int
		Longueur du bateau choisi.
	xy : numpy.ndarray
		Positions du point de pivotement utilisé pour la rotation.
	play_table : numpy.ndarray
		Plateau de jeu où les couleur indiquent où sont les bateaux.

	Retourne
	--------
	rota_cell : numpy.ndarray
		Numpy ndarray listing the positions at the other end of the boat at
		the i-th rotation.

	"""
	onegan = np.arange(radius)
	zergan = np.zeros(radius, dtype=int)
	rota_cell = np.array([[xy[0]+onegan, xy[1]+zergan],
						  [xy[0]-onegan, xy[1]+zergan],
						  [xy[0]+zergan, xy[1]+onegan],
						  [xy[0]+zergan, xy[1]-onegan]]).transpose((0, 2, 1))

	rota_cell = rota_cell[np.sum((rota_cell[:, :, 0] >= 0)&(
								  rota_cell[:, :, 1] >= 0)&(
								  rota_cell[:, :, 0] <= 9)&(
								  rota_cell[:, :, 1] <= 9),
								 axis=1) == radius]

	rota_cell = rota_cell[np.sum(np.sum(play_table[rota_cell[:, :, 0],
												   rota_cell[:, :, 1]],
										axis=1), axis=1) == 3*radius]

	rota_cell = rota_cell[:, -1, :]
	return rota_cell

def damier_positions(color):
	"""
	Créé une liste de coordonnées de manière à ce que celles-ci forment un
	damier.

	Paramètres
	----------
	color : str
		Indique quelles cases pourront être tirées. Les noires ('k') ou les
		blanches ('w').

	Erreurs
	-------
	ValueError
		La couleur rentrée ne fait pas partie des choix possibles ('w'/'k').

	Retourne
	--------
	positions : numpy.ndarray
		Liste des positions en damier pour l'array Table.
	damier : numpy.ndarray
		Matrice booléenne 2d où les "True" indiquent les positions ciblées.

	"""
	damier = np.zeros((10, 10), dtype=int)
	damier[::2] = 1
	damier = (damier+damier.T)
	if color == "w":
		damier = damier != 1
	elif color == "k":
		damier = damier == 1
	else:
		raise ValueError("color must be 'w' or 'k'.")

	positions = np.argwhere(damier)
	return positions, damier

def random_hit(list_possibles):
	"""
	Fonction pour choisir une position aléatoire dans une liste de cibles
	possibles.

	Parameters
	----------
	list_possibles : list
		Liste des cibles possibles.

	Returns
	-------
	x_ch : int
		Ligne de la cellule choisit.
	y_ch : int
		Colonne de la cellule choisit.


	"""
	xh, yh = list_possibles[np.random.randint(len(list_possibles))]
	return xh, yh

def conseq_fire(what_comp_see, xc, yc, list_ppl, human_table, list_water,
				list_not_sink, list_sinked, dico_human_ships, sh_h_sk_b,
				sm_h_sk_b, fr_h_sk_b, cr_h_sk_b, ac_h_sk_b, human_losts,
				touch_b, sinked_b, verbose=True):
	"""
	Fonction pour mettre à jour l’état des différentes variables après les
	tours de jeu de l’humain et de l’ordinateur.

	Paramètres
	----------
	what_comp_see : numpy.ndarray
		Un tableau 2d, remplit 0 et 1. 0 etant une cellule inexplorée par
		l’ordinateur.
	xc : int
		Position en x du tir.
	yc : int
		Position en y du tir.
	list_ppl : list
		Liste de deux listes de chaînes de caractères. Correspond aux
		valeurs à mettre sur les axes x et y. Provient de la fonction
		create_pos_pl().
	human_table : numpy.ndarray
		Table de jeu de l'humaine avec les couleurs rvb pour indiquer où sont
		les bateaux.
	list_water : list
		Liste des cellules qui ont déjà été explorées et contiennent de
		l'eau.
	list_not_sink : list
		Liste des cellules qui ont déjà été explorées et qui contiennent un
		bateau qui n'a pas encore été coulé.
	list_sinked : list
		Liste des cellules qui ont déjà été explorées et qui contiennent un
		bateau qui a été coulé.
	dico_human_ships : dict
		Dictionnaire humain où l’état des bateaux est enregistré.
	sh_h_sk_b : bool
		Si la navette de l'humain a été coulé, sinon = False.
	sm_h_sk_b : bool
		Si le sous-marin de l'humain a été coulé, sinon = False.
	fr_h_sk_b : bool
		Si la frégate de l'humain a été coulé, sinon = False.
	cr_h_sk_b : bool
		Si le croiseur de l'humain a été coulé, sinon = False.
	ac_h_sk_b : bool
		Si le porte-avion de l'humain a été coulé, sinon = False.
	human_losts : list # seems useless
		Liste des positions où il y avait un bateau humain avant qu’il ne
		soit coulé.
	touch_b : bool
		True si l’ordinateur a touché mais n’a toujours pas coulé le (ou les)
		bateaux touchés. False sinon.
	sinked_b : bool
		Si le(s) bateau(x) humain trouvé a été coulé ou non.
	verbose : bool, optional
		Si la conséquence du tir de l’ordinateur est affichée ou non. La
		valeur par défaut est True.

	Retourne
	--------
	wcs_copy : numpy.ndarray
		Un tableau 2d, remplit 0 et 1. 0 étant une cellule inexplorée par
		l’ordinateur.
	human_dic
		Dictionnaire humain où l’état des bateaux est enregistré mis à jour.
	sh_h_sk_b : bool
		Si la navette de l'humain a été coulé, sinon = False.
	sm_h_sk_b : bool
		Si le sous-marin de l'humain a été coulé, sinon = False.
	fr_h_sk_b : bool
		Si la frégate de l'humain a été coulé, sinon = False.
	cr_h_sk_b : bool
		Si le croiseur de l'humain a été coulé, sinon = False.
	ac_h_sk_b : bool
		Si le porte-avion de l'humain a été coulé, sinon = False.
	h_lost : list # seems useless
		Liste des positions où il y avait un bateau humain avant qu’il ne
		soit coulé mis à jour.
	list_water : list
		Liste des cellules qui ont déjà été explorées et contiennent de
		l'eau.
	list_not_sink : list
		Liste des cellules qui ont déjà été explorées et qui contiennent un
		bateau qui n'a pas encore été coulé.
	list_sinked : list
		Liste des cellules qui ont déjà été explorées et qui contiennent un
		bateau qui a été coulé.
	touch_b : bool
		True si l’ordinateur a touché mais n’a toujours pas coulé le (ou les)
		bateaux touchés. False sinon.
	sinked_b : bool
		Si le(s) bateau(x) humain trouvé a été coulé ou non.

	"""
	wcs_copy = np.copy(what_comp_see)
	l_water = list_water.copy()
	l_notsk = list_not_sink.copy()
	l_sink = list_sinked.copy()
	hum_tbl = np.copy(human_table)
	human_dic = deepcopy(dico_human_ships)
	h_lost = human_losts.copy()
	wcs_copy[xc, yc] = 1
	if verbose:
		print("L'ordinateur tire en " + str(list_ppl[0][xc]) + str(yc) + ".")

	if np.sum(hum_tbl[xc, yc]) != 3:
		touch_b = True
		l_notsk.append([xc, yc])
		for i in list(human_dic.keys()):
			if human_dic[i]['rvb'].tolist() == hum_tbl[xc, yc].tolist():
				human_dic[i]['etat'] -= 1
				break

		if verbose:
			print("Votre " + str(i) + " a été touché.")

		for i in list(human_dic.keys()):
			if human_dic[i]['etat'] == 0:
				h_lost.append(i)
				color_ref_boat = human_dic[i]['rvb'].tolist()
				if verbose:
					print("Votre " + str(i) + " a été coulé.")

				human_dic.pop(i)
				sinked_b = True
				if i == 'Navette':
					sh_h_sk_b = True
				elif i == 'Sous-marin':
					sm_h_sk_b = True
				elif i == 'Frégate':
					fr_h_sk_b = True
				elif i == 'Croiseur':
					cr_h_sk_b = True
				elif i == 'Porte-avion':
					ac_h_sk_b = True

		if sinked_b == True:
			not_sink_temp = l_notsk.copy()
			for i in range(len(l_notsk)):
				if (hum_tbl[not_sink_temp[i][0],
							not_sink_temp[i][1],
							:].tolist() == color_ref_boat):
					l_sink.append(not_sink_temp[i])
					l_notsk.remove(not_sink_temp[i])

				sinked_b = False

			if len(l_notsk) == 0:
				touch_b = False

	else:
		if verbose:
			print("L'ordinateur a tiré dans l'eau.")

		l_water.append([xc, yc])

	return(wcs_copy, human_dic, sh_h_sk_b, sm_h_sk_b, fr_h_sk_b, cr_h_sk_b,
		   ac_h_sk_b, h_lost, l_water, l_notsk, l_sink, touch_b, sinked_b)
