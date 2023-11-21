# -*- coding: utf-8 -*-
"""
Module contenant les fonctions permetant de faire s'affonter un humain contre
l'ordinateur, deux bots entre eux ou pour tester l'efficacité d'un bot.
"""
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import boucle_de_jeu
#=============================================================================

to_do = 'human'

if to_do == 'human':
	result = boucle_de_jeu.main_loop_human_bot()

elif  to_do == 'bot vs bot':
	scores = []
	joueur1 = 'difficile'
	joueur2 = 'difficile'
	for i in tqdm(range(100000)):
		gagnant = boucle_de_jeu.bot_match(joueur1, joueur2, False)
		if gagnant == 'j1':
			scores.append(1)
		elif gagnant == 'j2':
			scores.append(2)
		elif gagnant == 'null':
			scores.append(0)
		else:
			raise

	scores = np.array(scores)
	dictionaire = np.load('results_bots_match.npy', allow_pickle=True)[0]
	clee = joueur1+'_vs_'+joueur2
	if clee in list(dictionaire.keys()):
		dictionaire[clee] = np.concatenate((dictionaire[clee],
												scores)).astype('int16')
	else:
		dictionaire[clee] = scores.astype('int16')

	np.save('results_bots_match.npy', np.array([dictionaire]))

	values, counts = np.unique(dictionaire[clee], return_counts=True)
	if 1 not in values:
		vide = ' '*16+'0 |'
	else:
		compte = counts[values == 1][0]
		vide = ' '*(17-len(str(compte)))+str(compte)+' |'
	if 2 not in values:
		vide += ' '*17+'0 |'
	else:
		compte = counts[values == 2][0]
		vide += ' '*(18 - len(str(compte))) + str(compte) + ' |'
	if 0 not in values:
		vide += ' '*7+'0 '
	else:
		compte = counts[values == 0][0]
		vide += ' '*(8 - len(str(compte))) + str(compte) + ' '

	print('Résultats')
	print('Joueur 1 = '+joueur1)
	print('Joueur 2 = '+joueur2)
	print('victoire joueur 1 | victoire joueur 2 | égalité ')
	print('------------------+-------------------+---------')
	print(vide)

elif to_do == 'test bot':
	stats = []
	mode = 'facile'
	for i in tqdm(range(1000)):
		wat, repar = boucle_de_jeu.bot_analyse(mode)
		stats.append([len(wat), repar[0], repar[1]])

	stats = np.array(stats)
	result_dico = np.load('bot_test.npy', allow_pickle=True)[0]
	if mode in list(result_dico.keys()):
		result_dico[mode] = np.concatenate((result_dico[mode], stats))
	else:
		result_dico[mode] = stats

	np.save('bot_test.npy', np.array([result_dico]))

	for mod in list(result_dico.keys()):
		print(mod, result_dico[mod].shape)
		print('Min - Max : ', np.min(result_dico[mod], axis=0),
				np.max(result_dico[mod], axis=0))

		print('Moyenne : ', np.mean(result_dico[mod], axis=0))
		print('Médiane : ', np.median(result_dico[mod], axis=0))
		print('Ecart-type : ', np.std(result_dico[mod], axis=0), '\n')

		eau_v, eau_c = np.unique(result_dico[mod][:, 0], return_counts=True)
		chasse_v, chasse_c = np.unique(result_dico[mod][:, 1],
										return_counts=True)

		destruction_v, destruction_c = np.unique(result_dico[mod][:, 2],
													return_counts=True)

		eau_c = (eau_c/np.sum(eau_c)).astype('float32')
		chasse_c = (chasse_c/np.sum(chasse_c)).astype('float32')
		destruction_c = (destruction_c/np.sum(destruction_c)
												).astype('float32')

		eau_mean = np.mean(result_dico[mod][:, 0])
		chasse_mean = np.mean(result_dico[mod][:, 1])
		destruction_mean = np.mean(result_dico[mod][:, 2])

		plt.figure(figsize=(14, 5))
		plt.subplot(1, 3, 1)
		plt.title('Eau')
		plt.vlines(eau_v, 0, eau_c, lw=2)
		plt.vlines(eau_mean, 0, 1, color='r')
		plt.xlim(-1, 84)
		plt.ylim(0, np.max(eau_c)+np.max(eau_c)*0.02)
		plt.subplot(1, 3, 2)
		plt.title('Chasse')
		plt.vlines(chasse_v, 0, chasse_c, lw=2)
		plt.vlines(chasse_mean, 0, 1, color='r')
		plt.xlim(-1, 84)
		plt.ylim(0, np.max(chasse_c)+np.max(chasse_c)*0.02)
		plt.subplot(1, 3, 3)
		plt.title('Destruction')
		plt.vlines(destruction_v, 0, destruction_c, lw=2)
		plt.vlines(destruction_mean, 0, 1, color='r')
		plt.xlim(11, 45)
		plt.ylim(0, np.max(destruction_c)+np.max(destruction_c)*0.02)
		plt.show()
