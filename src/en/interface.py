# -*- coding: utf-8 -*-
"""
Module for the human actions.
"""
import numpy as np
from copy import deepcopy
import graphics as graphs
import ia_general as iag
#=============================================================================
def placing_human_boats(dico_ships, list_plcs, all_posi_pos_liLst,
						short_boat_call, shortcall_yes, shortcall_no):
	"""
	Function with witch the human will place its boats.

	Parameters
	----------
	dico_ships : dict
		Initilized dictionary of the boats.
	list_plcs : list
		List of two list of strings. Values to put at the x and y axis. It
		come from the the function create_pos_pl().
	all_posi_pos_liLst : list
		List of string. They correspond to all of the possible combination
		of position when the human put them in command line:
		(['A0', 'A1', ..., '8J', '9J']).
	short_boat_call : dict
		Dictionary containing shortcut call name for the boats.
	shortcall_yes : dict
		Dictionary containing shortcut call name for agreement expressions.
	shortcall_no : dict
		Dictionary containing shortcut call name for disagreement
		expressions.

	Returns
	-------
	human_table : numpy.ndarray
		Human plate with rvb chanel to indicate where are its boats.
	human_dico : dict
		Dictionary descripting all ship state of the human.

	"""
	dico_ships_copy  = deepcopy(dico_ships)
	human_table = np.ones((10, 10, 3), dtype=float)
	ok_boat_h = False
	human_dico = {}
	while ok_boat_h != True:
		ok_type_boat = False
		ok_position = False
		while ok_type_boat != True:
			print("")
			print("Please choose a type of boat to place it.\n"
				 + "Enter the name (Type) or the vessel identifier.\n"
				 + "You can also use the command: 'random' at any time to "
				 + "automatically webbed the remaining\nboats randomly. You "
				 + "will still be able to change the positions and "
				 + "rotations of ships\nplaced in this way.")

			graphs.pretty_dict_print(dico_ships_copy)
			ships_type = input("=>")
			if ships_type in list(short_boat_call.keys()):
				ships_type = short_boat_call[ships_type]

			if ships_type in dico_ships_copy['Type'].tolist():
				id_type = np.where(
							dico_ships_copy['Type'] == ships_type)[0][0]

				numb_rest = dico_ships_copy['Number'][id_type]
				if numb_rest < 1:
					print("There are no more boats of this type available,"
						 +" please try again with another type.")

				else:
					dico_ships_copy['Number'][id_type] -= 1
					ok_type_boat = True

			elif ships_type == 'random':
				human_dico, human_table = iag.random_positiong_ships(
											dico_ships_copy, human_table,
											human_dico)

				dico_ships_copy['Number'][:] = 0
				ok_type_boat = True
				ok_position = True

			else:
				print(ships_type, 'is not a possible type of boat. Please'
					 +' try again.')

		while ok_position != True:
			ok_acc = False
			while ok_acc != True:
				print("Please choose a box of acroche to place the ship "
					  + ships_type + " on the game board.\nTo do this, "
					  + "enter a letter in the interval [A, J] for the "
					  + "line and a number in the interval [0, 9] for the"
					  + " column.")

				graphs.show_state_ancrage(human_table, human_dico, list_plcs)
				ancre = input("=>").upper()
				place_xy = np.zeros(2, dtype=int)
				if ancre not in all_posi_pos_liLst:
					print(str(ancre) + " is not present on the tray. "
						 + "Please try again.")

				else:
					if ancre[0] in list_plcs[0]:
						place_xy[0] = np.where(
									np.array(list_plcs[0]) == ancre[0])[0]

						place_xy[1] = int(ancre[1])

					else:
						place_xy[1] = int(ancre[0])
						place_xy[0] = np.where(
									np.array(list_plcs[0]) == ancre[1])[0]

					rayon = dico_ships_copy['Length'][
								dico_ships_copy['Type'] == ships_type][0]

					end_close = iag.look_end_cell(rayon, place_xy,
												  human_table)
					if len(end_close) == 0:
						print("There is no configuration possible for this"
							 +" boat with this acroche box. Please choose"
							 +" another box.")

					else:
						ok_acc = True

			ok_rota = False
			while ok_rota != True:
				print("Please select one of the possible rotations.\nTo do"
					 +" this, enter the integer corresponding to the "
					 +"desired case represented in the following table(s)."
					 +"\nIf you wish to change the acroche box, enter: "
					 +"'back hook'.")

				graphs.show_state_rotation(human_table, dico_ships_copy,
											rayon, end_close, id_type,
											list_plcs, human_dico, place_xy,
											ships_type)

				ch_rotation = input("=>")
				try:
					ch_rotation = int(ch_rotation)
					if (ch_rotation < 0)|(ch_rotation >= len(end_close)):
						print(str(ch_rotation) + "is not part of the "
							 +"possible rotations")

					else:
						xrt = np.linspace(place_xy[0],
										  end_close[ch_rotation, 0],
										  rayon, dtype=int)

						yrt = np.linspace(place_xy[1],
										  end_close[ch_rotation, 1],
										  rayon, dtype=int)

						human_dico[ships_type] = {}
						human_dico[ships_type]['x'] = xrt
						human_dico[ships_type]['y'] = yrt
						human_dico[ships_type]['Color'] = dico_ships_copy[
														  'Color'][id_type]

						human_dico[ships_type]['rgb'] = dico_ships_copy[
														'Rgb codes'][id_type]

						human_table[xrt, yrt] = human_dico[ships_type]['rgb']
						ok_position = True
						ok_rota = True

				except:
					if ch_rotation == 'back hook':
						ok_rota = True
					else:
						print(str(ch_rotation) + " is not convertible into"
							 + " an integer, please try again")

		if np.sum(dico_ships_copy['Number']) == 0:
			ok_beggin = False
			while ok_beggin != True:
				print("There are no more ships available. Would you like "
					 +"to keep this configuration?")

				graphs.show_state_ancrage(human_table, human_dico, list_plcs)
				print("If yes, enter True, if not enter False")
				choice_confirm = input("=>")
				if choice_confirm in shortcall_yes:
					ok_beggin = True
					ok_boat_h = True

				elif choice_confirm in shortcall_no:
					ok_rearg = False
					while ok_rearg != True:
						print("Do you want to completely reset the "
							 +"placement of your ships? If so enter True, "
							 +"if not enter False.")

						what_reag = input("=>")
						if what_reag in shortcall_yes:
							human_table = np.ones((10, 10, 3), dtype=float)
							dico_ships_copy = deepcopy(dico_ships)
							human_dico = {}
							ok_beggin = True
							ok_rearg = True

						elif what_reag in shortcall_no:
							while ok_rearg != True:
								print("Do you want to change the placement "
									 +"of one of your ships? If so enter "
									 +"True, if not enter False.")

								what_reag = input("=>")
								if what_reag in shortcall_yes:
									ok_reposi = False
									while ok_reposi != True:
										print("Please select the vessel to "
											 +"be moved from the following "
											 +"list:")

										for i in list(human_dico.keys()):
											print(str(i) + " " +
												  + str(human_dico[i]))

										re_typ = input("=>")
										if re_typ in list(human_dico.keys()):
											human_table[
											 human_dico[re_typ]['x'],
											 human_dico[re_typ]['y'], :] = 1.
											msk = dico_ships_copy[
														'Type'] == re_typ

											dico_ships_copy[
														'Number'][msk] += 1

											human_dico.pop(re_typ)
											ok_rearg = True
											ok_reposi = True
											ok_beggin = True
										else:
											print(str(re_typ)
												 + " is not one of the"
												 + " possible choices.")

								elif what_reag in shortcall_no:
									ok_rearg = True

								else:
									print(str(what_reag) + " is not one"
										 + " of the possible choices.")

						else:
							print(str(what_reag) + " is not one of "
								 + "the possible choices.")

				else:
					print(str(choice_confirm) + " is not one of the"
						 + " possible choices.")

	return human_table, human_dico

def choice_difficulty(raccourci_diffi):
	"""
	Function with wich the human will choose the difficulty level.

	Parameters
	----------
	raccourci_diffi : dict
		Dictionary containing shortcut call name for the difficulty.

	Returns
	-------
	difficulty : str
		The difficulty level chosen.

	"""
	ok_dif = False
	while ok_dif != True:
		print("What level of difficulty do you want to choose:")
		print("\t1-easy (e)")
		print("\t2-medium (m)")
		print("\t3-hard (h)")
		difficulty = input("=>")
		if difficulty in list(raccourci_diffi.keys()):
			difficulty = raccourci_diffi[difficulty]

		if difficulty == 'easy':
			print("Difficulty chooses: " + difficulty)
			ok_dif = True

		elif difficulty == 'medium':
			print("Difficulty chooses: " + difficulty)
			ok_dif = True

		elif difficulty == 'hard' :
			print("Difficulty chooses: " + difficulty)
			ok_dif = True

		else:
			print(str(difficulty)
				  + " is not part of the possible choices.")

	return difficulty

def human_play(list_possi_place, list_ppl, what_human_see, computer_plate,
			  dico_computer, computer_lost, victoire, end):
	"""
	Function to make the human player choose where to fires at the
	computer plate.

	Parameters
	----------
	list_possi_place : list
		List of string. They correspond to all of the possible combination
		of position when the human put them in command line:
		(['A0', 'A1', ..., '8J', '9J']).
	list_ppl : list
		List of 2 list witch contain the name of the lines and columns.
	what_human_see : numpy.ndarray
		Computer plate representation saw by human. Its rgb chanel to
		indicate the nature of the explored cell. White = unexplored, blue
		= shot in water, red = shot in an unsinked boat, black = sinked
		boat.
	computer_plate : numpy.ndarray
		Computer plate with rgb chanel to indicate where are its boats.
	dico_computer : dict
		Dictionary descripting all ship state of the computer.
	computer_lost : list # seems useless
		List of position where there was a computer boat before it was sunk.
	victoire : str
		Indicate the winner.
	end : bool
		If the fight continue or not.

	Returns
	-------
	tbl_hum : numpy.ndarray
		Update computer plate representation saw by human. Its rgb chanel to
		indicate the nature of the explored cell. White = unexplored, blue =
		shot in water, red = shot in an unsinked boat, black = sinked boat.
	dico_computer_copy : dict
		Updated dictionary descripting all ship state of the computer.
	comp_lost : list
		List of position where there was a computer boat before it was sunk.
	victoire : str
		Indicate the winner.
	end : bool
		If the fight continue or not.

	"""
	ok_feu = False
	dico_computer_copy = deepcopy(dico_computer)
	tbl_hum = np.copy(what_human_see)
	comp_lost = deepcopy(computer_lost)
	while ok_feu != True:
		print("Please choose a box to fire on the tray. To do this,\n"
			  + "enter a letter in the interval [A, J] for the line, and\n"
			  + "a number in the interval [0, 9] for the column. To abandon"
			  + "the current part came 'give up'.")

		cell_tageted = input('=>')
		if cell_tageted in list_possi_place:
			shot_position = np.zeros(2, dtype=int)
			if cell_tageted[0] in list_ppl[0]:
				shot_position[0] = np.where(
								np.array(list_ppl[0]) == cell_tageted[0])[0]

				shot_position[1] = int(cell_tageted[1])

			else:
				shot_position[1] = int(cell_tageted[0])
				shot_position[0] = np.where(
								np.array(list_ppl[0]) == cell_tageted[1])[0]

			if 	np.sum(tbl_hum[shot_position[0], shot_position[1]]) != 3:
				print("You’ve already tried this box.")

			else:
				ok_feu = True
				if np.sum(computer_plate[shot_position[0],
										 shot_position[1]]) == 3:

					print("You didn’t hit an enemy ship.")
					tbl_hum[shot_position[0],
							shot_position[1]] = np.array([0., 0., 1.])

				else:
					print("You hit an enemy ship.")
					tbl_hum[shot_position[0],
							shot_position[1]] = np.array([1., 0., 0.])

					for i in list(dico_computer_copy.keys()):
						if np.sum(dico_computer_copy[i]['rgb'] == 
								  computer_plate[shot_position[0], 
												 shot_position[1]]) == 3:

							dico_computer_copy[i]['state'] -= 1

					for i in list(dico_computer_copy.keys()):
						if dico_computer_copy[i]['state'] == 0:
							print("You sunk the " + i.lower() + " enemy !")
							comp_lost.append(i)
							for xi in dico_computer_copy[i]['x']:
								for yi in dico_computer_copy[i]['y']:
									tbl_hum[xi, yi, :] = 0

							dico_computer_copy.pop(i)

		elif cell_tageted == 'give up':
			victoire = 'computer'
			ok_feu = True
			end = True

		else:
			print(str(cell_tageted) + " is not present on the set.")

	return tbl_hum, dico_computer_copy, comp_lost, victoire, end
