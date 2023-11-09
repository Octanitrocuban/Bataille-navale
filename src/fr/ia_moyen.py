# -*- coding: utf-8 -*-
"""
@author: Nougaret Matthieu

Module contenant les fonctions spécifiques au bot de difficulté moyen.

"""
import numpy as np
import ia_general as iag
#=============================================================================
def neighbor_search(list_water, list_notsink, list_sinked):
	"""
	Fonction de faire la recherche autour du bateau trouvé pour l'achever.

	Parameters
	----------
	list_water : list
		Liste des positions de cellules qui ont chuté en watter.
	list_notsink : list
		Liste des cellules qui font partie d’un bateau pas encore coulé.
	list_sinked : list
		Liste des positions des cellules qui font partie d’un bateau déjà
		coulé.

	Returns
	-------
	xh : int
		Position en x de la cellule à cibler.
	yh : int
		Position en y de la cellule à cibler.

	"""
	arr_notsink = np.array(list_notsink)
	if len(arr_notsink) >= 2:
		targs = []
		dx = np.unique(np.diff(arr_notsink[:, 0]))
		dy = np.unique(np.diff(arr_notsink[:, 1]))
		if len(dx) == 1:
			if dx[0] == 0:#Vertical alignment:
				mini = np.min(arr_notsink[:, 1])
				maxi = np.max(arr_notsink[:, 1])
				if mini > 0:
					targs.append([arr_notsink[0][0], mini-1])
				if maxi < 9:
					targs.append([arr_notsink[0][0], maxi+1])

		if len(dy) == 1:
			if dy[0] == 0:#Horizontal alignment:
				mini = np.min(arr_notsink[:, 0])
				maxi = np.max(arr_notsink[:, 0])
				if mini > 0:
					targs.append([mini-1, arr_notsink[0][1]])
				if maxi < 9:
					targs.append([maxi+1, arr_notsink[0][1]])

		if len(targs) > 0:
			possib_try = iag.look_loop_pth(targs, list_water, list_notsink,
									   list_sinked)
			if len(possib_try) == 1:
				xh, yh = possib_try[0]
			elif len(possib_try) > 1:
				xh, yh = possib_try[np.random.choice(range(len(possib_try)))]
			elif len(possib_try) < 1:
				xh, yh = iag.look_first_hit(list_water, list_notsink,
											list_sinked)

		else:#security line
			xh, yh = iag.look_first_hit(list_water, list_notsink,
										list_sinked)

	else:#security line
		xh, yh = iag.look_first_hit(list_water, list_notsink, list_sinked)

	return xh, yh
