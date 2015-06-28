from a_Model import ModelIt
from flask import render_template, request
from app import app

import random
import StringIO
 
from flask import Flask, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

@app.route('/')
@app.route('/index')
@app.route('/input')
def index():
  return render_template("input.html")

@app.route('/output')
def output():
  goal = request.args.get('Goal')
  category = request.args.get('Category')
  n_backed = request.args.get('N_backed')
  n_body_words = request.args.get('N_body_words')
  n_rewards = request.args.get('N_Rewards')
  min_reward = request.args.get('Min_reward')
  max_reward = request.args.get('Max_reward')


  success_chance, advice1, advice2, advice3, advice4 = ModelIt(goal,n_backed,n_rewards,min_reward,max_reward,n_body_words,category)
    
  return render_template("output.html", the_result = success_chance, advice1=advice1,advice2=advice2,advice3=advice3,advice4=advice4)

@app.errorhandler(500)
def internal_err():
  return render_template("input.html")