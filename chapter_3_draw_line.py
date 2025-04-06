#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 12:13:15 2025

@author: alpha
"""

import cv2
path='/home/alpha/Desktop/open_cv_program/Untitled.webp'


image=cv2.imread(path)
cv2.imshow('original',image)


imageline=image.copy()


imageline=cv2.line(imageline,(100,100),(100,100),(255,255,255),thickness=25,lineType=cv2.LINE_AA)





cv2.imshow("copy",imageline)



cv2.waitKey(0)
cv2.destroyAllWindows()