from sklearn.cluster import KMeans
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000

import matplotlib.pyplot as plt
import argparse
import utils
import cv2
import numpy as np
import sys

from text_detection import td_single
import os
r = open("white_result_r.txt","a+")
g = open("white_result_g.txt","a+")
b = open("white_result_b.txt","a+")
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str,
                help="path to input image")
args = ap.parse_args()

# we can dispaly it with matplotlib
image = cv2.imread(args.image, -1)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

white_r = 0
white_g = 0
white_b = 0

def show_color(color):#색 하나 막대로 출력하는 함수
    bar = np.zeros((50, 300, 3), dtype = "uint8")
    cv2.rectangle(bar, (0,0), (300, 300), color.astype("uint8").tolist(), -1)
    
    plt.figure()
    plt.axis("off")
    plt.imshow(bar)
    plt.show()
    
    
def centroid_histogram(clt):
    
    # grab the number of different clusters and create a histogram
    # based on the number of pixels assigned to each cluster
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins = numLabels)
 
    # normalize the histogram, such that it sums to one
    hist = hist.astype("float")
    hist /= hist.sum()

    hist.sort()
    max_color = 0 #제일 비율 높은 색의 인덱스

    okay = False
    
    for i in range(6, 0, -1):
        if(clt.cluster_centers_[i][0] > 10 and clt.cluster_centers_[i][1] > 10 and clt.cluster_centers_[i][2] > 10): #
            max_color = i
            #show_color(clt.cluster_centers_[max_color])
            okay = True
            break
    
    #print("Highest rate color :", clt.cluster_centers_[max_color])#제일 비율 높은 색의 rgb 값
    
    
    # return the histogram
    return okay, hist, clt.cluster_centers_[max_color][0], clt.cluster_centers_[max_color][1], clt.cluster_centers_[max_color][2]


gap = image.shape[0]//35
pieces = image.shape[0]//gap
max_color_rgb = [[0 for col in range(3)] for row in range(pieces + 1)]
delta_e = 0 #[[0] for row in range(pieces)]
num = 0
sum_standard=[0]*3
avg_max_color_rgb=[0]*3

for i in range(image.shape[0]-gap, 0, -gap):
    start = i
    end = i - gap

    if(end < 0):
        end = 0
    
    crop_img = image[end:start, 0:image.shape[1]]    
    each_image = crop_img.reshape((crop_img.shape[0] * crop_img.shape[1], 3)) #픽셀화
    
    clt = KMeans(n_clusters = 7, random_state=0)
    clt.fit(each_image)
    
    j = i//gap

    okay, hist, max_color_rgb[j][0], max_color_rgb[j][1], max_color_rgb[j][2] = centroid_histogram(clt)

    max_color_rgb.append(max_color_rgb[j][0] + max_color_rgb[j][1] + max_color_rgb[j][2])
    
    
    #print(j, "조각에서의 대표색 : ", max_color_rgb[j], "\nokay는? ", okay, "\n")

    if(okay):
        num = num + 1
        sum_standard[0] = sum_standard[0] + max_color_rgb[j][0]
        sum_standard[1] = sum_standard[1] + max_color_rgb[j][1]
        sum_standard[2] = sum_standard[2] + max_color_rgb[j][2]
        
    if(num == 3):
        break
    

avg_max_color_rgb[0] = sum_standard[0]/3.0
avg_max_color_rgb[1] = sum_standard[1]/3.0
avg_max_color_rgb[2] = sum_standard[2]/3.0


print("single file result = ",end='')
print(avg_max_color_rgb)
r.write(str(round(avg_max_color_rgb[0])))
r.write(" ")
g.write(str(round(avg_max_color_rgb[1])))
g.write(" ")
b.write(str(round(avg_max_color_rgb[2])))
b.write(" ")
