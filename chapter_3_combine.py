#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 11:33:24 2025

@author: alpha
"""
import cv2
path='/home/alpha/Desktop/open_cv_program/Untitled.webp'


image=cv2.imread(path)
# cv2.imshow('original',image)


imageline=image.copy()


imageline=cv2.line(imageline,(50,45),(300,45),(255,255,255),thickness=30,lineType=cv2.LINE_AA)



text="kdu image"
fontScale=2
fontFace=cv2.FONT_HERSHEY_PLAIN
fontColor=(0,255,0)
fontThickness=2

imageline=cv2.putText(imageline,text,(65,45),fontFace,fontScale,fontColor,fontThickness,cv2.LINE_AA)

imageline=cv2.circle(imageline,(150,95),40,(0,255,255),thickness=10,lineType=cv2.LINE_8)

imageline=cv2.rectangle(imageline,(50,136),(250,300),(255,0,255),thickness=5,lineType=cv2.LINE_8)



cv2.imshow("copy",imageline)



cv2.waitKey(0)
cv2.destroyAllWindows()