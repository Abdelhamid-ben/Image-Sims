#!/bin/python
#A new Calculating method by KadaVir
#https://www.facebook.com/profile.php?id=100009425638198


import cv2
from cv2 import *
from numpy import *
from math import *

#DEFINING THE MINM FUNCTION
def minm(val1,val2):
    if val1 < val2 :
        return val1
    else :
        return val2

#READING THE IMAGES 
img  = imread('a.jpg')
img2 = imread('b.jpg')
SOMME = 0

#CALCULATING THE HISTOGRAM FOR EACH COLOR 
img1Hist1 = cv2.calcHist([img],[0],None,[256],[0,256])
img1Hist2 = cv2.calcHist([img],[1],None,[256],[0,256])
img1Hist3 = cv2.calcHist([img],[2],None,[256],[0,256])

#CALCULATING THE HISTOGRAM FOR EACH COLOR 
img2Hist1 = cv2.calcHist([img2],[0],None,[256],[0,256])
img2Hist2 = cv2.calcHist([img2],[1],None,[256],[0,256])
img2Hist3 = cv2.calcHist([img2],[2],None,[256],[0,256])

#GETTING THE DIMENSIONS 
dem = img.shape
l = dem [0]
c = dem [1]
n = l*c*3

#COMBINING THE HISTOGRAMES
HISTORGRAM1 = append(img1Hist1, [img1Hist2, img1Hist3])
HISTORGRAM2 = append(img2Hist1, [img2Hist2, img2Hist3])

#NORMALISATION OF THE ELEMENTS
for i in range(0,767):
    HISTORGRAM1[i]=HISTORGRAM1[i]/n
    HISTORGRAM2[i]=HISTORGRAM2[i]/n



#CALCULATING...
for i in range(0,767):
   val1=HISTORGRAM1[i]
   val2=HISTORGRAM2[i]
   SOMME = SOMME + minm(val1,val2)
       
Seu = SOMME

#COMAPRING THE RESULT TO THE SEU
print "Seu = ",Seu
if Seu > 0.7 :
   print "Similair"
else :
   print "Not Simalair"

