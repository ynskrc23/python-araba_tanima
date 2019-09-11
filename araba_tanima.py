#!/usr/bin/env python
# coding: utf-8

import cv2
import numpy as np

video = cv2.VideoCapture("C:/Users/KARACA/Downloads/1.mp4")
araba_bulucu = cv2.CascadeClassifier("C:/Users/KARACA/Downloads/cars.xml")

while True:
    ret,kare = video.read()
    griton = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
    arabalar = araba_bulucu.detectMultiScale(griton,1.1,3)
  
    for(x,y,w,h) in arabalar:
        cv2.rectangle(kare,(x,y),(x+w,y+h),(255,0,0),3)
    
    cv2.imshow("video",kare)
  
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    
video.release()
cv2.destroyAllWindows()




