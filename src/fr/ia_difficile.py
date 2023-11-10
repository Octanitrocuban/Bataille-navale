# -*- coding: utf-8 -*-
"""
@author: Nougaret Matthieu

Module contenant les functions spécifiques au mode de difficulté difficile.

"""
import numpy as np
#=============================================================================
def opening():
	"""
	Cette fonction sert à générer une biblithèque d'ouverture pour le bot
	afin de ne pas avoir à recalculer la pdf à chaque début de jeu.

	Paramètres
	----------
	Aucun

	Retourne
	--------
	open_places : numpy.ndarray
		Liste les differents états qui peuvent être rencontrés au début du
		jeu.
	arbre : numpy.ndarray
		Un vecteur de vecteur qui met en relation les differents états.

	Note
	----
	La bibliothèque d'ouverture ne contient que les huits premiers coups
	possible car un arbre plus profond serait trop long à programmer. Mais
	n'hésitez pas à le compléter par vous même si vous le souhaitez.

	"""
	s_0_1 = np.zeros((10, 10), dtype=int)
	s_1_1 = np.copy(s_0_1)
	s_1_1[4, 4] = 1
	s_1_2 = np.rot90(np.copy(s_1_1), 3)
	s_1_3 = np.rot90(np.copy(s_1_1), 2)
	s_1_4 = np.rot90(np.copy(s_1_1), 1)
	s_2_1 = np.copy(s_1_1)
	s_2_1[5, 5] = 1
	s_2_2 = np.rot90(np.copy(s_2_1), 1)
	s_3_1 = np.copy(s_2_1)
	s_3_1[3, 3] = 1
	s_3_2 = np.rot90(np.copy(s_3_1), 3)
	s_3_3 = np.rot90(np.copy(s_3_1), 2)
	s_3_4 = np.rot90(np.copy(s_3_1), 1)
	s_3_5 = np.copy(s_2_1)
	s_3_5[3, 6] = 1
	s_3_6 = np.rot90(np.copy(s_3_5), 3)
	s_3_7 = np.rot90(np.copy(s_3_5), 2)
	s_3_8 = np.rot90(np.copy(s_3_5), 1)
	s_4_1 = np.copy(s_3_1)
	s_4_1[6, 6] = 1
	s_4_2 = np.rot90(np.copy(s_4_1), 3)
	s_4_3 = np.copy(s_3_5)
	s_4_3[6, 3] = 1
	s_4_4 = np.rot90(np.copy(s_4_3), 1)
	s_5_1 = np.copy(s_4_1)
	s_5_1[2, 6] = 1
	s_5_2 = np.rot90(np.copy(s_5_1), 3)
	s_5_3 = np.rot90(np.copy(s_5_1), 2)
	s_5_4 = np.rot90(np.copy(s_5_1), 1)
	s_5_5 = np.copy(s_4_1)
	s_5_5[3, 7] = 1
	s_5_6 = np.rot90(np.copy(s_5_5), 3)
	s_5_7 = np.rot90(np.copy(s_5_5), 2)
	s_5_8 = np.rot90(np.copy(s_5_5), 1)
	s_5_9 = np.copy(s_4_4)
	s_5_9[2, 6] = 1
	s_510 = np.rot90(np.copy(s_5_9), 3)
	s_511 = np.rot90(np.copy(s_5_9), 2)
	s_512 = np.rot90(np.copy(s_5_9), 1)
	s_513 = np.copy(s_4_4)
	s_513[3, 7] = 1
	s_514 = np.rot90(np.copy(s_513), 3)
	s_515 = np.rot90(np.copy(s_513), 2)
	s_516 = np.rot90(np.copy(s_513), 1)
	s_6_1 = np.copy(s_5_1)
	s_6_1[3, 7] = 1
	s_6_2 = np.rot90(np.copy(s_6_1), 3)
	s_6_3 = np.rot90(np.copy(s_6_1), 2)
	s_6_4 = np.rot90(np.copy(s_6_1), 1)
	s_6_5 = np.copy(s_5_1)
	s_6_5[6, 2] = 1
	s_6_6 = np.rot90(np.copy(s_6_5), 3)
	s_6_7 = np.rot90(np.copy(s_6_5), 2)
	s_6_8 = np.rot90(np.copy(s_6_5), 1)
	s_6_9 = np.copy(s_5_1)
	s_6_9[7, 3] = 1
	s_610 = np.rot90(np.copy(s_6_9), 3)
	s_611 = np.copy(s_5_5)
	s_611[6, 2] = 1
	s_612 = np.rot90(np.copy(s_611), 3)
	s_613 = np.copy(s_5_9)
	s_613[3, 7] = 1
	s_614 = np.rot90(np.copy(s_613), 3)
	s_615 = np.rot90(np.copy(s_613), 2)
	s_616 = np.rot90(np.copy(s_613), 1)
	s_617 = np.copy(s_5_9)
	s_617[6, 2] = 1
	s_618 = np.rot90(np.copy(s_617), 3)
	s_619 = np.rot90(np.copy(s_617), 2)
	s_620 = np.rot90(np.copy(s_617), 1)
	s_621 = np.copy(s_5_9)
	s_621[7, 3] = 1
	s_622 = np.rot90(np.copy(s_621), 3)
	s_623 = np.copy(s_513)
	s_623[6, 2] = 1
	s_624 = np.rot90(np.copy(s_623), 3)
	s_7_1 = np.copy(s_6_1)
	s_7_1[6, 2] = 1
	s_7_2 = np.rot90(np.copy(s_7_1), 3)
	s_7_3 = np.rot90(np.copy(s_7_1), 2)
	s_7_4 = np.rot90(np.copy(s_7_1), 1)
	s_7_5 = np.copy(s_6_1)
	s_7_5[7, 3] = 1
	s_7_6 = np.rot90(np.copy(s_7_5), 3)
	s_7_7 = np.rot90(np.copy(s_7_5), 2)
	s_7_8 = np.rot90(np.copy(s_7_5), 1)
	s_7_9 = np.copy(s_613)
	s_7_9[6, 2] = 1
	s_710 = np.rot90(np.copy(s_7_9), 3)
	s_711 = np.rot90(np.copy(s_7_9), 2)
	s_712 = np.rot90(np.copy(s_7_9), 1)
	s_713 = np.copy(s_613)
	s_713[7, 3] = 1
	s_714 = np.rot90(np.copy(s_713), 3)
	s_715 = np.rot90(np.copy(s_713), 2)
	s_716 = np.rot90(np.copy(s_713), 1)
	s_8_1 = np.copy(s_7_1)
	s_8_1[7, 3] = 1
	s_8_2 = np.rot90(np.copy(s_8_1), 3)
	s_8_3 = np.copy(s_7_9)
	s_8_3[7, 3] = 1
	s_8_4 = np.rot90(np.copy(s_8_3), 3)
	open_places = np.array([s_0_1, s_1_1, s_1_2, s_1_3, s_1_4, s_2_1, s_2_2,
							s_3_1, s_3_2, s_3_3, s_3_4, s_3_5, s_3_6, s_3_7,
							s_3_8, s_4_1, s_4_2, s_4_3, s_4_4, s_5_1, s_5_2,
							s_5_3, s_5_4, s_5_5, s_5_6, s_5_7, s_5_8, s_5_9,
							s_510, s_511, s_512, s_513, s_514, s_515, s_516,
							s_6_1, s_6_2, s_6_3, s_6_4, s_6_5, s_6_6, s_6_7,
							s_6_8, s_6_9, s_610, s_611, s_612, s_613, s_614,
							s_615, s_616, s_617, s_618, s_619, s_620, s_621,
							s_622, s_623, s_624, s_7_1, s_7_2, s_7_3, s_7_4,
							s_7_5, s_7_6, s_7_7, s_7_8, s_7_9, s_710, s_711,
							s_712, s_713, s_714, s_715, s_716, s_8_1, s_8_2,
							s_8_3, s_8_4])

	arbre = np.array([np.array([1, 2, 3, 4]), np.array([5]), np.array([6]),
					  np.array([5]), np.array([6]), np.array([7, 9, 11, 13]),
					  np.array([8, 10, 12, 14]), np.array([15]),
					  np.array([16]), np.array([15]), np.array([16]),
					  np.array([17]), np.array([18]), np.array([17]),
					  np.array([18]), np.array([19, 21, 23, 25]),
					  np.array([20, 22, 24, 26]), np.array([28, 30, 32, 34]),
					  np.array([27, 29, 31, 33]),
					  np.array([35, 39, 43]), np.array([36, 40, 44]),
					  np.array([37, 41, 43]), np.array([38, 42, 44]),
					  np.array([35, 41, 45]), np.array([36, 42, 46]),
					  np.array([37, 39, 45]), np.array([38, 40, 46]),
					  np.array([47, 51, 55]), np.array([48, 52, 56]),
					  np.array([49, 51, 53]), np.array([50, 54, 56]),
					  np.array([47, 53, 57]), np.array([48, 54, 58]),
					  np.array([49, 51, 57]), np.array([50, 52, 58]),
					  np.array([59, 63]), np.array([60, 64]),
					  np.array([61, 65]), np.array([62, 66]),
					  np.array([59, 65]), np.array([60, 66]),
					  np.array([61, 63]), np.array([62, 64]),
					  np.array([63, 65]), np.array([64, 66]),
					  np.array([59, 61]), np.array([60, 62]),
					  np.array([67, 71]), np.array([68, 72]),
					  np.array([69, 73]), np.array([70, 74]),
					  np.array([67, 73]), np.array([68, 74]),
					  np.array([69, 71]), np.array([70, 72]),
					  np.array([71, 73]), np.array([72, 74]),
					  np.array([67, 69]), np.array([68, 70]),
					  np.array([75]), np.array([76]), np.array([75]),
					  np.array([76]), np.array([75]), np.array([76]),
					  np.array([75]), np.array([76]), np.array([77]),
					  np.array([78]), np.array([77]), np.array([78]),
					  np.array([77]), np.array([78]), np.array([77]),
					  np.array([78])], dtype=object)
	return open_places, arbre

def map_one_boat(plateau, ray):
	"""
	Cette fonction sers a calculé la fonction de densité de probabilité
	de la répartition d’un navire sur une carte donnée.

	Paramètres
	----------
	plateau : numpy.ndarray
		Un tableau 2d, remplit 0 et 1. 0 etant une cellule inexplorée par
		l’ordinateur.
	ray : int
		Longueur du bateau.

	Retourne
	--------
	proba : numpy.ndarray
		Tableau numpy carré 2d, où les valeurs de cellules comptent le
		nombre de fois qu’un bateau peut être placé sur celle-ci.
		

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
	if ray == 5:
		kernel = kpa
	elif ray == 4:
		kernel = kcr
	elif ray == 3:
		kernel = ksm
	elif ray == 2:
		kernel = knv

	proba = np.zeros((10, 10))
	places_0 = np.argwhere(plateau == 0)
	lk0 = places_0[:, np.newaxis, np.newaxis]+kernel
	# une méthode de concaténation plus rapide
	empty = np.empty((lk0.shape[0]*lk0.shape[1], lk0.shape[2], 2), dtype=int)
	empty[:, :, 0] = np.reshape(lk0[:, :, :, 0],
						(lk0.shape[0]*lk0.shape[1], lk0.shape[2]))

	empty[:, :, 1] = np.reshape(lk0[:, :, :, 1],
						(lk0.shape[0]*lk0.shape[1], lk0.shape[2]))

	lk0 = empty[np.sum((empty[:, :, 0] <= 9)&(empty[:, :, 1] <= 9)&(
						empty[:, :, 0] >= 0)&(empty[:, :, 1] >= 0),
					 	axis=1) == ray]

	lk0 = lk0[np.sum(plateau[empty[:, :, 0], empty[:, :, 1]], axis=1) == 0]
	empty = np.empty((lk0.shape[0]*lk0.shape[1], 2), dtype=int)
	empty[:, 0] = np.ravel(lk0[:, :, 0])
	empty[:, 1] = np.ravel(lk0[:, :, 1])
	p, c = np.unique(empty, axis=0, return_counts=True)
	proba[p[:, 0], p[:, 1]] = c
	return proba

def approx_density(plateau, navette_sinked, fregate_sinked,
				  submarine_sinked, cruiser_sinked, airporter_sinked):
	"""
	Cette fonction est utilisée pour calculer la fonction de densité
	de probabilité de la répartition possible du navire sur une
	carte donnée.

	Paramètres
	----------
	plateau : numpy.ndarray
		Un tableau 2d, remplit 0 et 1. 0 etant une cellule inexplorée par
		l’ordinateur.
	navette_sinked : bool
		Indique si la navette a été coulé ou non.
	fregate_sinked : bool
		Indique si le sous-marin a été coulé ou non.
	submarine_sinked : bool
		Indique si la fregatte a été coulé ou non.
	cruiser_sinked : bool
		Indique si le croiseur a été coulé ou non.
	airporter_sinked : bool
		Indique si le porte-avion a été coulé ou non.

	Retourne
	--------
	array_pdf : numpy.ndarray
		Un tableau 2d. Il a une forme de (n, 3). n étant le nombre de
		cellules sur lesquelles une partie d’un navire peut être. 3 étant
		(x, y, densité de probabilité pour cette cellule).

	Note
	----
	Cette fonction ne calcule qu’une approximation de la vraie carte pdf qui
	est non calculable avec la puissance et la mémoire moyennes de
	l’ordinateur.

	"""
	pdf = np.zeros((10, 10), dtype=int)
	if navette_sinked == False:
		pdf = pdf+map_one_boat(plateau, 2)
	if fregate_sinked == False:
		pdf = pdf+map_one_boat(plateau, 3)
	if submarine_sinked == False:
		pdf = pdf+map_one_boat(plateau, 3)
	if cruiser_sinked == False:
		pdf = pdf+map_one_boat(plateau, 4)
	if airporter_sinked == False:
		pdf = pdf+map_one_boat(plateau, 5)

	kept = np.argwhere(pdf > 0)
	array_pdf = np.zeros((len(kept), 3), dtype=object)
	array_pdf[:, 0] = kept[:, 0]
	array_pdf[:, 1] = kept[:, 1]
	array_pdf[:, 2] = pdf[kept[:,0], kept[:,1]]
	return array_pdf

def inner(damier_array, list_keep):
	"""
	Fonction pour sélectionner les positions de list_keep qui sont sur des
	cellules valant 0 dans le damier fournit.

	Paramètres
	----------
	damier_array : numpy.ndarray
		Un tableau 2d quadrillé avec des valeurs 0-1.
	list_keep : numpy.ndarray
		Tableau listant les cellules qui peuvent être touchées.

	Retourne
	--------
	union : numpy.ndarray
		Un numpy array qui liste les positions list_keep qui tombent sur
		une cellules valant 0 dans le damier.

	"""
	values = damier_array[list_keep[:, 0], list_keep[:, 1]]
	union = list_keep[values]
	return union

def choice_appx_dens_map(plateau, shuttle_sk, submarine_sk, fregate_sk,
						 cruiser_sk, airpoter_sk, list_water,
						 list_notsink, list_sinked, open_tree, open_tables,
						 damier=None, use_damier=False):
	"""
	Cette fonction est utiliser pour déterminer quelle cellule doit être
	ciblée.

	Paramètres
	----------
	plateau : numpy.ndarray
		Tableau 2d avec la forme (10, 10). Ses valeurs indiquent si
		chaque cellule était déjà touchée (== 1.).
	shuttle_sk : bool
		Indique si la navette (2 cellules de long) a été coulé.
	submarine_sk : bool
		Indique si le sous-marin (3 cellules de long) a été coulé.
	fregate_sk : bool
		Indique si la frégate (3 cellules de long) a été coulé.
	cruiser_sk : bool
		Indique si le croiseur (4 cellules de long) a été coulé.
	airpoter_sk : bool
		Indique si le porte-avions (5 cellules de long) a coulé.
	list_water : list
		Liste des positions de cellules qui sont de l'eau.
	list_notsink : list
		Liste des cellules qui font partie d’un bateau pas encore coulé.
	list_sinked : list
		Liste des positions des cellules qui font partie d’un bateau déjà
		coulé.
	damier : numpy.ndarray, optional
		Matrice booléenne 2d où les "True" indiquent les positions ciblées.
	use_damier : bool, optional
		Indique s'il faut utiliser le filtre en damier sur les positions.
		La valeur par défaut est False.

	Raises
	------
	TypeError
		damier ne doit pas être de type NoneType lorsque use_damier
		est True.

	Retourne
	--------
	xh : int
		Position en x de la cellule à cibler.
	yh : int
		Position en y de la cellule à cibler.

	"""
	if (len(list_water) < 8)&(len(list_notsink) == 0)&(
				len(list_sinked) == 0):
		proba = np.zeros((10, 10))
		current = np.sum(np.sum(open_tables == plateau, axis=1),
						 axis=1) == 100
		branch = open_tree[current[:-4]][0]
		next_one = open_tables[branch[np.random.randint(0,
											len(branch))]]
		xh, yh = np.argwhere((next_one - plateau) == 1)[0]
		return xh, yh

	else:
		dens_map_positions = approx_density(plateau, shuttle_sk,
											submarine_sk, fregate_sk,
											cruiser_sk, airpoter_sk)

		if use_damier:
			if type(damier) != type(None):
				conj = inner(damier, dens_map_positions)
			else:
				raise TypeError(
	'"damier" ne doit pas être un NoneType lorsque use_damier est True.')

		else:
			conj = dens_map_positions

		idx = np.argmax(conj[:, 2])
		xh, yh = conj[idx, :-1].astype(int)
		return xh, yh

def sink_proba_map(table, kernel, rayon):
	"""
	Fonction pour calculer la carte de probabilité par bateau.

	Paramètres
	----------
	table : numpy.ndarray
		Matrice 2d représentant l'état du plateau humain pour l'ordinateur.
		0 = cellules non explrées, 1 = cellules contenant de l'eau ou un
		bateau coulé, 2 = cellules contenant un bateau non coulé.
	kernel : numpy.ndarray
		Noyau pour simuler les cellules recouverte par le bateau.
	rayon : int
		Longueur du bateau.

	Retourne
	--------
	proba : numpy.ndarray
		Tableau de probabilité des cellules sur la possible présence d'un
		bateau.

	"""
	proba = np.zeros((10, 10))
	places = np.argwhere(table == 2)
	places = np.concatenate((places[:, np.newaxis, np.newaxis]+kernel))
	places = places[np.sum((places[:, :, 0] <= 9)&(
							places[:, :, 1] <= 9)&(
							places[:, :, 0] >= 0)&(
							places[:, :, 1] >= 0),
							axis=1) == rayon]

	places = places[np.sum(table[places[:, :, 0],
								 places[:, :, 1]] == 1, axis=1) == 0]

	comptage = np.ravel(np.sum(table[places[:, :, 0],
									 places[:, :, 1]] == 2,
							   axis=1)[:, np.newaxis]+
						np.zeros((len(places), rayon)))

	empty = np.empty((places.shape[0]*places.shape[1], 2), dtype=int)
	empty[:, 0] = np.ravel(places[:, :, 0])
	empty[:, 1] = np.ravel(places[:, :, 1])
	posi, index, compte = np.unique(empty, axis=0, return_counts=True,
									return_index=True)
	proba[posi[:, 0], posi[:, 1]] = compte*comptage[index]
	return proba

def proba_sinker(what_computer_see, list_notsink, shuttle_sk, submarine_sk,
				 fregate_sk, cruiser_sk, airpoter_sk):
	"""
	Fonction pour calculer la carte de probabilité pour chaque bateau
	restant sur la carte.

	Paramètres
	----------
	what_computer_see : numpy.ndarray
		Matrice 2d représentant l'état du plateau humain pour l'ordinateur.
		0 = cellules non explrées, 1 = cellules contenant de l'eau ou un
		bateau coulé, 2 = cellules contenant un bateau non coulé.
	list_notsink : list
		Liste des cellules qui font partie d’un bateau pas encore coulé.
	shuttle_sk : bool
		Indique si la navette (2 cellules de long) a été coulé.
	submarine_sk : bool
		Indique si le sous-marin (3 cellules de long) a été coulé.
	fregate_sk : bool
		Indique si la frégate (3 cellules de long) a été coulé.
	cruiser_sk : bool
		Indique si le croiseur (4 cellules de long) a été coulé.
	airpoter_sk : bool
		Indique si le porte-avions (5 cellules de long) a coulé.

	Retourne
	--------
	xh : int
		Position en x de la cellule à cibler.
	yh : int
		Position en y de la cellule à cibler.

	"""
	kpa = np.array([[[ 0,  0], [ 0,  1], [ 0,  2], [ 0,  3], [ 0,  4]],
					[[ 0, -1], [ 0,  0], [ 0,  1], [ 0,  2], [ 0,  3]],
					[[ 0, -2], [ 0, -1], [ 0,  0], [ 0,  1], [ 0,  2]],
					[[ 0,  0], [ 1,  0], [ 2,  0], [ 3,  0], [ 4,  0]],
					[[-1,  0], [ 0,  0], [ 1,  0], [ 2,  0], [ 3,  0]],
					[[-2,  0], [-1,  0], [ 0,  0], [ 1,  0], [ 2,  0]],
					[[ 0,  0], [ 0, -1], [ 0, -2], [ 0, -3], [ 0, -4]],
					[[ 0,  1], [ 0,  0], [ 0, -1], [ 0, -2], [ 0, -3]],
					[[ 0,  2], [ 0,  1], [ 0,  0], [ 0, -1], [ 0, -2]],
					[[ 0,  0], [-1,  0], [-2,  0], [-3,  0], [-4,  0]],
					[[ 1,  0], [ 0,  0], [-1,  0], [-2,  0], [-3,  0]],
					[[ 2,  0], [ 1,  0], [ 0,  0], [-1,  0], [-2,  0]]],
					dtype=int)

	kcr = np.array([[[ 0,  0], [ 0,  1], [ 0,  2], [ 0,  3]],
					[[ 0, -1], [ 0,  0], [ 0,  1], [ 0,  2]],
					[[ 0,  0], [ 1,  0], [ 2,  0], [ 3,  0]],
					[[-1,  0], [ 0,  0], [ 1,  0], [ 2,  0]],
					[[ 0,  0], [ 0, -1], [ 0, -2], [ 0, -3]],
					[[ 0,  1], [ 0,  0], [ 0, -1], [ 0, -2]],
					[[ 0,  0], [-1,  0], [-2,  0], [-3,  0]],
					[[ 1,  0], [ 0,  0], [-1,  0], [-2,  0]]], dtype=int)

	ksm = np.array([[[ 0,  0], [ 0,  1], [ 0,  2]],
					[[ 0, -1], [ 0,  0], [ 0,  1]],
					[[ 0,  0], [ 1,  0], [ 2,  0]],
					[[-1,  0], [ 0,  0], [ 1,  0]],
					[[ 0,  0], [ 0, -1], [ 0, -2]],
					[[ 0,  0], [-1,  0], [-2,  0]]], dtype=int)


	knv = np.array([[[ 0,  0], [ 0,  1]], [[ 0,  0], [ 1,  0]], [[ 0,  0],
					[ 0, -1]], [[ 0,  0], [-1,  0]]], dtype=int)

	map_see_copy = np.copy(what_computer_see)
	arr_not_sink = np.array(list_notsink)
	proba = np.zeros((10, 10))
	map_see_copy[arr_not_sink[:, 0], arr_not_sink[:, 1]] = 2
	if shuttle_sk == False:
		proba = proba + sink_proba_map(map_see_copy, knv, 2)
	if submarine_sk == False:
		proba = proba + sink_proba_map(map_see_copy, ksm, 3)
	if fregate_sk == False:
		proba = proba + sink_proba_map(map_see_copy, ksm, 3)
	if cruiser_sk == False:
		proba = proba + sink_proba_map(map_see_copy, kcr, 4)
	if airpoter_sk == False:
		proba = proba + sink_proba_map(map_see_copy, kpa, 5)

	proba[what_computer_see != 0] = 0
	posi = np.argwhere(proba == np.max(proba))
	if len(posi) == 1:
		xh, yh = posi[0]
		return xh, yh

	else:
		xh, yh = posi[np.random.randint(len(posi))]
		return xh, yh
