import cv2 as cv
import os 
import numpy as np


class Camera:
    def __init__(self):
     self.video = cv.VideoCapture(0)

    def detect_faces(self):
     while True:
        reet, frame = self.video.read()
        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        haar_cascade = cv.CascadeClassifier('haar_face.xml')
        faces_rect = haar_cascade.detectMultiScale(gray_frame ,scaleFactor=1.1, minNeighbors=3) 

        for (x,y,w,h) in faces_rect:
            cv.rectangle(frame,(x,y), (x + w, y + h), (0,0,255), thickness=2)

        cv.imshow('name of video', frame)

        if cv.waitKey(20) & 0xFF==ord('d'):    
            break

            
       

camera1 = Camera()
camera1.detect_faces()


