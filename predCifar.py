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
#Setting the device as CPU, sadly wont work since CNN trained on a CUDA machine.
os.environ['THEANO_FLAGS']="device=cpu"

from lasagne.updates import nesterov_momentum
from lasagne.updates import adadelta
from nolearn.lasagne import NeuralNet
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

def predCifar():
    with open('netpickleCifar','rb') as f:
         neuralNet = pickle.load(f)
            
    #loading image into appropriate format
    img = Image.open('image.jpg').resize((32,32),PIL.Image.NEAREST)
    img = numpy.asarray(img, dtype='float32') / 256.
    img_ = img.transpose(2, 0, 1).reshape(1, 3, 32, 32)

    #Loading class names
    fo = open('batches.meta', 'rb')
    dict = pickle.load(fo)
    fo.close()
    listnames = dict['label_names']

    #predictijg
    prediction = neuralNet.predict(img_)
    return listnames[prediction[0]]
