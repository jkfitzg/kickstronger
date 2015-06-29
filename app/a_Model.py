from sklearn.externals import joblib
import pandas as pd
import numpy as np 
import re

def clean_currency(money):
	if isistance(money,str):
		clean_money = money.replace('$','')
		clean_money = money.replace(',','')
		return int(clean_money)
	else:
		return int(money)


def ModelIt(goal,n_backed,n_rewards,min_reward,max_reward,n_body_words,category):

	goal = int(round(float(goal)))
	n_backed = int(round(float(n_backed)))
	n_rewards = int(round(float(n_rewards)))
	min_reward = int(round(float(min_reward)))
	max_reward = int(round(float(max_reward)))
	n_body_words = int(round(float(n_body_words)))


	category_names = np.array(['art','comics','crafts','dance','design','fashion','film',
                           'food','games','journalism','music','photography','publishing',
                           'technology','theater'])

	category_array = np.zeros_like(category_names,dtype=int)
	category_array[np.where(category_names == category)[0]] = 1

	X_pre = np.array([goal,n_backed,n_rewards,min_reward,max_reward,n_body_words])
	X = np.hstack([X_pre,category_array])

	# for local
	# clf = joblib.load('/Users/jamie/insight_data/kickstarter/small_clf/clf.pkl')
	
	# for aws
	clf = joblib.load('/home/ubuntu/app/small_clf/small_clf/clf.pkl')
	y_1_proba = clf.predict_proba(X)
	success_chance = 100*round(y_1_proba[0,1],3)

	advice1 = ''
	advice2 = ''
	advice3 = ''
	advice4 = ''

	if n_backed < 3:
		advice1 = 'Consider backing other campaigns. This will get you involved in the Kickstarter community and '+\
		'show you other campaigns. You backed ' + str(n_backed) + \
				' campaigns, while successful campaigners backed a median of 3 campaigns.'

	if n_rewards < 9:
		if advice1 == '':
			advice1 = 'Consider adding more rewards. You have ' + str(n_rewards)+ \
				' rewards, while successful campaigns have a median of 9 rewards.' 
		else:
			advice2 = 'Consider adding more rewards. You have ' + str(n_rewards)+ \
				' rewards, while successful campaigns have a median of 9 rewards.' 

	if n_body_words < 650:
		if advice1 == '':
			advice1 = 'Consider writing a longer post description. Your description is ' + str(n_body_words) + \
				' words, while successful campaigns have a median of 658 words.'
		elif advice2 == '':
			advice2 = 'Consider writing a longer post description. Your description is ' + str(n_body_words) + \
				' words, while successful campaigns have a median of 658 words.'
		else:		
			advice3 = 'Consider writing a longer post description. Your description is ' + str(n_body_words) + \
				' words, while successful campaigns have a median of 658 words.'

	if goal > 4000:
		if advice1 == '':
			advice1 = 'Consider lowering your goal or strengthening your advertizing. Your goal is $'+str(goal) +\
				', while the median goal of successful campaigns is $4000.'
		elif advice2 == '':
			advice2 = 'Consider lowering your goal or strengthening your advertizing. Your goal is $'+str(goal) +\
				', while the median goal of successful campaigns is $4000.'
		elif advice3 == '':
			advice3 = 'Consider lowering your goal or strengthening your advertizing. Your goal is $'+str(goal) +\
				', while the median goal of successful campaigns is $4000.'
		else:
			advice4 = 'Consider lowering your goal or strengthening your advertizing. Your goal is $'+str(goal) +\
				', while the median goal of successful campaigns is $4000.'

	if advice1 == '' and advice2 == '' and advice3 =='' and advice4 == '':
		advice1 = 'Your involvement in backing other Kickstarter campaigns, many rewards,\
		 		detailed project description, and relatively small goal give you a great chance of success.'
		advice2 = 'Getting your social network involved in your campaign is also likely to help you meet your goal.' 

	return success_chance, advice1, advice2, advice3, advice4