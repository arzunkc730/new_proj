#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 12:24:05 2025

@author: alpha
"""

import cv2 
import numpy as np 
import matplotlib.pyplot as plt 


path='/home/alpha/Desktop/open_cv_program/Untitled.webp'

image =cv2.imread(path)

image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


r,g,b=cv2.split(image)


plt.figure(figsize=(10,4))

plt.subplot(1,3,1)
plt.imshow(r,cmap="Reds")
plt.title('Red Channel')


plt.subplot(1,3,2)
plt.imshow(g,cmap="Greeens")
plt.title('Green Channel')

plt.subplot(1,3,3)
plt.imshow(b,cmap="Blues")
plt.title('Blue Channel')

plt.show