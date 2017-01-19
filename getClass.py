##Code majorly from https://github.com/bikz05/bag-of-words
import argparse as ap
import cv2
import imutils 
import numpy as np
import os
from sklearn.svm import LinearSVC
from sklearn.externals import joblib
from scipy.cluster.vq import *
def customClassifier():
    clf, classes_names, stdSlr, k, voc = joblib.load("features.pkl")


    # Image received from android device
    image_paths = []
    image_paths.append("image.jpg")    
    # Using SURF here, can use SIFT also
    fea_det = cv2.FeatureDetector_create("SURF")
    des_ext = cv2.DescriptorExtractor_create("SURF")

    des_list = []

    for image_path in image_paths:
        im = cv2.imread(image_path)
        if im == None:
            print "No such file"
            exit()
        kpts = fea_det.detect(im)
        kpts, des = des_ext.compute(im, kpts)
        des_list.append((image_path, des))   
        
    descriptors = des_list[0][1]
    for image_path, descriptor in des_list[0:]:
        descriptors = np.vstack((descriptors, descriptor)) 

    
    test_features = np.zeros((len(image_paths), k), "float32")
    for i in xrange(len(image_paths)):
        words, distance = vq(des_list[i][1],voc)
        for w in words:
            test_features[i][w] += 1

    # Scale the features
    test_features = stdSlr.transform(test_features)

    # Perform the predictions
    predictions =  [classes_names[i] for i in clf.predict(test_features)]

    # Visualize the results, if "visualize" flag set to true by the user
    for image_path, prediction in zip(image_paths, predictions):
        return prediction
