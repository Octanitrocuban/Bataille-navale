# -*- coding: utf-8 -*-
"""
@author: Nougaret Matthieu

This module countain the graphical functions used to plot the game board.

"""
import matplotlib.pyplot as plt
import numpy as np
#=============================================================================
def show_state_ancrage(tablehumain, dicshiphumain, lplaces):
	"""
	This function is used to show the different possibles cells where to put
	a ship.

	Parameters
	----------
	tablehumain : numpy.ndarray
		Human plate with rgb chanel to indicate where are its boats.
	dicshiphumain : dict
		Human dictionary where the state of the human boats is recorded.
	lplaces : list
		List of two list of strings. Values to put at the x and y axis. It
		come from the the function create_pos_pl().

	Returns
	-------
	None.

	"""
	plt.figure(figsize=(8, 8))
	plt.imshow(tablehumain, zorder=1)
	# to have the grid lines and the labes on the axes offset
	plt.xticks(range(10), lplaces[1], fontsize=13)
	plt.yticks(range(10), lplaces[0], fontsize=13)
	for i in np.arange(0.5, 9.5, 1):
		plt.hlines(i, -0.5, 9.5, "k", zorder=2)
		plt.vlines(i, -0.5, 9.5, "k", zorder=2)

	for j in list(dicshiphumain.keys()):
		plt.plot(dicshiphumain[j]['y'][0], dicshiphumain[j]['x'][0],
			   's', color=dicshiphumain[j]['rgb'], label=j)

		plt.legend(loc=(1.01, 0.5))

	plt.show()

def show_state_rotation(table_humain, dic_hum, radius, end_cells, indice_boat,
						lplaces, rempl_ship_hum, position_xy, ship_name):
	"""
	This function is used to show the different possibles rotations for the
	selected ship.

	Parameters
	----------
	table_humain : numpy.ndarray
		Human plate with rgb chanel to indicate where are its boats.
	dic_hum : dict
		Initilized dictionary of the boats.
	radius : int
		Length (in cell) of the boat.
	end_cells : numpy.ndarray
		Numpy ndarray listing the positions at the other end of the boat at
		the i-th rotation.
	indice_boat : int
		Position at which the chosen boat is in list of the boats. It will
		be used to access to the parameters of this boat.
	lplaces : list
		List of two list of strings. Values to put at the x and y axis. It
		come from the the function create_pos_pl().
	rempl_ship_hum : dict
		Human dictionary where the state of the human boats is recorded.
	position_xy : numpy.ndarray
		Positions of the pivot point used for rotation.
	ship_name : str
		Name of the current choosen boat.

	Returns
	-------
	None.

	"""
	plt.figure(figsize=(8*len(end_cells), 9))
	for i in range(len(end_cells)):
		# creating a representation for the possible rotations
		table_hum_2 = np.copy(table_humain)
		# it use the pre computed starting and ending cell to avoid collision
		# with other boat or to get out of the frame
		xh = np.linspace(position_xy[0], end_cells[i, 0], radius+1,
						dtype=int)

		yh = np.linspace(position_xy[1], end_cells[i, 1], radius+1,
						dtype=int)

		table_hum_2[xh, yh, :] = dic_hum['Rgb codes'][indice_boat]

		plt.subplot(1, len(end_cells), i+1)
		plt.title("Rotation n°"+str(i))
		plt.imshow(table_hum_2, zorder=1)
		# plot trick to have a legend with the boat color and name
		plt.plot(yh[0], xh[0], 's', label=ship_name,
				color=dic_hum['Rgb codes'][indice_boat], zorder=2)

		# plot the already placed boats
		for j in list(rempl_ship_hum.keys()):
			plt.plot(rempl_ship_hum[j]['y'][0], rempl_ship_hum[j]['x'][0],
					 's', color=rempl_ship_hum[j]['rgb'], label=j, zorder=2)

		plt.plot(position_xy[1], position_xy[0], "ro",
				 label="Attachment\npoint", zorder=2)

		# to have the grid lines and the labes on the axes offset
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
	Function to show the fight between two bots.

	Parameters
	----------
	table_bot1 : numpy.ndarray
		Plate of the first bot with rgb chanel to indicate where are its
		boats.
	dico_bot1 : dict
		First bot dictionary where the state of the boats is recorded.
	watter_bot1 : list
		List of hit that end in the see made by bot 1.
	notsink_bot1 : list
		List of hit that touch a boat but without sinking it by bot 1.
	sinked_bot1 : list
		List of hit that touch a boat and sinked it by bot 1.
	table_bot2 : numpy.ndarray
		Plate of the second bot with rgb chanel to indicate where are its
		boats.
	dico_bot2 : dict
		Second bot dictionary where the state of the boats is recorded.
	watter_bot2 : list
		List of hit that end in the see made by bot 2.
	notsink_bot2 : list
		List of hit that touch a boat but without sinking it by bot 2.
	sinked_bot2 : list
		List of hit that touch a boat and sinked it by bot 2.
	list_ppl : list
		List of two list of strings. Values to put at the x and y axis. It
		come from the the function create_pos_pl().

	Returns
	-------
	None.

	"""
	plt.figure(figsize=(13, 5))
	plt.subplot(1, 2, 1)
	plt.title("Player 1 plate")
	plt.imshow(table_bot1, zorder=1)
	plt.xticks(range(10), list_ppl[1], fontsize=13)
	plt.yticks(range(10), list_ppl[0], fontsize=13)
	for i in np.arange(0.5, 9.5, 1):
		plt.hlines(i, -0.5, 9.5, "k", zorder=2)
		plt.vlines(i, -0.5, 9.5, "k", zorder=2)

	for j in list(dico_bot1.keys()):
		plt.plot(dico_bot1[j]['y'][0], dico_bot1[j]['x'][0], 's',
				 color=dico_bot1[j]['rgb'], label=j, zorder=2)

	for j in range(len(watter_bot1)):
		plt.plot(watter_bot1[j][1], watter_bot1[j][0], 'bo', zorder=2)

	for j in range(len(notsink_bot1)):
		plt.plot(notsink_bot1[j][1], notsink_bot1[j][0], 'ro', zorder=2)

	for j in range(len(sinked_bot1)):
		plt.plot(sinked_bot1[j][1], sinked_bot1[j][0], 'ko', zorder=2)

	plt.legend(loc=(1.01, 0.5))
	plt.subplot(1, 2, 2)
	plt.title("Player 2 plate")
	plt.imshow(table_bot2, zorder=1)
	plt.xticks(range(10), list_ppl[1], fontsize=13)
	plt.yticks(range(10), list_ppl[0], fontsize=13)
	for i in np.arange(0.5, 9.5, 1):
		plt.hlines(i, -0.5, 9.5, "k", zorder=2)
		plt.vlines(i, -0.5, 9.5, "k", zorder=2)

	for j in list(dico_bot2.keys()):
		plt.plot(dico_bot2[j]['y'][0], dico_bot2[j]['x'][0],
			   's', color=dico_bot2[j]['rgb'], label=j, zorder=2)

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
	Function to show the human and computer grid during the fight. For
	the human grid, there will be:
		-its ship's position as colored cells;
		-the sea in white cells;
		-the legend with the color corresponding to the remaing ships;
		-the positions where the computer hit the sea with blue dots;
		-the positions where the computer hit a baot with red dots;
		-the positions where the computer sinked a baot with dark dots;

	Parameters
	----------
	table_humain : numpy.ndarray
		Human plate with rgb chanel to indicate where are its boats.
	list_ppl : list
		List of two list of strings. Values to put at the x and y axis. It
		come from the the function create_pos_pl().
	human_dico : dict
		Human dictionary where the state of the human boats is recorded.
	ordi_watter : list
		List of hit that end in the see made by computer.
	ordi_notsink : list
		List of hit that touch a boat but without sinking it by computer.
	ordi_sinked : list
		List of hit that touch a boat and sinked it by computer.
	what_human_see : numpy.ndarray
		What human see from its hits. It is a rgb 2d array with: blue cell
		indicate that it is watter, red cell indicate that it is a boat not
		sinked yet and dark cell indicate that it is sinked boat.

	Returns
	-------
	None.

	"""
	plt.figure(figsize=(19, 9))
	plt.subplot(1, 2, 1)
	plt.title("Your plate")
	plt.imshow(table_humain, zorder=1)
	plt.xticks(range(10), list_ppl[1], fontsize=13)
	plt.yticks(range(10), list_ppl[0], fontsize=13)
	for i in np.arange(0.5, 9.5, 1):
		plt.hlines(i, -0.5, 9.5, "k", zorder=2)
		plt.vlines(i, -0.5, 9.5, "k", zorder=2)

	for j in list(human_dico.keys()):
		plt.plot(human_dico[j]['y'][0], human_dico[j]['x'][0],
			   's', color=human_dico[j]['rgb'], label=j)

	for j in range(len(ordi_watter)):
		plt.plot(ordi_watter[j][1], ordi_watter[j][0], 'bo')

	for j in range(len(ordi_notsink)):
		plt.plot(ordi_notsink[j][1], ordi_notsink[j][0], 'ro')

	for j in range(len(ordi_sinked)):
		plt.plot(ordi_sinked[j][1], ordi_sinked[j][0], 'ko')

	plt.legend(loc=(1.01, 0.5))
	plt.subplot(1, 2, 2)
	plt.title("Computer plate")
	plt.imshow(what_human_see, zorder=1)
	plt.xticks(range(10), list_ppl[1], fontsize=13)
	plt.yticks(range(10), list_ppl[0], fontsize=13)
	for i in np.arange(0.5, 9.5, 1):
		plt.hlines(i, -0.5, 9.5, "k", zorder=2)
		plt.vlines(i, -0.5, 9.5, "k", zorder=2)

	plt.show()

def print_victory(victoire, list_sinked, list_water):
	"""
	Function to print the result of a game.

	Parameters
	----------
	victoire : str
		String that indicates who win the match.
	list_sinked : list
		List of the hit that had touch water cell.
	list_water : list
		List of the hit that had touch boat cell.

	Returns
	-------
	int
		Number of hit during the match.

	"""
	if victoire == "null":
		print("Draw")

	elif victoire == "human":
		print("Human victory")
		print("******    ******     ******     *           *    ******* ")
		print("*     *   *     *   *       *    *         *    *       *")
		print("*     *   *     *   *       *     *       *     *       *")
		print("******    ******    *********      *     *      *       *")
		print("*     *   * *       *       *       *   *       *       *")
		print("*     *   *   *     *       *        * *        *       *")
		print("******    *     *   *       *         *          ******* ")
	
	elif victoire == "computer":
		print("Computer victory")

	return len(list_sinked)+len(list_water)

def pretty_dict_print(ship_dico):
	"""
	Function to have a nice print of the state of your boat when placing
	them.

	Parameters
	----------
	ship_dico : dict
		Dictionary where the state of the boats is recorded.

	Returns
	-------
	None.

	"""
	num = ship_dico['Number']
	nam = ship_dico['Type']
	sep = '+'+'-'*18+'+'+'-'*12+'+'+'-'*8+'+'+'-'*8+'+'+'-'*9+'+'+'-'*20+'+'
	print(sep)
	print('|       Type       | Identifier | Length | Number |  Color  |'
		 +'     Rgb codes      |')

	print(sep)
	if 'Aircraft-carrier' in ship_dico['Type']:
		print('| Aircraft-carrier |      0     |   5    |    '
			 +str(num[nam == 'Aircraft-carrier'][0])+'   |  grey   | '
			 +'[0.50, 0.50, 0.50] |')

		print(sep)

	if 'Cruiser' in ship_dico['Type']:
		print('|      Cruiser     |      1     |   4    |    '
			 +str(num[nam == 'Cruiser'][0])+'   | orange  | '
			 +'[1.00, 0.50, 0.00] |')

		print(sep)

	if 'Submarine' in ship_dico['Type']:
		print('|     Submarine    |      2     |   3    |    '
			 +str(num[nam == 'Submarine'][0])+'   |  green  | '
			 +'[0.00, 0.75, 0.00] |')

		print(sep)

	if 'Frigate' in ship_dico['Type']:
		print('|      Frigate     |      3     |   3    |    '
			 +str(num[nam == 'Frigate'][0])+'   | yellow  | '
			 +'[1.00, 0.90, 0.00] |')

		print(sep)

	if 'Shuttle' in ship_dico['Type']:
		print('|      Shuttle     |      4     |   2    |    '
			 +str(num[nam == 'Shuttle'][0])+'   | purple  | '
			 +'[0.75, 0.00, 0.75] |')

		print(sep)
