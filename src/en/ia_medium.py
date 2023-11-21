# -*- coding: utf-8 -*-
"""
Module containing the functions specific to the medium difficulty bot.
"""
import numpy as np
import ia_general as iag
#=============================================================================
def neighbor_search(list_water, list_notsink, list_sinked):
	"""
	Function to search around the found boat to complete it.

	Parameters
	----------
	list_water : list
		List of cells position that have fall in watter.
	list_notsink : list
		List of cell position that are part of a still not sinked boat.
	list_sinked : list
		List of cell position that are part of an already sinked boat.

	Returns
	-------
	xh : int
		X position of the cell to target.
	yh : int
		Y position of the cell to target.

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
				xh, yh = possib_try[np.random.choice(
							range(len(possib_try)))]

			elif len(possib_try) < 1:
				xh, yh = iag.look_first_hit(list_water, list_notsink,
											list_sinked)

		else:#security line
			xh, yh = iag.look_first_hit(list_water, list_notsink, list_sinked)

	else:#security line
		xh, yh = iag.look_first_hit(list_water, list_notsink, list_sinked)

	return xh, yh
