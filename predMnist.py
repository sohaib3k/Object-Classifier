import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from urllib import urlretrieve
import cPickle as pickle
import os
import gzip
import sys
from util import *
sys.setrecursionlimit(10000)
import numpy as np
import theano
import glob
import numpy
import PIL
from PIL import Image,ImageMath
import lasagne
from lasagne import layers
os.environ['THEANO_FLAGS']="device=cpu"

from lasagne.updates import nesterov_momentum
from lasagne.updates import adadelta
from nolearn.lasagne import NeuralNet
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

def predMnist():
    with open('netpickleMnist','rb') as f:
         neuralNet = pickle.load(f)
            
    #with open("image.jpg", "rb") as g:
    #    img = g.read()

    img = Image.open('image.jpg').resize((28,28),PIL.Image.NEAREST)
    img = numpy.asarray(img, dtype='float32')
    img_ = img.reshape(None,None, 32, 32)




    prediction = neuralNet.predict(img_)
    return prediction
