#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 09:07:14 2025

@author: alpha
"""
from tkinter import*
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk


def file_upload():
    file_path=filedialog.askopenfilename(title="Select an image")
    if file_path:
        img_entry_box.delete(0, END)
        img_entry_box.insert(0, file_path)


def or_img_display():
      if not img_entry_box.get():
         
          alert.config(text="*Please Select image path")
          
      else:
        alert.config(text="")
        img_p=img_entry_box.get()
        img_p=Image.open(img_p)
        img_p.show()
        
        
def img_atrributes():
    if not img_entry_box.get():
       
        alert.config(text="*Please Select image path")
        
    else:
      alert.config(text="")
      img_p=img_entry_box.get()
      img=cv2.imread(img_p)
      w,h,c=img.shape
      print(w,h,c)
      
      
window=Tk()
window.geometry("700x600")

window.title("Image_Processing")

heading=Label(window, text='Computer Vision Project')
heading.pack()
up_label=Label(window,text="Select path of image")
up_label.place(x=30,y=150)
img_entry_box=Entry(window,width=50)
img_entry_box.place(x=150, y=150)

alert=Label(window,text="")
alert.place(x=250,y=175)
upload_button=Button(window,text="Image path",command=file_upload)

upload_button.place(x=515,y=145)

display_button=Button(window,text="Display Original Image",command=or_img_display)
display_button.place(x=200,y=200)

attributes_button=Button(window,text="Image Atrributes",command=img_atrributes)
attributes_button.place(x=200,y=240)
















window.mainloop()

