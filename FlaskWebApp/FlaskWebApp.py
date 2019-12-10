from flask import Flask, render_template,request
from scipy.misc import imsave, imread, imresize
import numpy as np
import keras.models
import re
import sys 
import base64
import tensorflow as tf
from keras.models import load_model

app = Flask(__name__)

global model, graph

graph = tf.get_default_graph()

model = load_model('../Notebook/Model/model.h5')

@app.route('/')
def index():
	#initModel()
	#render out pre-built HTML file right on the index page
	return render_template("draw.html")


if __name__ == "__main__":
    # run the app locally on the given port
	app.run(host='0.0.0.0', port=5000, threaded=False)