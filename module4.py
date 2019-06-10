#realtimefirebase_2 ver.
#
##
#return
# 0 : blue
# 1 : green
# 2 : transparent
# 3 : other
#print("\n*\n*\n*\nModule 4 Activated")
from result_class import res3
from sklearn.cluster import KMeans
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000

import matplotlib.pyplot as plt
import argparse
import utils
import cv2
import numpy as np

mod4 = 400
# we can dispaly it with matplotlib
image = cv2.imread(res3.path, -1)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


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

def function4():

    gap = image.shape[0]//35
    pieces = image.shape[0]//gap
    max_color_rgb = [[0 for col in range(3)] for row in range(pieces + 1)]
    delta_e = 0 #[[0] for row in range(pieces)]
    num = 0
    sum_standard=[0]*3
    avg_max_color_rgb=[0]*3
    is_it_finish = False

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


    # print("\n#1. WHITE TEST FIRST!!!")
    sensitivity_low = 35
    sensitivity_high = 35

    lower_white = np.array([127.099-sensitivity_low,130.0594-sensitivity_low,132.5842-sensitivity_low])
    upper_white = np.array([127.099+sensitivity_high,130.0594+sensitivity_high,132.5842+sensitivity_high])

    lower_bound = (avg_max_color_rgb>lower_white).all()
    upper_bound = (avg_max_color_rgb<upper_white).all()

    if(lower_bound and upper_bound):
        res3.wht_tsp = True #print("\n***Bottle is White/Transparent***")

        is_it_finish = True



    if (is_it_finish == False):
     
        i=0
        #     most_likely_red = False
        most_likely = avg_max_color_rgb[0]
        most_likely_index = 0
        while i < 3:
            if(most_likely<avg_max_color_rgb[i]):
                most_likely = avg_max_color_rgb[i]
                most_likely_index = i

            i=i+1

        if(most_likely_index==0):
            res3.others = True #print("\n***Bottle is Others***")
            is_it_finish = True



    if(is_it_finish == False):

        
        color_rgb = sRGBColor(avg_max_color_rgb[0], avg_max_color_rgb[1], avg_max_color_rgb[2])
        color_lab = convert_color(color_rgb, LabColor)
        
        #  GREEN detect
        green_rgb = sRGBColor(0, 128, 0)
        green_lab = convert_color(green_rgb, LabColor)
        
        delta_e_green = delta_e_cie2000(color_lab, green_lab)
        #     print("초록색이랑 차이 : ", delta_e_green)
        
        #   BLUE detect
        blue_rgb = sRGBColor(0, 0, 255)
        blue_lab = convert_color(blue_rgb, LabColor)
        
        delta_e_blue = delta_e_cie2000(color_lab, blue_lab)

        
        if(delta_e_green < delta_e_blue):#and delta_e_green < delta_e_white and not most_likely_red): # and (delta_e_blue - delta_e_green) > 10):
            res3.green = True #print("\n***Bottle is Green***")

        elif(delta_e_blue < delta_e_green): #and delta_e_blue < delta_e_white and not most_likely_red):
            res3.blue = True #print("\n***Bottle is Blue***")

    res3.print_final_color()
