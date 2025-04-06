#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 12:25:47 2025

@author: alpha
"""

import cv2

path='/home/alpha/Desktop/open_cv_program/Untitled.webp'


image=cv2.imread(path)
cv2.imshow('original',image)




imgreact=image.copy()

imgreact=cv2.rectangle(imgreact,(500,100),(50,600),(255,0,255),thickness=5,lineType=cv2.LINE_8)

cv2.imshow("copy",imgreact)

cv2.waitKey(0)
cv2.destroyAllWindows()