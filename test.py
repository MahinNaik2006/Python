from sklearn.neighbors import KNeighborsClassifier


import cv2
import pickle
import numpy as np
import os
video=cv2.VideoCapture(0)
facedetect=cv2.CascadeClassifier('data/file.xml')

with open('data/names.pkl', 'rb') as f:
    LABLES = pickle.load(f)
with open('data/faces_data.pkl', 'rb') as f:
    Faces=pickle.load(f)

model = KNeighborsClassifier(5)
model.fit(Faces,LABLES)

while True:
    ret,frame=video.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=facedetect.detectMultiScale(gray, 1.3 ,5)
    for (x,y,w,h) in faces:
        crop_img=frame[y:y+h, x:x+w, :]
        resized_img=cv2.resize(crop_img, (50,50)).flatten().reshape(1,-1)
        output = model.predict(resized_img)
        cv2.putText(frame,str(output[0]),(x,y+15) ,cv2.FONT_HERSHEY_DUPLEX,1,(225,225,225),3)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (50,50,255), 1)
    cv2.imshow("Frame",frame)
    k=cv2.waitKey(1)
    if k==ord('q'):
        break
video.release()
cv2.destroyAllWindows()
