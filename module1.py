#realtimefirebase_2 ver.


import os, re, glob
os.environ['THEANO_FLAGS'] = 'optimizer=None'
import cv2
import numpy as np
from sklearn.model_selection import train_test_split

#저장한 이미지들로 .npy 만든 후 CNN 돌리는 코드

from keras.models import Sequential
from keras.layers import Dropout, Activation, Dense
from keras.layers import Flatten, Convolution2D, MaxPooling2D
from keras.models import load_model

# UPR _ module 1
import shutil
from numpy import argmax
 
categories = ["bottle", "dummy"]


def Dataization(img_path):
    image_w = 28
    image_h = 28
    img = cv2.imread(img_path)
    img = cv2.resize(img, None, fx=image_w/img.shape[1], fy=image_h/img.shape[0])
    return (img/256)

def function():
    from result_class import res3
    src = []
    name = []
    test = []
 
    image_dir = "/Users/bonha/realtimefirebase_easypath/image"
    for file in os.listdir(image_dir):
         if (file.find('.png') is not -1):
             src.append(image_dir + file)
             name.append(file)
             test.append(Dataization(image_dir + '/' + file))


    mod1 = 100
    
    test = np.array(test)
    model = load_model('Gersang.h5')
    predict = model.predict_classes(test)

    for i in range(len(test)):
        print('\n' + name[i])
        print("Predict : " + str(categories[predict[i]]))

    if (str(categories[predict[i]])=="bottle"):
        res3.isBottle = True

    print("                                      1. From module 1 =>"+str(res3.isBottle))

    res3.path = image_dir + "/" + name[i]
    print(res3.path)
