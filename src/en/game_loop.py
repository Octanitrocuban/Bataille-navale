# -*- coding: utf-8 -*-
"""
Module containing functions to make a human race against the computer or
two bots between them.
"""
import numpy as np
import graphics as graphs
import interface
import ia_general as iag
import ia_medium as iam
import ia_hard as iah
from copy import deepcopy
#=============================================================================
def main_loop_human_bot():
	"""
	Main function that allows a human to do a battle game against a bot of
	the chosen difficulty.

	Parameters
	----------
	None

	Returns
	-------
	victory : str
		A string indicating which robot or human won the game, if there was
		no draw.

	"""
	boats = {'Type': np.array(['Aircraft-carrier','Cruiser','Submarine',
								 'Frigate', 'Shuttle']),
			 'Length': np.array([5, 4, 3, 3, 2]),
			 'Number': np.array([1, 1, 1, 1, 1]),
			 'Color':np.array(['grey','orange','green','yellow','purple']),
			 'Rgb codes':np.array([[.5, .5, .5], [1, .5, 0], [0, .75, 0],
									 [1., .9, 0.], [.75, 0, .75]])}

	racc_bat = {'a':'Aircraft-carrier', 'c':'Cruiser', 's':'Submarine',
			   '1':'Cruiser', 'f':'Frigate', 'n':'Shuttle',
			   '0':'Aircraft-carrier', '2':'Submarine', '3':'Frigate',
			   '4':'Shuttle'}

	racc_diffi = {'e':'easy', '1':'easy', 'm':'medium', '2':'medium', 
				 'd':'hard', '3':'hard'}

	oui = ['True', 'true', 't', 'oui', 'o', 'yes', 'y']
	non = ['False', 'false', 'f', 'non', 'n', 'no']
	pspspl, poss_places = iag.create_possible_places()
	fond_humain, dico_humain = interface.placing_human_boats(boats, pspspl,
											poss_places, racc_bat, oui, non)

	dico_ordi, fond_ordi = iag.random_positiong_ships(boats)
	visu_human_ordi = np.ones((10, 10, 3), dtype=float)
	for i in list(dico_humain.keys()):
		dico_humain[i]['state'] = len(dico_humain[i]['x'])
		dico_ordi[i]['state'] = len(dico_ordi[i]['x'])

	difficulte = interface.choice_difficulty(racc_diffi)
	if difficulte == 'hard':
		tables_difficile, tree_difficile = iah.opening()

	what_comp_see = np.zeros((10, 10))
	posi_damier, damier_0 = iag.damier_positions(color='k')
	all_x, all_y = np.meshgrid(range(10), range(10))
	all_positions = np.array([all_x.ravel(), all_y.ravel()]).T.tolist()
	victory = 'None'
	human_loss = []
	compu_loss = []
	water = []
	not_sink = []
	sinked = []
	navette_b = False
	sous_b = False
	fregate_b = False
	croiseur_b = False
	porte_b = False
	stop = False
	touched = False
	sinked_b = False
	graphs.show_state_of_the_fight(fond_humain, pspspl, dico_humain, water, 
								   not_sink, sinked, visu_human_ordi)
	while stop != True:
		graphs.show_state_of_the_fight(fond_humain, pspspl, dico_humain,
									   water, not_sink, sinked,
									   visu_human_ordi)

		h_played = interface.human_play(poss_places, pspspl, visu_human_ordi,
										fond_ordi, dico_ordi, compu_loss,
										victory, stop)

		visu_human_ordi, dico_ordi, compu_loss, victory, stop = h_played

		feu_ordi = False
		while feu_ordi != True:
			if touched == False:
				if difficulte == 'easy':
					xh, yh = iag.random_hit(all_positions)
				elif difficulte == 'medium':
					xh, yh = iag.random_hit(posi_damier)
				elif difficulte == 'hard':
					xh, yh = iah.choice_appx_dens_map(what_comp_see,
									navette_b, sous_b, fregate_b, croiseur_b,
									porte_b, water, not_sink, sinked,
									tree_difficile, tables_difficile,
									damier_0, False)

			elif touched == True:
				if difficulte == 'easy':
					xh, yh = iag.look_first_hit(water, not_sink, sinked)
				elif difficulte == 'medium':
					xh, yh = iam.neighbor_search(water, not_sink, sinked)
				elif difficulte == 'hard':
					xh, yh = iah.proba_sinker(what_comp_see, not_sink,
											  navette_b, sous_b, fregate_b,
											  croiseur_b, porte_b)

			cond_water = [xh, yh] not in water
			cond_sinked = [xh, yh] not in not_sink
			cond_not_sink = [xh, yh] not in sinked
			if (cond_water)&(cond_sinked)&(cond_not_sink):
				feu_ordi = True
				conseq = iag.conseq_fire(what_comp_see, xh, yh, pspspl,
										fond_humain, water, not_sink, sinked,
										dico_humain, navette_b, sous_b,
										fregate_b, croiseur_b, porte_b,
										human_loss, touched, sinked_b, False)

				what_comp_see = conseq[0]
				dico_humain = conseq[1]
				navette_b = conseq[2]
				sous_b = conseq[3]
				fregate_b = conseq[4]
				croiseur_b = conseq[5]
				porte_b = conseq[6]
				human_loss = conseq[7]
				water = conseq[8]
				not_sink = conseq[9]
				sinked = conseq[10]
				touched = conseq[11]
				sinked_b = conseq[12]

			# Cleans up the list of possible shots that could already be in
			# water, sinked ou not_sink.
			posi_damier = np.array(iag.look_loop_pth(posi_damier.tolist(),
												water, sinked, not_sink))

			all_positions = iag.look_loop_pth(all_positions, water, sinked,
											  not_sink)

			if (len(dico_ordi.keys()) == 0)&(len(dico_humain.keys()) == 0):
				victory = "null"
				stop = True

			elif len(dico_ordi.keys()) == 0:
				victory = "human"
				stop = True

			elif len(dico_humain.keys()) == 0:
				victory = "computer"
				stop = True

		if len(dico_humain.keys()) == 0:
			victory = "computer"
			stop = True

	graphs.show_state_of_the_fight(fond_humain, pspspl, dico_humain, water,
								   not_sink, sinked, visu_human_ordi)

	graphs.print_victory(victory, sinked, water)
	return victory

def bot_match(joueur1, joueur2, show_fight=False):
	"""
	Function to make 2 fighting algorithms.

	Parameters
	----------
	joueur1 : str
		Difficulty level of the bot playing as player 1.
	joueur2 : str
		Difficulty level of the bot playing as player 2.
	show_fight : bool, optional
		Boolean, if true: displays the match status between two bots.
		The default value is False.

	Returns
	-------
	victory : str
		String indicating which player won.

	"""
	boats = {'Type': np.array(['Aircraft-carrier','Cruiser','Submarine',
								 'Frigate', 'Shuttle']),
			 'Length': np.array([5, 4, 3, 3, 2]),
			 'Number': np.array([1, 1, 1, 1, 1]),
			 'Color':np.array(['grey','orange','green','yellow','purple']),
			 'Rgb codes':np.array([[.5, .5, .5], [1, .5, 0], [0, .75, 0],
									 [1., .9, 0.], [.75, 0, .75]])}

	pspspl, poss_places = iag.create_possible_places()
	dico_bot_1, fond_bot_1 = iag.random_positiong_ships(boats)
	dico_bot_2 = deepcopy(dico_bot_1)
	fond_bot_2 = np.copy(fond_bot_1)
	for i in list(dico_bot_1.keys()):
		dico_bot_1[i]['state'] = len(dico_bot_1[i]['x'])
		dico_bot_2[i]['state'] = len(dico_bot_2[i]['x'])

	if (joueur1 == 'hard')|(joueur2 == 'hard'):
		tables_difficile, tree_difficile = iah.opening()

	what_comp_see_1 = np.zeros((10, 10))
	what_comp_see_2 = np.zeros((10, 10))
	posi_damier1, damier1 = iag.damier_positions(color='k')
	posi_damier2, damier2 = iag.damier_positions(color='k')
	all_x, all_y = np.meshgrid(range(10), range(10))
	all_posi_1 = np.array([all_x.ravel(), all_y.ravel()]).T.tolist()
	all_posi_2 = np.array([all_x.ravel(), all_y.ravel()]).T.tolist()
	victory = 'None'
	loss_1 = []
	loss_2 = []
	water_2 = []
	not_sink_2 = []
	sinked_2 = []
	navette_2 = False
	sous_2 = False
	frega_2 = False
	crois_2 = False
	porte_2 = False
	stop = False
	touch_2 = False
	sinked_b_2 = False
	touch_1 = False
	navette_1 = False
	sous_1 = False
	frega_1 = False
	crois_1 = False
	porte_1 = False
	not_sink_1 = []
	water_1 = []
	sinked_1 = []
	sinked_b_1 = False
	while stop != True:
		if show_fight:
			graphs.show_comp_comp(fond_bot_1, dico_bot_1, water_1,
								  not_sink_1, sinked_1, fond_bot_2,
								  dico_bot_2, water_2, not_sink_2, sinked_2,
								  pspspl)

		feu_1 = False
		while feu_1 != True:
			if touch_1 == False:
				if joueur1 == 'easy':
					xh1, yh1 = iag.random_hit(all_posi_1)
				elif joueur1 == 'medium':
					xh1, yh1 = iag.random_hit(posi_damier1)
				elif joueur1 == 'hard':
					xh1, yh1 = iah.choice_appx_dens_map(what_comp_see_1,
														navette_1, sous_1,
														frega_1, crois_1,
														porte_1, water_1,
														not_sink_1, sinked_1,
														tree_difficile,
														tables_difficile,
														damier1, False)

			elif touch_1 == True:
				if joueur1 == 'easy':
					xh1, yh1 = iag.look_first_hit(water_1, not_sink_1,
												  sinked_1)
				elif joueur1 == 'medium':
					xh1, yh1 = iam.neighbor_search(water_1, not_sink_1,
												   sinked_1)
				elif joueur1 == 'hard':
					xh1, yh1 = iah.proba_sinker(what_comp_see_1, not_sink_1,
												navette_1,  sous_1,
												frega_1, crois_1, porte_1)

			cond_water_1 = [xh1, yh1] not in water_1
			cond_notsk_1 = [xh1, yh1] not in not_sink_1
			cond_sinke_1 = [xh1, yh1] not in sinked_1
			if (cond_water_1)&(cond_notsk_1)&(cond_sinke_1):
				feu_1 = True
				conseq_1 = iag.conseq_fire(what_comp_see_1, xh1, yh1, pspspl,
										   fond_bot_1, water_1, not_sink_1,
										   sinked_1, dico_bot_1, navette_1,
										   sous_1, frega_1, crois_1, porte_1,
										   loss_1, touch_1,  sinked_b_1,
										   False)

				what_comp_see_1 = conseq_1[0]
				dico_bot_1 = conseq_1[1]
				navette_1 = conseq_1[2]
				sous_1 = conseq_1[3]
				frega_1 = conseq_1[4]
				crois_1 = conseq_1[5]
				porte_1 = conseq_1[6]
				loss_1 = conseq_1[7]
				water_1 = conseq_1[8]
				not_sink_1 = conseq_1[9]
				sinked_1 = conseq_1[10]
				touch_1 = conseq_1[11]
				sinked_b_1 = conseq_1[12]

			posi_damier1 = np.array(iag.look_loop_pth(posi_damier1.tolist(),
													  water_1, sinked_1,
													  not_sink_1))

			all_posi_1 = iag.look_loop_pth(all_posi_1, water_1, sinked_1,
										   not_sink_1)

		feu_2 = False
		while feu_2 != True:
			if touch_2 == False:
				if joueur2 == 'easy':
					xh2, yh2 = iag.random_hit(all_posi_2)
				elif joueur2 == 'medium':
					xh2, yh2 = iag.random_hit(posi_damier2)
				elif joueur2 == 'hard':
					xh2, yh2 = iah.choice_appx_dens_map(what_comp_see_2,
														navette_2, sous_2,
														frega_2, crois_2,
														porte_2, water_2,
														not_sink_2, sinked_2,
														tree_difficile,
														tables_difficile,
														damier2, False)

			elif touch_2 == True:
				if joueur2 == 'easy':
					xh2, yh2 = iag.look_first_hit(water_2, not_sink_2,
												  sinked_2)

				elif joueur2 == 'medium':
					xh2, yh2 = iam.neighbor_search(water_2, not_sink_2,
												   sinked_2)

				elif joueur2 == 'hard':
					xh2, yh2 = iah.proba_sinker(what_comp_see_2, not_sink_2,
												navette_2,  sous_2,
												frega_2, crois_2, porte_2)

			cond_water_2 = [xh2, yh2] not in water_2
			cond_notsk_2 = [xh2, yh2] not in not_sink_2
			cond_sinke_2 = [xh2, yh2] not in sinked_2
			if (cond_water_2)&(cond_notsk_2)&(cond_sinke_2):
				feu_2 = True
				conseq_2 = iag.conseq_fire(what_comp_see_2, xh2, yh2, pspspl,
										   fond_bot_2, water_2, not_sink_2,
										   sinked_2, dico_bot_2, navette_2,
										   sous_2, frega_2, crois_2, porte_2,
										   loss_2, touch_2, sinked_b_2,
										   False)

				what_comp_see_2 = conseq_2[0]
				dico_bot_2 = conseq_2[1]
				navette_2 = conseq_2[2]
				sous_2 = conseq_2[3]
				frega_2 = conseq_2[4]
				crois_2 = conseq_2[5]
				porte_2 = conseq_2[6]
				loss_2 = conseq_2[7]
				water_2 = conseq_2[8]
				not_sink_2 = conseq_2[9]
				sinked_2 = conseq_2[10]
				touch_2 = conseq_2[11]
				sinked_b_2 = conseq_2[12]

			posi_damier2 = np.array(iag.look_loop_pth(posi_damier2.tolist(),
													  water_2, sinked_2,
													  not_sink_2))

			all_posi_2 = iag.look_loop_pth(all_posi_2, water_2, sinked_2,
										   not_sink_2)

		if (len(dico_bot_2.keys()) == 0)&(len(dico_bot_1.keys()) == 0):
			victory = "null"
			stop = True

		elif len(dico_bot_2.keys()) == 0:
			victory = "j2"
			stop = True

		elif len(dico_bot_1.keys()) == 0:
			victory = "j1"
			stop = True

	return victory

def bot_analyse(mode, show_fight=False):
	"""
	Function to play a single bot to analyze the number of shots
	needed to sink all the boats of a random map.

	Parameters
	----------
	mode : str
		Type of bot (difficulty level) to test.
	show_fight : bool
		Check whether the tray status will be displayed or not.

	Returns
	-------
	water : list
		List of positions of shots that hit a water cell.
	iter_in : list
		List containing two integers. The first indicates the number of
		shots fired in the hunting phase. The second indicates the number
		of shots fired during the destruction phase.

	"""
	boats = {'Type': np.array(['Aircraft-carrier','Cruiser','Submarine',
								 'Frigate', 'Shuttle']),
			 'Length': np.array([5, 4, 3, 3, 2]),
			 'Number': np.array([1, 1, 1, 1, 1]),
			 'Color':np.array(['grey','orange','green','yellow','purple']),
			 'Rgb codes':np.array([[.5, .5, .5], [1, .5, 0], [0, .75, 0],
									[1., .9, 0.], [.75, 0, .75]])}

	pspspl, poss_places = iag.create_possible_places()
	dico_bot, fond_bot = iag.random_positiong_ships(boats)
	for i in list(dico_bot.keys()):
		dico_bot[i]['state'] = len(dico_bot[i]['x'])

	if mode == 'hard':
		tables_difficile, tree_difficile = iah.opening()

	what_comp_see = np.zeros((10, 10))
	posi_damier, damier = iag.damier_positions(color='k')
	all_x, all_y = np.meshgrid(range(10), range(10))
	all_posi = np.array([all_x.ravel(), all_y.ravel()]).T.tolist()
	victory = 'None'
	loss = []
	stop = False
	touch_b = False
	navette_b = False
	sous_b = False
	frega_b = False
	crois_b = False
	porte_b = False
	water = []
	not_sink = []
	sinked = []
	iter_in = [0, 0]
	sinked_b = False
	while stop != True:
		if show_fight:
			graphs.show_comp_comp(fond_bot, dico_bot, water, not_sink,
								  sinked, fond_bot, dico_bot, water,
								  not_sink, sinked, pspspl)

		feu = False
		while feu != True:
			if touch_b == False:
				iter_in[0] += 1
				if mode == 'easy':
					xh, yh = iag.random_hit(all_posi)
				elif mode == 'medium':
					xh, yh = iag.random_hit(posi_damier)
				elif mode == 'hard':
					xh, yh = iah.choice_appx_dens_map(what_comp_see,
													  navette_b, sous_b,
													  frega_b, crois_b,
													  porte_b, water,
													  not_sink, sinked,
													  tree_difficile,
													  tables_difficile,
													  damier, False)

			elif touch_b == True:
				iter_in[1] += 1
				if mode == 'easy':
					xh, yh = iag.look_first_hit(water, not_sink, sinked)
				elif mode == 'medium':
					xh, yh = iam.neighbor_search(water, not_sink, sinked)
				elif mode == 'hard':
					xh, yh = iah.proba_sinker(what_comp_see, not_sink,
											  navette_b, sous_b, frega_b,
											  crois_b, porte_b)

			cond_water = [xh, yh] not in water
			cond_notsk = [xh, yh] not in not_sink
			cond_sinke = [xh, yh] not in sinked
			if (cond_water)&(cond_notsk)&(cond_sinke):
				feu = True
				conseq = iag.conseq_fire(what_comp_see, xh, yh, pspspl,
										 fond_bot, water, not_sink, sinked,
										 dico_bot, navette_b, sous_b,
										 frega_b, crois_b, porte_b, loss,
										 touch_b,  sinked_b, False)

				what_comp_see = conseq[0]
				dico_bot = conseq[1]
				navette_b = conseq[2]
				sous_b = conseq[3]
				frega_b = conseq[4]
				crois_b = conseq[5]
				porte_b = conseq[6]
				loss = conseq[7]
				water = conseq[8]
				not_sink = conseq[9]
				sinked = conseq[10]
				touch_b = conseq[11]
				sinked_b = conseq[12]

			posi_damier = np.array(iag.look_loop_pth(posi_damier.tolist(),
													 water, sinked, not_sink))

			all_posi = iag.look_loop_pth(all_posi, water, sinked, not_sink)

		if len(dico_bot.keys()) == 0:
			stop = True

	return water, iter_in
