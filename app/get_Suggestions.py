from sklearn.externals import joblib
import pandas as pd
import numpy as np 
import re


def get_advice(goal,n_backed,n_rewards,n_body_words):
	advice = ''

	if n_backed < 3:
		advice = advice + 'Consider backing other campaigns first. \n You haven't backed any campaigns, while successful campaigners backed a median of 3 campaigns.'
	else:
		advice = advice + 'You are taking it up to 11!'

	return advice

	