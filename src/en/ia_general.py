# -*- coding: utf-8 -*-
"""
Module containing general functions.
"""
import numpy as np
from copy import deepcopy
#=============================================================================
def create_possible_places():
	"""
	Function to create two list containing the possibles positions on the
	plate.

	Returns
	-------
	axes : list
		List of 2 list witch contain the name of the lines and columns.
	poss_places : list
		List of string. They correspond to all of the possible combination
		of position when the human put them in command line:
		(['A0', 'A1', ..., '8J', '9J']).

	"""
	axes = [list("ABCDEFGHIJ"), list("0123456789")]
	poss_1 = np.sort(axes[0]*10).astype(object)+np.array(axes[1]*10,
														 dtype=object)

	poss_2 = np.sort(axes[1]*10).astype(object)+np.array(axes[0]*10,
														 dtype=object)

	poss_places = np.concatenate((poss_1, poss_2)).tolist()
	return axes, poss_places

def random_positiong_ships(ships_dico, computer_table=None, navig_ordi=None):
	"""
	Function to randomly fill a plate with the boats.

	Parameters
	----------
	ships_dico : dictionary
		Dictionary of the ships :
			Boats = {
				'Type':np.array(['Aircraft-carrier', 'Cruiser', 'Submarine',
								 'Frigate', 'Shuttle']),
				'Length': np.array([5, 4, 3, 3, 2]),
				'Number': np.array([1, 1, 1, 1, 1]),
				'Color': np.array(['grey', 'orange', 'green', 'yellow',
								   'purple']),
				'Rgb codes':np.array([[0.50, 0.50, 0.50], [1.00, 0.50, 0.00],
									  [0.00, 0.75, 0.00], [1.00, 0.90, 0.00],
									  [0.75, 0.00, 0.75]])}

	Returns
	-------
	navig_ordi : dictionary
		Dictionary descripting all ship state.
	computer_table : np.ndarray
		3 dimensions np.array, it record the ships positions through their
		rgb code value.

	Example
	-------
	In [0] : random_positiong_ships(Boats)
	Out [0]: ({'Shuttle':{'x':array([2, 3]), 'y':array([7, 7]),
			   'Color':'purple', 'rgb':array([0.75, 0., 0.75])},
			   'Submarine':{'x':array([2, 2, 2]), 'y': array([2, 1, 0]),
			   'Color':'green', 'rgb':array([0., 0.75, 0.])},
			   'Aircraft-carrier':{'x':array([1, 1, 1, 1, 1]),
			   'y':array([8, 7, 6, 5, 4]), 'Color':'grey',
			   'rgb':array([0.5, 0.5, 0.5])},
			   'Cruiser':{'x':array([6, 6, 6, 6]), 'y':array([1, 2, 3, 4]),
			   'Color':'orange', 'rgb':array([1., 0.5, 0.])},
			   'Frigate':{'x':array([2, 2, 2]), 'y':array([3, 4, 5]),
			   'Color':'yellow', 'rgb':array([1., 0.9, 0.])}},
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

	for i in range(np.sum(copy_dico['Number'] > 0)):
		ship = np.random.choice(
				copy_dico['Type'][copy_dico['Number'] > 0], 1)[0]

		id_type = np.where(copy_dico['Type'] == ship)[0][0]
		ancres = np.argwhere((computer_table[:, :, 0] == 1)&(
							  computer_table[:, :, 1] == 1)&(
							  computer_table[:, :, 2] == 1))

		ray = copy_dico['Length'][id_type]
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
		navig_ordi[ship]['Color'] = copy_dico['Color'][id_type]
		navig_ordi[ship]['rgb'] = copy_dico['Rgb codes'][id_type]
		computer_table[choice[:, 0], choice[:, 1]] = navig_ordi[ship]['rgb']
		copy_dico['Number'][id_type] -= 1

	return navig_ordi, computer_table

def look_loop_pth(possib_try, water, notsink, sinked):
	"""
	Function to remove cells that were already explored.

	Parameters
	----------
	possib_try : list
		List of cells position.
	water : list
		List of cell position that are watter cell.
	notsink : list
		List of cell position that are part of a still not sinked boat.
	sinked : list
		List of cell position that are part of an already sinked boat.

	Returns
	-------
	possib_try_2 : list
		List of cell position that could be part of the ship that is already
		touch but not sinked yet.

	"""
	not_in = water+notsink+sinked
	possib_try_2 = []
	for i in range(len(possib_try)):
		if possib_try[i] not in not_in:
			possib_try_2.append(possib_try[i])

	return possib_try_2

def look_first_hit(water, notsink, sinked):
	"""
	Function to choose a surrounding cell to those that contain a
	unsunk boat.

	Parameters
	----------
	possib_try : numpy.ndarray
		Liste de position de cellules.
	water : list
		List of cell position that are watter cell.
	notsink : list
		List of cell position that are part of a still not sinked boat.
	sinked : list
		List of cell position that are part of an already sinked boat.

	Returns
	-------
	x_ch : int
		Cell line chooses.
	y_ch : int
		Column of the cell chooses.

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
	Function to extract the positions at the other end of the boat at the
	i-th rotation.

	Parameters
	----------
	radius : int
		Length of the chosen boat.
	xy : numpy.ndarray
		Positions of the pivot point used for rotation.
	play_table : numpy.ndarray
		 Game board where the colors indicate where the boats are.

	Returns
	-------
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
	Created a list of coordinates so that they form a checkerboard.

	Parameters
	----------
	color : str
		Indicates which squares can be drawn. Black ('k') or white ('w').

	Raises
	------
	ValueError
		The color returned is not part of the possible choices ('w'/'k').

	Returns
	-------
	positions : numpy.ndarray
		List of checkered positions according to the color requested.
	damier : numpy.ndarray
		2d boolean matrix where the True indicate the targeted positions.

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
	Function to choose a random position from a list of possible target.

	Parameters
	----------
	list_possibles : list
		list of possible cell target.

	Returns
	-------
	x_ch : int
		Cell line chooses.
	y_ch : int
		Column of the cell chooses.


	"""
	xh, yh = list_possibles[np.random.randint(len(list_possibles))]
	return xh, yh

def conseq_fire(what_comp_see, xc, yc, list_ppl, human_table, list_water,
				list_not_sink, list_sinked, dico_human_ships, sh_h_sk_b,
				sm_h_sk_b, fr_h_sk_b, cr_h_sk_b, ac_h_sk_b, human_losts,
				touch_b, sinked_b, verbose=True):
	"""
	Function to update the state of the differents variables after the human
	and the computer plays.

	Parameters
	----------
	what_comp_see : numpy.ndarray
		A 0 and 1 values 2d array. 0 beeing unexplored cell for the computer.
	xc : int
		x position of the hit.
	yc : int
		y position of the hit.
	list_ppl : list
		List of two list of strings. Values to put at the x and y axis. It
		come from the the function create_pos_pl().
	human_table : numpy.ndarray
		Human plate with rgb chanel to indicate where are its boats.
	list_water : list
		List of cell that have been already try and are water.
	list_not_sink : list
		List of cell that have been already try and are not sinked yet boat.
	list_sinked : list
		List of cell that have been already try and are sinked boat.
	dico_human_ships : dict
		Dictionary descripting all ship state of the human.
	sh_h_sk_b : bool
		If shuttle of the human was sinked, else = False.
	sm_h_sk_b : bool
		If submarine of the human was sinked, else = False.
	fr_h_sk_b : bool
		If fregatte of the human was sinked, else = False.
	cr_h_sk_b : bool
		If cruiser of the human was sinked, else = False.
	ac_h_sk_b : bool
		If aircraft carrier of the human was sinked, else = False.
	human_losts : list # seems useless
		List of position where there was a human boat before it was sunk.
	touch_b : bool
		True if the computer have touch but still not sunk one (or more)
		human boat. False else.
	sinked_b : bool
		If the found(s) human boat was sunk or not.
	verbose : bool, optional
		If the consequence of the computer shot is printed or not. The
		default is True.

	Returns
	-------
	wcs_copy : numpy.ndarray
		A 0 and 1 values 2d array. 0 beeing unexplored cell for the computer.
	human_dic
		Updated dictionary descripting all ship state of the human.
	sh_h_sk_b : bool
		If shuttle of the human was sinked, else = False.
	sm_h_sk_b : bool
		If submarine of the human was sinked, else = False.
	fr_h_sk_b : bool
		If fregatte of the human was sinked, else = False.
	cr_h_sk_b : bool
		If cruiser of the human was sinked, else = False.
	ac_h_sk_b : bool
		If aircraft carrier of the human was sinked, else = False.
	h_lost : list # seems useless
		Updated list of position where there was a human boat befaore it was
		sunk.
	l_water : list
		Updated list of cells that have been already try and are water.
	l_notsk : list
		Updated list of cells that have been already try and are not sinked
		yet boat.
	l_sink : list
		Updated list of cells that have been already try and are sinked boat.
	touch_b : bool
		True if the computer have touch but still not sunk one (or more)
		human boat. False else.
	sinked_b : bool
		If the found(s) human boat was sunk or not.

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
		print("Computer fires in "+str(list_ppl[0][xc])+str(yc)+".")

	if np.sum(hum_tbl[xc, yc]) != 3:
		touch_b = True
		l_notsk.append([xc, yc])
		for i in list(human_dic.keys()):
			if human_dic[i]['rgb'].tolist() == hum_tbl[xc, yc].tolist():
				human_dic[i]['state'] -= 1
				break

		if verbose:
			print("Your " + str(i) + " was shot.")

		for i in list(human_dic.keys()):
			if human_dic[i]['state'] == 0:
				h_lost.append(i)
				color_ref_boat = human_dic[i]['rgb'].tolist()
				if verbose:
					print("Your " + str(i) + " was sunk.")

				human_dic.pop(i)
				sinked_b = True
				if i == 'Shuttle':
					sh_h_sk_b = True
				elif i == 'Submarine':
					sm_h_sk_b = True
				elif i == 'Frigate':
					fr_h_sk_b = True
				elif i == 'Cruiser':
					cr_h_sk_b = True
				elif i == 'Aircraft-carrier':
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
			print("Computer shot into the water.")

		l_water.append([xc, yc])

	return(wcs_copy, human_dic, sh_h_sk_b, sm_h_sk_b, fr_h_sk_b, cr_h_sk_b,
		   ac_h_sk_b, h_lost, l_water, l_notsk, l_sink, touch_b, sinked_b)
