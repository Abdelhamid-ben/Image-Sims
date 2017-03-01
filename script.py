#!/bin/python
from cv2 import *
from numpy import *
from math import *
img1 = imread('a.jpg')
img2 = imread('a.jpg')
#similarite MSE
def MSE(image1,image2):
    gray1 = cvtColor(image1, COLOR_BGR2GRAY)
    gray2 = cvtColor(image2, COLOR_BGR2GRAY)
    TEMP = 0
    x= image1.shape
    a=x[0]
    b=x[1]
    for i in range(0, a) :
        for j in range(0,b): 
            TEMP = TEMP + pow((gray1[i,j]- gray2[i,j]),2)
    MSE= TEMP/(a*b)
    sim= 30
    if MSE < 30 :
        print 'MSE Similar'
    else:
        print 'MSE not Similar'

#Distance entre distibution
def distancedistr(image1,image2):
    gray1 = cvtColor(image1, COLOR_BGR2GRAY)
    gray2 = cvtColor(image2, COLOR_BGR2GRAY)
    TEMP = 0
    TEMP2 = 0
    x= gray1.shape
    a=x[0]
    b=x[1]
    for i in range(0, a) :
        for j in range(0, b):
            TEMP = TEMP + pow((gray1[i,j]- gray2[i,j]),2)
            TEMP2= TEMP2 + (gray1[i,j]+ gray2[i,j])
    DISTANCE = TEMP/TEMP2
    sim= 30
    if DISTANCE < 30 :
         print 'DISTANCE Similar'
    else:
        print 'DISTANCE not Similar'
def hist(image1,image2):
    gray1 = cvtColor(image1, COLOR_BGR2GRAY)
    gray2 = cvtColor(image2, COLOR_BGR2GRAY)
    hist1 = cv2.calcHist([image1],[0],None,[256],[0,256])
    hist2 = cv2.calcHist([image2],[0],None,[256],[0,256])
    leng=len(hist1)
    TEMP=0
    TEMP2=0
    for i in range(0,leng):
        TEMP=TEMP+min(hist1[i],hist2[i])
        TEMP2=TEMP2 + hist2[i]
    TOTAL_HIST= TEMP/TEMP2
    if TOTAL_HIST == 1 :
         print 'HISTOGRAMME Similaire'
    else:
        print 'HISTOGRAMME not Similaire'
answer=raw_input("Enter the method: mse,dist,hist\n")
if answer == "mse" :
    MSE(img1,img2)
elif answer== "hist" :
    hist(img1,img2)
elif answer == "dist":
    distancedistr(img1,img2)
else:
    print "Please write mse,hist, or dist"
    




