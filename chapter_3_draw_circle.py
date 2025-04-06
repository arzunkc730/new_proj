#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 12:20:41 2025

@author: alpha
"""

import cv2

path='/home/alpha/Desktop/open_cv_program/Untitled.webp'


image=cv2.imread(path)
cv2.imshow('original',image)


imgcircle=image.copy()

imgcircle=cv2.circle(imgcircle,(50,150),100,(0,255,255),thickness=10,lineType=cv2.LINE_8)

cv2.imshow("copy",imgcircle)


cv2.waitKey(0)
cv2.destroyAllWindows()