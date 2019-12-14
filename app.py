import os
from flask import Flask
from flask import render_template
from flask import request, redirect
# from pymongo import MongoClient
from scipy.stats import beta
from scipy.stats import beta
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import time
import random

from img_to_vec import Img2Vec
from PIL import Image

import os

from ElementWiseRounding import ElementWiseRounding

img2vec = Img2Vec()

input_path = './Cars'


app = Flask(__name__, static_url_path='/static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

PEOPLE_FOLDER = os.path.join('static')
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

@app.route('/')
def hello_world():
    return render_template('gui.html')

@app.route('/action')
def test():

	# for i in range(20):

		# for file in os.listdir(input_path):

		# 	filename = os.fsdecode(file)
		# 	img = Image.open(os.path.join(input_path, filename)
		# 	vec = img2vec.get_vec(img)

	for i in range(5):
		for file in os.listdir(input_path):
			filename = os.fsdecode(file)
			img = Image.open(os.path.join(input_path, filename))
			vec = img2vec.get_vec(img)	

    # for i in range(length):

    #     dist = distance.euclidean(list,db[i])

    #     distances.append([dist, i+1])

    # distances.sort()

    # nearest_r_indices = []

    # for i in range(r):

    #     nearest_r_indices.append(distances[i][1])
        
    # return nearest_r_indices 
    
	path ='./static'
	files = os.listdir(path)
	index = random.randrange(0, len(files))
	# print(files[index])
	fig = os.path.join(app.config['UPLOAD_FOLDER'], files[index])

	index = random.randrange(0, len(files))
	# print(files[index])
	fig2 = os.path.join(app.config['UPLOAD_FOLDER'], files[index])

	index = random.randrange(0, len(files))
	# print(files[index])
	fig3 = os.path.join(app.config['UPLOAD_FOLDER'], files[index])

	index = random.randrange(0, len(files))
	# print(files[index])
	fig4 = os.path.join(app.config['UPLOAD_FOLDER'], files[index])

	return render_template('results.html', img = fig, img2 = fig2, img3 = fig3, img4 = fig4)    

if __name__ == '__main__':
    app.run()    
