# -*- coding: utf-8 -*-
"""
Module contenant les functions extremes.
"""
import numpy as np
#=============================================================================
def opening_dict():
	"""
	
	"""
	opentree = np.array([np.array([1, 2, 3, 4]), np.array([5]),
						 np.array([6]), np.array([5]),
						 np.array([6]), np.array([7, 9]), np.array([8, 10]),
						 np.array([11]), np.array([12]), np.array([11]),
						 np.array([12]), np.array([13, 15, 17, 19]),
						 np.array([14, 16, 18, 20]), np.array([21]),
						 np.array([22]), np.array([23]), np.array([24]),
						 np.array([21]), np.array([22]), np.array([23]),
						 np.array([24]), np.array([25, 29]),
						 np.array([26, 30]), np.array([27, 31]),
						 np.array([28, 32]), np.array([33]), np.array([34]),
						 np.array([35]), np.array([36]), np.array([33]),
						 np.array([34]), np.array([35]), np.array([36]),
						 np.array([37, 41]), np.array([38, 42]),
						 np.array([39, 43]), np.array([40, 44]),
						 np.array([45]), np.array([46]), np.array([47]),
						 np.array([48]), np.array([45]), np.array([46]),
						 np.array([47]), np.array([48]), np.array([49, 53]),
						 np.array([50, 54]), np.array([51, 55]),
						 np.array([52, 56]), np.array([57]), np.array([58]),
						 np.array([57]), np.array([58]), np.array([57]),
						 np.array([58]), np.array([57]), np.array([58]),
						 np.array([59, 61]), np.array([60, 62]),
						 np.array([63]), np.array([64]), np.array([63]),
						 np.array([64]), np.array([65, 67, 69, 71]),
						 np.array([66, 68, 70, 72]), np.array([73]),
						 np.array([74]), np.array([75]), np.array([76]),
						 np.array([75]), np.array([76]), np.array([73]),
						 np.array([74]), np.array([77, 81]),
						 np.array([78, 82]), np.array([79, 83]),
						 np.array([80, 84]), np.array([85]), np.array([86]),
						 np.array([85]), np.array([86]), np.array([85]),
						 np.array([86]), np.array([85]), np.array([86]),
						 np.array([87, 89]), np.array([88, 90]),
						 np.array([91]), np.array([92]), np.array([91]),
						 np.array([92]), np.array([93, 95]),
						 np.array([94, 96]), np.array([97]), np.array([98]),
						 np.array([97]), np.array([98])], dtype=object)

	step_0 = np.zeros((10, 10), dtype=int)
	step_1_1 = np.copy(step_0)
	step_1_1[4, 4] = 1
	step_1_2 = np.rot90(np.copy(step_1_1), 3)
	step_1_3 = np.rot90(np.copy(step_1_1), 2)
	step_1_4 = np.rot90(np.copy(step_1_1), 1)
	step_2_1 = np.copy(step_0)
	step_2_1[4, 4] = 1
	step_2_1[5, 5] = 1
	step_2_2 = np.rot90(np.copy(step_2_1), 1)
	step_3_1 = np.copy(step_2_1)
	step_3_1[3, 3] = 1
	step_3_2 = np.rot90(np.copy(step_3_1), 3)
	step_3_3 = np.rot90(np.copy(step_3_1), 2)
	step_3_4 = np.rot90(np.copy(step_3_1), 1)
	step_4_1 = np.copy(step_3_1)
	step_4_1[6, 6] = 1
	step_4_2 = np.rot90(np.copy(step_4_1), 1)
	step_5_1 = np.copy(step_4_1)
	step_5_1[6, 2] = 1
	step_5_2 = np.rot90(np.copy(step_5_1), 3)
	step_5_3 = np.rot90(np.copy(step_5_1), 2)
	step_5_4 = np.rot90(np.copy(step_5_1), 1)
	step_5_5 = np.copy(step_4_1)
	step_5_5[7, 3] = 1
	step_5_6 = np.rot90(np.copy(step_5_5), 3)
	step_5_7 = np.rot90(np.copy(step_5_5), 2)
	step_5_8 = np.rot90(np.copy(step_5_5), 1)
	step_6_1 = np.copy(step_5_1)
	step_6_1[7, 3] = 1
	step_6_2 = np.rot90(np.copy(step_6_1), 3)
	step_6_3 = np.rot90(np.copy(step_6_1), 2)
	step_6_4 = np.rot90(np.copy(step_6_1), 1)
	step_7_1 = np.copy(step_6_1)
	step_7_1[5, 1] = 1
	step_7_2 = np.rot90(np.copy(step_7_1), 3)
	step_7_3 = np.rot90(np.copy(step_7_1), 2)
	step_7_4 = np.rot90(np.copy(step_7_1), 1)
	step_7_5 = np.copy(step_6_1)
	step_7_5[8, 4] = 1
	step_7_6 = np.rot90(np.copy(step_7_5), 3)
	step_7_7 = np.rot90(np.copy(step_7_5), 2)
	step_7_8 = np.rot90(np.copy(step_7_5), 1)
	step_8_1 = np.copy(step_7_1)
	step_8_1[8, 4] = 1
	step_8_2 = np.rot90(np.copy(step_8_1), 3)
	step_8_3 = np.rot90(np.copy(step_8_1), 2)
	step_8_4 = np.rot90(np.copy(step_8_1), 1)
	step_9_1 = np.copy(step_8_1)
	step_9_1[2, 6] = 1
	step_9_2 = np.rot90(np.copy(step_9_1), 3)
	step_9_3 = np.rot90(np.copy(step_9_1), 2)
	step_9_4 = np.rot90(np.copy(step_9_1), 1)
	step_9_5 = np.copy(step_8_1)
	step_9_5[3, 7] = 1
	step_9_6 = np.rot90(np.copy(step_9_5), 3)
	step_9_7 = np.rot90(np.copy(step_9_5), 2)
	step_9_8 = np.rot90(np.copy(step_9_5), 1)
	step_10_1 = np.copy(step_9_1)
	step_10_1[3, 7] = 1
	step_10_2 = np.rot90(np.copy(step_10_1), 3)
	step_10_3 = np.rot90(np.copy(step_10_1), 2)
	step_10_4 = np.rot90(np.copy(step_10_1), 1)
	step_11_1 = np.copy(step_10_1)
	step_11_1[1, 5] = 1
	step_11_2 = np.rot90(np.copy(step_11_1), 3)
	step_11_3 = np.rot90(np.copy(step_11_1), 2)
	step_11_4 = np.rot90(np.copy(step_11_1), 1)
	step_11_5 = np.copy(step_10_1)
	step_11_5[4, 8] = 1
	step_11_6 = np.rot90(np.copy(step_11_5), 3)
	step_11_7 = np.rot90(np.copy(step_11_5), 2)
	step_11_8 = np.rot90(np.copy(step_11_5), 1)
	step_12_1 = np.copy(step_11_1)
	step_12_1[4, 8] = 1
	step_12_2 = np.rot90(np.copy(step_12_1), 1)
	step_13_1 = np.copy(step_12_1)
	step_13_1[2, 2] = 1
	step_13_2 = np.rot90(np.copy(step_13_1), 3)
	step_13_3 = np.rot90(np.copy(step_13_1), 2)
	step_13_4 = np.rot90(np.copy(step_13_1), 1)
	step_14_1 = np.copy(step_13_1)
	step_14_1[7, 7] = 1
	step_14_2 = np.rot90(np.copy(step_14_1), 1)
	step_15_1 = np.copy(step_14_1)
	step_15_1[0, 4] = 1
	step_15_2 = np.rot90(np.copy(step_15_1), 3)
	step_15_3 = np.rot90(np.copy(step_15_1), 2)
	step_15_4 = np.rot90(np.copy(step_15_1), 1)
	step_15_5 = np.copy(step_14_1)
	step_15_5[4, 0] = 1
	step_15_6 = np.rot90(np.copy(step_15_5), 3)
	step_15_7 = np.rot90(np.copy(step_15_5), 2)
	step_15_8 = np.rot90(np.copy(step_15_5), 1)
	step_16_1 = np.copy(step_15_1)
	step_16_1[5, 9] = 1
	step_16_2 = np.rot90(np.copy(step_16_1), 3)
	step_16_3 = np.rot90(np.copy(step_16_1), 2)
	step_16_4 = np.rot90(np.copy(step_16_1), 1)
	step_17_1 = np.copy(step_16_1)
	step_17_1[4, 0] = 1
	step_17_2 = np.rot90(np.copy(step_17_1), 3)
	step_17_3 = np.rot90(np.copy(step_17_1), 2)
	step_17_4 = np.rot90(np.copy(step_17_1), 1)
	step_17_5 = np.copy(step_16_1)
	step_17_5[9, 5] = 1
	step_17_6 = np.rot90(np.copy(step_17_5), 3)
	step_17_7 = np.rot90(np.copy(step_17_5), 2)
	step_17_8 = np.rot90(np.copy(step_17_5), 1)
	step_18_1 = np.copy(step_17_1)
	step_18_1[9, 5] = 1
	step_18_2 = np.rot90(np.copy(step_18_1), 1)
	step_19_1 = np.copy(step_18_1)
	step_19_1[1, 1] = 1
	step_19_2 = np.rot90(np.copy(step_19_1), 3)
	step_19_3 = np.rot90(np.copy(step_19_1), 2)
	step_19_4 = np.rot90(np.copy(step_19_1), 1)
	step_20_1 = np.copy(step_19_1)
	step_20_1[8, 8] = 1
	step_20_2 = np.rot90(np.copy(step_20_1), 1)
	step_21_1 = np.copy(step_20_1)
	step_21_1[9, 0] = 1
	step_21_2 = np.rot90(np.copy(step_21_1), 3)
	step_21_3 = np.rot90(np.copy(step_21_1), 2)
	step_21_4 = np.rot90(np.copy(step_21_1), 1)
	step_22_1 = np.copy(step_21_1)
	step_22_1[0, 9] = 1
	step_22_2 = np.rot90(np.copy(step_22_1), 1)

	opendic = np.array([step_0, step_1_1, step_1_2, step_1_3, step_1_4,
						step_2_1, step_2_2, step_3_1, step_3_2, step_3_3,
						step_3_4, step_4_1, step_4_2, step_5_1, step_5_2,
						step_5_3, step_5_4, step_5_5, step_5_6, step_5_7,
						step_5_8, step_6_1, step_6_2, step_6_3, step_6_4,
						step_7_1, step_7_2, step_7_3, step_7_4, step_7_5,
						step_7_6, step_7_7, step_7_8, step_8_1, step_8_2,
						step_8_3, step_8_4, step_9_1, step_9_2, step_9_3,
						step_9_4, step_9_5, step_9_6, step_9_7, step_9_8,
						step_10_1, step_10_2, step_10_3, step_10_4,
						step_11_1, step_11_2, step_11_3, step_11_4,
						step_11_5, step_11_6, step_11_7, step_11_8,
						step_12_1, step_12_2, step_13_1, step_13_2,
						step_13_3, step_13_4, step_14_1, step_14_2,
						step_15_1, step_15_2, step_15_3, step_15_4,
						step_15_5, step_15_6, step_15_7, step_15_8,
						step_16_1, step_16_2, step_16_3, step_16_4,
						step_17_1, step_17_2, step_17_3, step_17_4,
						step_17_5, step_17_6, step_17_7, step_17_8,
						step_18_1, step_18_2, step_19_1, step_19_2,
						step_19_3, step_19_4, step_20_1, step_20_2,
						step_21_1, step_21_2, step_21_3, step_21_4,
						step_22_1, step_22_2])

	return opendic, opentree

def perfect_map_probability(plateau, porte_a, croiseur, sous_m, fregatte,
							navette, list_watter, list_notsink,
							list_sinked, open_tables, open_tree):
	"""
	"""
	# Starting with an opening dictionary
	proba = np.zeros((10, 10)) # initialisation
	if (len(list_notsink) == 0)&(len(list_sinked) == 0):
		current = np.sum(np.sum(open_tables == plateau, axis=1),
						 axis=1) == 100
		branch = open_tree[current[:-2]][0]
		next_one = open_tables[branch[np.random.randint(0,
											len(branch))]]
		proba = next_one - plateau

	return proba

def fine_proba(looked, porte_avion, croiseur, sous_marin, fregatte, navette):
	"""
	Go quickly up in time and memory consumstion. Don not make it run over an
	fully unkwon plate. Should wait at least 25 hit and a sunked boat.
	To be run during the hunt phase & if there are more than 1 missing boat.

	Pramameters
	-----------
	looked : numpy.ndarray
		Binary 2D array where the 1 indicate that the node is already
		knowned, without matter if it was sea or ship.
	porte_avion : bool
		True if the porte-avion was sinked, else False.
	croiseur : bool
		True if the  was sinked, else False.
	sous_marin : bool
		True if the  was sinked, else False.
	fregatte : bool
		True if the  was sinked, else False.
	navette : bool
		True if the  was sinked, else False.

	Returns
	-------
	posi : numpy.ndarray
		DESCRIPTION.

	Note
	----
	This function does not have the same pdf map as DensityPosiMap.
	DensityPosiMap compute an approximation of the true pdf map wich is not
	computable with average computer power and memory.

	"""
	possibles_plates = np.copy(looked).astype(int)[np.newaxis]

	if porte_avion == False:
		kr = np.array([[[ 0,  0], [ 0,  1], [ 0,  2], [ 0,  3], [ 0,  4]],
					   [[ 0,  0], [ 1,  0], [ 2,  0], [ 3,  0], [ 4,  0]],
					   [[ 0,  0], [ 0, -1], [ 0, -2], [ 0, -3], [ 0, -4]],
					   [[ 0,  0], [-1,  0], [-2,  0], [-3,  0], [-4,  0]]],
					 dtype=int)
		possibles_plates = fine_search_loop(possibles_plates, kr)

	if croiseur == False:
		kr = np.array([[[ 0,  0], [ 0,  1], [ 0,  2], [ 0,  3]],
					   [[ 0,  0], [ 1,  0], [ 2,  0], [ 3,  0]],
					   [[ 0,  0], [ 0, -1], [ 0, -2], [ 0, -3]],
					   [[ 0,  0], [-1,  0], [-2,  0], [-3,  0]]], dtype=int)
		possibles_plates = fine_search_loop(possibles_plates, kr)

	if sous_marin == False:
		kr = np.array([[[ 0,  0], [ 0,  1], [ 0,  2]],
					   [[ 0,  0], [ 1,  0], [ 2,  0]],
					   [[ 0,  0], [ 0, -1], [ 0, -2]],
					   [[ 0,  0], [-1,  0], [-2,  0]]], dtype=int)
		possibles_plates = fine_search_loop(possibles_plates, kr)


	if fregatte == False:
		kr = np.array([[[ 0,  0], [ 0,  1], [ 0,  2]],
					   [[ 0,  0], [ 1,  0], [ 2,  0]],
					   [[ 0,  0], [ 0, -1], [ 0, -2]],
					   [[ 0,  0], [-1,  0], [-2,  0]]], dtype=int)
		possibles_plates = fine_search_loop(possibles_plates, kr)

	if navette == False:
		kr = np.array([[[ 0,  0], [ 0,  1]], [[ 0,  0], [ 1,  0]],
					   [[ 0,  0], [ 0, -1]], [[ 0,  0], [-1,  0]]],
					  dtype=int)
		possibles_plates = fine_search_loop(possibles_plates, kr)

	probabilities = np.sum(possibles_plates-looked, axis=0)
	posi = np.argwhere(probabilities == np.max(probabilities))
	if len(posi) == 1:
		posi = posi[0]
	else:
		posi = posi[np.random.randint(len(posi))]

	return posi

def map_four_boats(plateau, rays):
	"""
	For when four boats remain.

	Parameters
	----------
	plateau : TYPE
		DESCRIPTION.
	rays : TYPE
		Decreased sorted.

	Returns
	-------
	proba : TYPE
		DESCRIPTION.

	"""
	kpa = np.array([[[ 0,  0], [ 0,  1], [ 0,  2], [ 0,  3], [ 0,  4]],
					[[ 0,  0], [ 1,  0], [ 2,  0], [ 3,  0], [ 4,  0]],
					[[ 0,  0], [ 0, -1], [ 0, -2], [ 0, -3], [ 0, -4]],
					[[ 0,  0], [-1,  0], [-2,  0], [-3,  0], [-4,  0]]],
					dtype=int)
	kcr = np.array([[[ 0,  0], [ 0,  1], [ 0,  2], [ 0,  3]],
					[[ 0,  0], [ 1,  0], [ 2,  0], [ 3,  0]],
					[[ 0,  0], [ 0, -1], [ 0, -2], [ 0, -3]],
					[[ 0,  0], [-1,  0], [-2,  0], [-3,  0]]],
					dtype=int)
	ksm = np.array([[[ 0,  0], [ 0,  1], [ 0,  2]], [[ 0,  0], [ 1,  0],
					 [ 2,  0]], [[ 0,  0], [ 0, -1], [ 0, -2]], [[ 0,  0],
					 [-1,  0], [-2,  0]]], dtype=int)
	knv = np.array([[[ 0,  0], [ 0,  1]], [[ 0,  0], [ 1,  0]], [[ 0,  0],
					 [ 0, -1]], [[ 0,  0], [-1,  0]]], dtype=int)

	kernels = []
	for i in rays:
		if i == 5:
			kernels.append(kpa)
		elif i == 4:
			kernels.append(kcr)
		elif i == 3:
			kernels.append(ksm)
		elif i == 2:
			kernels.append(knv)

	proba = np.zeros((10, 10))
	# first boat
	places_0 = np.argwhere(plateau == 0)
	lk0 = np.concatenate((places_0[:, np.newaxis, np.newaxis]
						 + np.copy(kernels[0])))
	lk0 = lk0[np.sum((lk0[:, :, 0] <= 9)&(
					  lk0[:, :, 1] <= 9)&(
					  lk0[:, :, 0] >= 0)&(
					  lk0[:, :, 1] >= 0),
					 axis=1) == rays[0]]
	lk0 = lk0[np.sum(plateau[lk0[:, :, 0],
				 lk0[:, :, 1]], axis=1) == 0]
	for t_0 in range(len(lk0)):
		table_0 = np.copy(plateau)
		table_0[lk0[t_0, :, 0], lk0[t_0, :, 1]] = 1
		# second boat
		places_1 = np.argwhere(table_0 == 0)
		lk1 = np.concatenate((places_1[:, np.newaxis, np.newaxis]
							  + np.copy(kernels[1])))
		lk1 = lk1[np.sum((lk1[:, :, 0] <= 9)&(
						  lk1[:, :, 1] <= 9)&(
						  lk1[:, :, 0] >= 0)&(
						  lk1[:, :, 1] >= 0),
						 axis=1) == rays[1]]
		lk1 = lk1[np.sum(table_0[lk1[:, :, 0],
								 lk1[:, :, 1]], axis=1) == 0]
		for t_1 in range(len(lk1)):
			table_1 = np.copy(table_0)
			table_1[lk1[t_1, :, 0], lk1[t_1, :, 1]] = 1
			# third boat
			places_2 = np.argwhere(table_1 == 0)
			lk2 = np.concatenate((places_2[:, np.newaxis, np.newaxis]
								  + np.copy(kernels[2])))
			lk2 = lk2[np.sum((lk2[:, :, 0] <= 9)&(
							  lk2[:, :, 1] <= 9)&(
							  lk2[:, :, 0] >= 0)&(
							  lk2[:, :, 1] >= 0),
							 axis=1) == rays[2]]
			lk2 = lk2[np.sum(table_1[lk2[:, :, 0],
							  lk2[:, :, 1]], axis=1) == 0]
			for t_2 in range(len(lk2)):
				table_2 = np.copy(table_1)
				table_2[lk2[t_2, :, 0], lk2[t_2, :, 1]] = 1
				# fourth boat
				places_3 = np.argwhere(table_2 == 0)
				lk3 = np.concatenate((places_3[:, np.newaxis, np.newaxis]
									  + np.copy(kernels[3])))
				lk3 = lk3[np.sum((lk3[:, :, 0] <= 9)&(
								  lk3[:, :, 1] <= 9)&(
								  lk3[:, :, 0] >= 0)&(
								  lk3[:, :, 1] >= 0),
								  axis=1) == rays[3]]
				lk3 = lk3[np.sum(table_2[lk3[:, :, 0],
								  lk3[:, :, 1]], axis=1) == 0]
				for t_3 in range(len(lk3)):
					table_3 = np.copy(table_2)
					table_3[lk3[t_3, :, 0], lk3[t_3, :, 1]] = 1
					proba = proba+table_3

	proba[plateau == 1] = 0
	return proba

# 3 boats
def map_three_boats(plateau, rays):
	"""For when three boats remain"""
	kpa = np.array([[[ 0,  0], [ 0,  1], [ 0,  2], [ 0,  3], [ 0,  4]],
					[[ 0,  0], [ 1,  0], [ 2,  0], [ 3,  0], [ 4,  0]],
					[[ 0,  0], [ 0, -1], [ 0, -2], [ 0, -3], [ 0, -4]],
					[[ 0,  0], [-1,  0], [-2,  0], [-3,  0], [-4,  0]]],
					dtype=int)
	kcr = np.array([[[ 0,  0], [ 0,  1], [ 0,  2], [ 0,  3]],
					[[ 0,  0], [ 1,  0], [ 2,  0], [ 3,  0]],
					[[ 0,  0], [ 0, -1], [ 0, -2], [ 0, -3]],
					[[ 0,  0], [-1,  0], [-2,  0], [-3,  0]]],
					dtype=int)
	ksm = np.array([[[ 0,  0], [ 0,  1], [ 0,  2]], [[ 0,  0], [ 1,  0],
					 [ 2,  0]], [[ 0,  0], [ 0, -1], [ 0, -2]], [[ 0,  0],
					 [-1,  0], [-2,  0]]], dtype=int)
	knv = np.array([[[ 0,  0], [ 0,  1]], [[ 0,  0], [ 1,  0]], [[ 0,  0],
					 [ 0, -1]], [[ 0,  0], [-1,  0]]], dtype=int)

	kernels = []
	for i in rays:
		if i == 5:
			kernels.append(kpa)
		elif i == 4:
			kernels.append(kcr)
		elif i == 3:
			kernels.append(ksm)
		elif i == 2:
			kernels.append(knv)

	proba = np.zeros((10, 10))
	# first boat
	places_0 = np.argwhere(plateau == 0)
	lk0 = np.concatenate((places_0[:, np.newaxis, np.newaxis]
						 + np.copy(kernels[0])))
	lk0 = lk0[np.sum((lk0[:, :, 0] <= 9)&(
					  lk0[:, :, 1] <= 9)&(
					  lk0[:, :, 0] >= 0)&(
					  lk0[:, :, 1] >= 0),
					 axis=1) == rays[0]]
	lk0 = lk0[np.sum(plateau[lk0[:, :, 0],
				 lk0[:, :, 1]], axis=1) == 0]
	for t_0 in range(len(lk0)):
		table_0 = np.copy(plateau)
		table_0[lk0[t_0, :, 0], lk0[t_0, :, 1]] = 1
		# second boat
		places_1 = np.argwhere(table_0 == 0)
		lk1 = np.concatenate((places_1[:, np.newaxis, np.newaxis]
							  + np.copy(kernels[1])))
		lk1 = lk1[np.sum((lk1[:, :, 0] <= 9)&(
						  lk1[:, :, 1] <= 9)&(
						  lk1[:, :, 0] >= 0)&(
						  lk1[:, :, 1] >= 0),
						 axis=1) == rays[1]]
		lk1 = lk1[np.sum(table_0[lk1[:, :, 0],
								 lk1[:, :, 1]], axis=1) == 0]
		for t_1 in range(len(lk1)):
			table_1 = np.copy(table_0)
			table_1[lk1[t_1, :, 0], lk1[t_1, :, 1]] = 1
			# third boat
			places_2 = np.argwhere(table_1 == 0)
			lk2 = np.concatenate((places_2[:, np.newaxis, np.newaxis]
								  + np.copy(kernels[2])))
			lk2 = lk2[np.sum((lk2[:, :, 0] <= 9)&(
							  lk2[:, :, 1] <= 9)&(
							  lk2[:, :, 0] >= 0)&(
							  lk2[:, :, 1] >= 0),
							 axis=1) == rays[2]]
			lk2 = lk2[np.sum(table_1[lk2[:, :, 0],
							  lk2[:, :, 1]], axis=1) == 0]
			for t_2 in range(len(lk2)):
				table_2 = np.copy(table_1)
				table_2[lk2[t_2, :, 0], lk2[t_2, :, 1]] = 1
				proba = proba+table_2

	proba[plateau == 1] = 0
	return proba

# 2 boats
def map_two_boats(plateau, rays):
	"""For when two boats remain"""
	kpa = np.array([[[ 0,  0], [ 0,  1], [ 0,  2], [ 0,  3], [ 0,  4]],
					[[ 0,  0], [ 1,  0], [ 2,  0], [ 3,  0], [ 4,  0]],
					[[ 0,  0], [ 0, -1], [ 0, -2], [ 0, -3], [ 0, -4]],
					[[ 0,  0], [-1,  0], [-2,  0], [-3,  0], [-4,  0]]],
					dtype=int)
	kcr = np.array([[[ 0,  0], [ 0,  1], [ 0,  2], [ 0,  3]],
					[[ 0,  0], [ 1,  0], [ 2,  0], [ 3,  0]],
					[[ 0,  0], [ 0, -1], [ 0, -2], [ 0, -3]],
					[[ 0,  0], [-1,  0], [-2,  0], [-3,  0]]],
					dtype=int)
	ksm = np.array([[[ 0,  0], [ 0,  1], [ 0,  2]], [[ 0,  0], [ 1,  0],
					 [ 2,  0]], [[ 0,  0], [ 0, -1], [ 0, -2]], [[ 0,  0],
					 [-1,  0], [-2,  0]]], dtype=int)
	knv = np.array([[[ 0,  0], [ 0,  1]], [[ 0,  0], [ 1,  0]], [[ 0,  0],
					 [ 0, -1]], [[ 0,  0], [-1,  0]]], dtype=int)

	kernels = []
	for i in rays:
		if i == 5:
			kernels.append(kpa)
		elif i == 4:
			kernels.append(kcr)
		elif i == 3:
			kernels.append(ksm)
		elif i == 2:
			kernels.append(knv)

	proba = np.zeros((10, 10))
	# first boat
	places_0 = np.argwhere(plateau == 0)
	lk0 = np.concatenate((places_0[:, np.newaxis, np.newaxis]
						 + np.copy(kernels[0])))
	lk0 = lk0[np.sum((lk0[:, :, 0] <= 9)&(
					  lk0[:, :, 1] <= 9)&(
					  lk0[:, :, 0] >= 0)&(
					  lk0[:, :, 1] >= 0),
					 axis=1) == rays[0]]
	lk0 = lk0[np.sum(plateau[lk0[:, :, 0],
				 lk0[:, :, 1]], axis=1) == 0]
	for t_0 in range(len(lk0)):
		table_0 = np.copy(plateau)
		table_0[lk0[t_0, :, 0], lk0[t_0, :, 1]] = 1
		# second boat
		places_1 = np.argwhere(table_0 == 0)
		lk1 = np.concatenate((places_1[:, np.newaxis, np.newaxis]
							  + np.copy(kernels[1])))
		lk1 = lk1[np.sum((lk1[:, :, 0] <= 9)&(
						  lk1[:, :, 1] <= 9)&(
						  lk1[:, :, 0] >= 0)&(
						  lk1[:, :, 1] >= 0),
						 axis=1) == rays[1]]
		lk1 = lk1[np.sum(table_0[lk1[:, :, 0],
								 lk1[:, :, 1]], axis=1) == 0]
		for t_1 in range(len(lk1)):
			table_1 = np.copy(table_0)
			table_1[lk1[t_1, :, 0], lk1[t_1, :, 1]] = 1
			proba = proba+table_1

	proba[plateau == 1] = 0
	return proba

def map_one_boat(plateau, ray):
	"""For when one boats remain"""
	kpa = np.array([[[ 0,  0], [ 0,  1], [ 0,  2], [ 0,  3], [ 0,  4]],
					[[ 0,  0], [ 1,  0], [ 2,  0], [ 3,  0], [ 4,  0]],
					[[ 0,  0], [ 0, -1], [ 0, -2], [ 0, -3], [ 0, -4]],
					[[ 0,  0], [-1,  0], [-2,  0], [-3,  0], [-4,  0]]],
					dtype=int)
	kcr = np.array([[[ 0,  0], [ 0,  1], [ 0,  2], [ 0,  3]],
					[[ 0,  0], [ 1,  0], [ 2,  0], [ 3,  0]],
					[[ 0,  0], [ 0, -1], [ 0, -2], [ 0, -3]],
					[[ 0,  0], [-1,  0], [-2,  0], [-3,  0]]],
					dtype=int)
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
	lk0 = np.concatenate((places_0[:, np.newaxis, np.newaxis]
						 + np.copy(kernel)))
	lk0 = lk0[np.sum((lk0[:, :, 0] <= 9)&(
					  lk0[:, :, 1] <= 9)&(
					  lk0[:, :, 0] >= 0)&(
					  lk0[:, :, 1] >= 0),
					 axis=1) == ray]
	lk0 = lk0[np.sum(plateau[lk0[:, :, 0],
				 lk0[:, :, 1]], axis=1) == 0]
	for t_0 in range(len(lk0)):
		table_0 = np.copy(plateau)
		table_0[lk0[t_0, :, 0], lk0[t_0, :, 1]] = 1
		proba = proba+table_0

	proba[plateau == 1] = 0
	return proba