# -*- coding: utf-8 -*-
"""
Module pour les actions de l'humain.
"""
import numpy as np
from copy import deepcopy
import graphics as graphs
import ia_general as iag
#=============================================================================
def placing_human_boats(dico_ships, list_plcs, all_posi_pos_list,
						short_boat_call, shortcall_yes, shortcall_no):
	"""
	Fonction avec laquelle l’humain placera ses bateaux.

	Paramètres
	----------
	dico_ships : dict
		Dictionnaire initié des bateaux.
	list_plcs : list
		Liste de deux chaînes. Valeurs à mettre sur les axes x et y. Il
		provient de la fonction create_pos_pl().
	all_posi_pos_list : list
		Liste de chaînes de caractaîres. Elle correspond à toutes les
		combinaisons possibles de position lorsque l’humain les rentre :
		(['A0', 'A1', ..., '8J', '9J']).
	short_boat_call : dict
		Dictionnaire contenant les raccourci d’appel pour les bateaux.
	shortcall_yes : dict
		Dictionnaire contenant les raccourci d’appel pour l’accord.
	shortcall_no : dict
		Dictionnaire contenant les raccourci d’appel pour le désaccord.

	Retourne
	--------
	human_table : numpy.ndarray
		Table de jeu de l'humaine avec les couleurs rvb pour indiquer où
		sont les bateaux.
	human_dico : dict
		Dictionnaire humain où l’état des bateaux est enregistré.

	"""
	dico_ships_cp  = deepcopy(dico_ships)
	human_table = np.ones((10, 10, 3), dtype=float)
	ok_boat_h = False
	human_dico = {}
	while ok_boat_h != True:
		ok_type_boat = False
		ok_position = False
		while ok_type_boat != True:
			print("Veuillez choisir un type de bateau pour le placer.\n"
				 + "Pour cela rentrez le nom (Type) ou le numéros du "
				 + "navire.\nIl est aussi possible d'utiliser la commande :"
				 + " 'aleatoire' à n'importe quel moment pour que soit "
				 + "automatiquement palcé les\nbateaux restant de manière "
				 + "aléatoire. Vous pourrez toujours modifier les positions "
				 + "et les rotations de navires placé de\ncette manière.")

			graphs.pretty_dict_print(dico_ships_cp)
			ship_type = input("=>")
			if ship_type in list(short_boat_call.keys()):
				ship_type = short_boat_call[ship_type]

			if ship_type in dico_ships_cp['Type'].tolist():
				id_type = np.where(dico_ships_cp['Type'] == ship_type)[0][0]
				numb_rest = dico_ships_cp['Nombre'][id_type]
				if numb_rest < 1:
					print("Il n'y a plus de bateaux de ce type de "
						  + "disponible, veuillez réessayer avec un autre "
						  + "type.")

				else:
					dico_ships_cp['Nombre'][id_type] -= 1
					ok_type_boat = True

			elif ship_type == 'aleatoire':
				human_dico, human_table = iag.random_positiong_ships(
												dico_ships_cp, human_table)

				dico_ships_cp['Nombre'][:] = 0
				ok_type_boat = True
				ok_position = True

			else:
				print(ship_type + ' ne fait pas partie des types de bateaux '
					  + 'possible. Veuillez réessayer.')

		while ok_position != True:
			ok_acc = False
			while ok_acc != True:
				print("Veuillez choisir une case d'acroche pour placer le "
					  + "navire " + ship_type + " sur le plateau.\nPour "
					  + "cela rentrer une lettre dans l'interval [A, J] pour"
					  +" la ligne, et un nombre dans l'interval [0, 9] pour "
					  + "la colone.")

				graphs.show_state_ancrage(human_table, human_dico, list_plcs)
				ancre = input("=>").upper()
				place_xy = np.zeros(2, dtype=int)
				if ancre not in all_posi_pos_list:
					print(str(ancre) + " n'est pas présent sur le plateau."
						  + " Veuillez réessayer.")
				else:
					if ancre[0] in list_plcs[0]:
						place_xy[0] = np.where(
									   np.array(list_plcs[0]) == ancre[0])[0]

						place_xy[1] = int(ancre[1])
					else:
						place_xy[1] = int(ancre[0])
						place_xy[0] = np.where(
									   np.array(list_plcs[0]) == ancre[1])[0]

					rayon = dico_ships_cp['Longueur'][
								dico_ships_cp['Type'] == ship_type][0]

					end_close = iag.look_end_cell(rayon, place_xy,
															human_table)
					if len(end_close) == 0:
						print("Il n'y a aucune configuration possible pour "
							  + "ce bateau avec cette case d'acroche. "
							  + "Veuillez choisir une autre case.")

					else:
						ok_acc = True

			ok_rota = False
			while ok_rota != True:
				print("Veuillez choisir une des rotations possibles. Pour "+
					  "cela rentrez l'entier correspondant au cas voulus "+
					  "représenté dans le(s) tableau(x) suivant. Si vous "+
					  "souhaiter changer la case d'acroche, rentrez : "+
					  "'retour accroche'.")

				graphs.show_state_rotation(human_table, dico_ships_cp, rayon,
										   end_close, id_type, list_plcs,
										   human_dico, place_xy, ship_type)

				ch_rotation = input("=>")
				try:
					ch_rotation = int(ch_rotation)
					if (ch_rotation < 0)|(ch_rotation >= len(end_close)):
						print(str(ch_rotation) + " ne fais pas partie des "
							  + "rotations possible, veuillez réessayer")

					else:
						xrt = np.linspace(place_xy[0],
										  end_close[ch_rotation, 0], rayon+1,
										  dtype=int)
						yrt = np.linspace(place_xy[1],
										  end_close[ch_rotation, 1], rayon+1,
										  dtype=int)

						human_dico[ship_type] = {}
						human_dico[ship_type]['x'] = xrt
						human_dico[ship_type]['y'] = yrt
						human_dico[ship_type]['Couleur'] = dico_ships_cp[
														'Couleur'][id_type]
						human_dico[ship_type]['rvb'] = dico_ships_cp[
														'Codes rvb'][id_type]
						human_table[xrt, yrt] = human_dico[ship_type]['rvb']
						ok_position = True
						ok_rota = True

				except:
					if ch_rotation == 'retour accroche':
						ok_rota = True
					else:
						print(str(ch_rotation) + " n'est pas convertible en "
							  + "un entier, veuillez réessayer")

		if np.sum(dico_ships_cp['Nombre']) == 0:
			ok_beggin = False
			while ok_beggin != True:
				print("Il n'y plus de navires disponible. Souhaitez-vous "
					  + "garder cette configuration ?")

				graphs.show_state_ancrage(human_table, human_dico, list_plcs)
				print("Si oui, rentrez True, si non rentrez False")
				choice_confirm = input("=>")
				if choice_confirm in shortcall_yes:
					ok_beggin = True
					ok_boat_h = True

				elif choice_confirm in shortcall_no:
					ok_rearg = False
					while ok_rearg != True:
						print("Voulez vous entièrement réinitialiser le "
							  + "placement de vos navires ? Si oui entrez "
							  + "True, si non entrez False.")

						what_reag = input("=>")
						if what_reag in shortcall_yes:
							human_table = np.ones((10, 10, 3), dtype=float)
							dico_ships_cp = deepcopy(dico_ships)
							human_dico = {}
							ok_beggin = True
							ok_rearg = True

						elif what_reag in shortcall_no:
							while ok_rearg != True:
								print("Voulez vous changer le placement d'un"
									  + " de vos navires ? Si oui entrez "
									  + "True, si non entrez False.")

								what_reag = input("=>")
								if what_reag in shortcall_yes:
									ok_reposi = False
									while ok_reposi != True:
										print("Veuillez choisir le navire à "
											  + "déplacer dans la liste "
											  + "suivante :")

										for i in list(human_dico.keys()):
											print(sctr(i) + " "
												  + str(human_dico[i]))

										re_typ = input("=>")
										if re_typ in list(human_dico.keys()):
											human_table[
											  human_dico[re_typ]['x'],
											  human_dico[re_typ]['y'],:] = 1.

											masque = dico_ships_cp['Type']
											masque = masque == re_typ
											dico_ships_cp['Nombre'][
																masque] += 1
											human_dico.pop(re_typ)
											ok_rearg = True
											ok_reposi = True
											ok_beggin = True
										else:
											print(str(re_typ) + " ne fait "
												  + "pas parti des choix "
												  + "possibles.")

								elif what_reag in shortcall_no:
									ok_rearg = True

								else:
									print(str(what_reag) + " ne fait pas "
										  + "parti des choix possibles.")

						else:
							print(str(what_reag) + " ne fait pas parti des "
								  + "choix possibles.")

				else:
					print(str(choice_confirm) + " ne fait pas parti des choix"
						  + " possibles.")

	return human_table, human_dico

def choice_difficulty(raccourci_diffi):
	"""
	Fonction avec laquelle l’humain choisira le niveau de difficulté.

	Paramètres
	----------
	raccourci_diffi : dict
		Dictionnaire contenant le raccourci pour la difficulté.

	Retourne
	--------
	difficulty : str
		Le niveau de difficulté choisi.

	"""
	ok_dif = False
	while ok_dif != True:
		print("Quel niveau de difficulté voulez-vous choisir :")
		print("\t1-facile (f)")
		print("\t2-moyen (m)")
		print("\t3-difficile (d)")
		difficulty = input("=>")
		if difficulty in list(raccourci_diffi.keys()):
			difficulty = raccourci_diffi[difficulty]

		if difficulty == 'facile':
			print("Difficulté choisi : " + difficulty)
			ok_dif = True

		elif difficulty == 'moyen':
			print("Difficulté choisi : " + difficulty)
			ok_dif = True

		elif difficulty == 'difficile' :
			print("Difficulté choisi : " + difficulty)
			ok_dif = True

		else:
			print(str(difficulty)
				  + " ne fait pas partie des choix possibles.")

	return difficulty

def human_play(list_possi_place, list_ppl, what_human_see, computer_plate,
			  dico_computer, computer_lost, victoire, end):
	"""
	Fonction pour faire choisir au joueur humain choisir où tirer sur
	la table de jeu d’ordinateur.

	Paramètres
	----------
	list_possi_place : list
		Liste de chaînes de caractaîres. Elle correspond à toutes les
		combinaisons possibles de position lorsque l’humain les rentre :
		(['A0', 'A1', ..., '8J', '9J']).
	list_ppl : list
		Liste de 2 listes contenant le nom des lignes et colonnes.
	what_human_see : numpy.ndarray
		Table de jeu où l'humain peut voir les conséquences de ses tirs
		contre l'ordinateur. C’est un tableau 2d rgb avec : les cellules
		bleue indiquent un coup dans l'eau, les cellules rouge indiquent
		qu’un bateau a été touché mais pas encore coulé, les cellules noires
		indiquent qu’un bateau a été touché et coulé et les cellules blanche
		sont celles qui n'ont pas encore été explorées.
	computer_plate : numpy.ndarray
		Table de jeu de l'ordinateur avec les couleurs rvb pour indiquer où
		sont les bateaux.
	dico_computer : dict
		Dictionnaire de l'ordinateur où l’état des bateaux est enregistré.
	computer_lost : list # seems useless
		Liste des positions où il y avait un bateau de l'ordinateur avant
		qu’il ne soit coulé.
	victoire : str
		indique le vainqueur.
	end : bool
		Indique si le match continus ou non.

	Retourne
	-------
	tbl_hum : numpy.ndarray
		Table de jeu où l'humain peut voir les conséquences de ses tirs
		contre l'ordinateur mis à jour.
	dico_computer_copy : dict
		Dictionnaire de l'ordinateur mi à jour.
	comp_lost : list
		Liste des positions où il y avait un bateau de l'ordinateur avant
		qu’il ne soit coulé mis à jour.
	victoire : str
		indique le vainqueur.
	end : bool
		Indique si le match continus ou non.

	"""
	ok_feu = False
	dico_computer_copy = deepcopy(dico_computer)
	tbl_hum = np.copy(what_human_see)
	comp_lost = deepcopy(computer_lost)
	while ok_feu != True:
		print("Veuillez choisir une case où faire feu sur le plateau."
			  + "\nPour cela rentrer une lettre dans l'interval [A, J] "
			  + "pour la ligne, et un nombre dans l'interval [0, 9] pour"
			  + " la colone.\n Pour abandonner la partie en cours écrivez"
			  + " 'abandonner'.")

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
				print("Vous avez déjà essayé cette case.")

			else:
				ok_feu = True
				if np.sum(computer_plate[shot_position[0],
										 shot_position[1]]) == 3:

					print("Vous n'avez pas touché de navire adverse.")
					tbl_hum[shot_position[0], shot_position[1]] = np.array(
										[0., 0., 1.])

				else:
					print("Vous avez touché un navire ennemi.")
					tbl_hum[shot_position[0], shot_position[1]] = np.array(
										[1., 0., 0.])

					for i in list(dico_computer_copy.keys()):
						if (dico_computer_copy[i]['rvb'] == 
								computer_plate[shot_position[0], 
									shot_position[1]].tolist()):

							dico_computer_copy[i]['etat'] -= 1

					for i in list(dico_computer_copy.keys()):
						if dico_computer_copy[i]['etat'] == 0:
							print("Vous avez coulé le " + i.lower()
								  + " ennemi !")
							comp_lost.append(i)
							for xi in dico_computer_copy[i]['x']:
								for yi in dico_computer_copy[i]['y']:
									tbl_hum[xi, yi, :] = 0

							dico_computer_copy.pop(i)

		elif cell_tageted == 'abandonner':
			victoire = 'ordniateur'
			ok_feu = True
			end = True

		else:
			print(str(cell_tageted) + " n'est pas présent sur le plateau.")

	return tbl_hum, dico_computer_copy, comp_lost, victoire, end
