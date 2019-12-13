# Adapted from https://pythonspot.com/flask-hello-world/
# Adapted from https://www.youtube.com/watch?v=f6Bf3gl4hWY
# https://docs.scipy.org/doc/scipy-0.18.1/reference/generated/scipy.misc.imsave.html
from flask import Flask, render_template, request
# used for saving, reading, and resizing images
# Scipy was deprecated on the version I was using. Using 1.2.0 now
# https://stackoverflow.com/questions/15345790/scipy-misc-module-has-no-attribute-imread
from scipy.misc import imread, imresize, imsave
# For matrix math
import numpy as np
import re
import sys
import base64
import tensorflow as tf
from keras.models import load_model
#for reading operating system data
import os
#tell our app where our saved model is
#sys.path.append(os.path.abspath("/model"))
# Initialise Flask
app = Flask(__name__)

# global variables
global model, graph

#graph 
graph = tf.get_default_graph()
#model = load_model()

# Load trained model
model = load_model('model.h5')

# decoding image from base64 into raw representation
def convertImage(imgData1):
  imgstr = re.search(r'base64,(.*)', str(imgData1)).group(1)
  with open('output.png', 'wb') as output:
    output.write(base64.b64decode(imgstr))
 
@app.route('/')
def index():
  return render_template("index.html")
@app.route('/predict/', methods=['GET', 'POST'])
def predict():
  #get the raw data format of the image
  imgData = request.get_data()
  #encode it into a suitable format
  convertImage(imgData)
  # read the image into memory
  x = imread('output.png', mode='L')
  # resize image
  x = imresize(x,(28, 28))/255
  #Save resized image
  imsave('final_image.jpg', x)
  # Reshape image
  x = x.reshape(1, 28, 28, 1)
  # computation graph
  with graph.as_default():
	# perform prediciton  
    out = model.predict(x)
    response = np.argmax(out, axis=1)
    return str(response[0])

# Run the app on given port 
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, threaded=False)