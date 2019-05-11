#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 03:24:46 2019

@author: minicoder
"""
import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
 
time.sleep(2)
 
backgroundframe=0
 
for i in range(30):
  _,backgroundframe = cap.read()
 
background = np.flip(backgroundframe,axis=1)
#--------------------------------------------------------
while(1):
    _,frame = cap.read()
     
    img  = np.flip(frame ,axis=1)
     
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
     
    lowerred = np.array([0,120,70])
    upperred = np.array([4,255,255])
    mask1 = cv2.inRange(hsv, lowerred, upperred)
     

    lowerred = np.array([170,120,70])
    upperred = np.array([180,255,255])
    mask2 = cv2.inRange(hsv,lowerred,upperred)
     
    mask1 = mask1+mask2
    
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3),np.uint8))
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3,3),np.uint8))
     
     
    mask2 = cv2.bitwise_not(mask1)
     
     
    res1 = cv2.bitwise_and(img,img,mask=mask2)
    
    res2 = cv2.bitwise_and(background, background, mask = mask1)
     
    final_output = cv2.addWeighted(res1,1,res2,1,0)
    cv2.imshow("magic",final_output)
    cv2.waitKey(1)
    