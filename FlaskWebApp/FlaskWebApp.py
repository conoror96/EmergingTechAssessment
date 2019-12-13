# Adapted from https://pythonspot.com/flask-hello-world/
# Adapted from https://www.youtube.com/watch?v=f6Bf3gl4hWY
# https://docs.python.org/2/library/
# https://docs.scipy.org/doc/scipy-0.18.1/reference/generated/scipy.misc.imsave.html
# https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_default_graph
# https://stackoverflow.com/questions/15345790/scipy-misc-module-has-no-attribute-imread
from flask import Flask, render_template, request
# used for saving, reading, and resizing images
# Scipy was deprecated on the version I was using. Using 1.2.0 now
from scipy.misc import imread, imresize, imsave
# For matrix math
import numpy as np
# for regular expressions
import re
# Used to decode the image with b64decode
import base64
# import tensorflow
import tensorflow as tf
# import load_model from keras
from keras.models import load_model

# Initialise Flask App
app = Flask(__name__)

# global variables for model & graph
global model, graph, sess


# set graph to the current computation graph
graph = tf.get_default_graph()

# Load trained model
model = load_model('model.h5')

# decoding image from base64 into raw representation
def convertImage(imgData1):
  imgstr = re.search(r'base64,(.*)', str(imgData1)).group(1)
  with open('output.png', 'wb') as output:
    output.write(base64.b64decode(imgstr))

# Render the webpage
@app.route('/')
def index():
  return render_template("index.html")

# When the predict method is called, the user drawn image will be input to the model
# A conclusion is reached and a classification is returned
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
	  # prediction is made
    out = model.predict(x)
    # convert the response to a string and return
    response = np.argmax(out, axis=1)
    return str(response[0])

# Run the app on given port 
if __name__ == "__main__":
  #app.run()
	app.run(host='0.0.0.0', port=5000, threaded=False)