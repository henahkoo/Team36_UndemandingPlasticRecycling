
from result_class import res3
from sklearn.cluster import KMeans
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000


import matplotlib.pyplot as plt
import argparse as ap
import utils
import cv2
import os
import warnings
import numpy as np

mod3 = 300

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
    max_color = 0
    
    for i in range(6, 0, -1):
        if(clt.cluster_centers_[i][0] > 60 and clt.cluster_centers_[i][1] > 60 and clt.cluster_centers_[i][2] > 60): #
            max_color = i
            #show_color(clt.cluster_centers_[max_color])
            break

#print("Higest rate color :", clt.cluster_centers_[max_color])#제일 비율 높은 색의 rgb 값

#if(clt.cluster_centers_[max_color][0]> 1 and clt.cluster_centers_[max_color][1]> 1 and clt.cluster_centers_[max_color][2]> 1):
#show_color(clt.cluster_centers_[max_color])

# return the histogram
    return hist, clt.cluster_centers_[max_color][0], clt.cluster_centers_[max_color][1], clt.cluster_centers_[max_color][2]




def function3():
    # we can dispaly it with matplotlib
    image = cv2.imread(res3.path, -1)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    gap = image.shape[0]//35
    pieces = image.shape[0]//gap
    max_color_rgb = [[0 for col in range(3)] for row in range(pieces + 1)]
    delta_e = [0. for row in range(pieces)] #0
    n_clusters = 7
    sum_standard=[0]*3
    avg_max_color_rgb=[0]*3
    
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        for i in range(image.shape[0], 0, -gap):
            start = i
            end = i - gap
        
            if(end < 0):
                end = 0
            
            crop_img = image[end:start, 0:image.shape[1]]
            each_image = crop_img.reshape((crop_img.shape[0] * crop_img.shape[1], 3)) #픽셀화
            
            clt = KMeans(n_clusters = 7, random_state=0)
            clt.fit(each_image)
            
            j = i//gap
            
            hist, max_color_rgb[j][0], max_color_rgb[j][1], max_color_rgb[j][2] = centroid_histogram(clt)
    
        max_color_rgb.append(max_color_rgb[j][0] + max_color_rgb[j][1] + max_color_rgb[j][2])
    
    for i in range(pieces - 1, 0, -1): #avg_max_color가 모듈4에서 병 색깔 이라고 결정하기!
        if(max_color_rgb[i][0] != 0 and max_color_rgb[i][1] != 0 and max_color_rgb[i][2] != 0):
            sum_standard[0] = max_color_rgb[i-1][0] + max_color_rgb[i-2][0] + max_color_rgb[i-3][0]
            sum_standard[1] = max_color_rgb[i-1][1] + max_color_rgb[i-2][1] + max_color_rgb[i-3][1]
            sum_standard[2] = max_color_rgb[i-1][2] + max_color_rgb[i-2][2] + max_color_rgb[i-3][2]
            
            avg_max_color_rgb[0] = sum_standard[0]/3.0
            avg_max_color_rgb[1] = sum_standard[1]/3.0
            avg_max_color_rgb[2] = sum_standard[2]/3.0
            break

    count = 0
    max_delta_e = 0
    for j in range(pieces, 0, -1):
        if(max_color_rgb[j][0] != 0 and max_color_rgb[j][1] != 0 and max_color_rgb[j][2] != 0
           and max_color_rgb[j-1][0] != 0 and max_color_rgb[j-1][1] != 0 and max_color_rgb[j-1][2] != 0):
            color1_rgb = sRGBColor(max_color_rgb[j-1][0], max_color_rgb[j-1][1], max_color_rgb[j-1][2]) #맨아래보다 하나 위부터 3개 평균색
            color2_rgb = sRGBColor(max_color_rgb[j][0], max_color_rgb[j][1], max_color_rgb[j][2])
            
            color1_lab = convert_color(color1_rgb, LabColor)
            color2_lab = convert_color(color2_rgb, LabColor)
            
            delta_e[j-1] = delta_e_cie2000(color1_lab, color2_lab)
            
            if(delta_e[j-1] > 50):
                count = count + 1
            elif(delta_e[j-1] > 40):
                count = count + 0.5


#    print("count = ", count)

    if(count > 5.5):
        mod3 = 1
        res3.hasLabel = True
        print("Label O!")
    else:
        mod3 = 0
        print("Label X!")

