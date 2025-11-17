from sklearn.neighbors import KNeighborsClassifier
import cv2
import pickle
import os
import csv
import time
from datetime import datetime
from win32com.client import Dispatch

def speak(str1):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(str1)

video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier('data/frontface.xml')

with open('data/names.pkl', 'rb') as w:
    LABELS = pickle.load(w)
with open('data/faces_data.pkl', 'rb') as f:
    FACES = pickle.load(f)

print('Shape of Faces matrix --> ', FACES.shape)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(FACES, LABELS)

# Load new corrected background
imgBackground = cv2.imread("C:/Users/Mahin/Downloads/ChatGPT Image Nov 17, 2025, 09_23_38 PM.png")

# Black box exact placement (measured)
BOX_X = 402
BOX_Y = 400
BOX_W = 820
BOX_H = 510

COL_NAMES = ['NAME', 'TIME']

while True:
    ret, frame = video.read()

    # Resize camera feed to perfectly fit the box
    frame_resized = cv2.resize(frame, (BOX_W, BOX_H))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)

    attendance = None
    for (x, y, w, h) in faces:
        crop_img = frame[y:y + h, x:x + w, :]
        resized_img = cv2.resize(crop_img, (50, 50)).flatten().reshape(1, -1)
        output = knn.predict(resized_img)

        ts = time.time()
        date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
        timestamp = datetime.fromtimestamp(ts).strftime("%H:%M-%S")
        exist = os.path.isfile("Attendance/Attendance_" + date + ".csv")

        # Draw face box
        cv2.rectangle(frame_resized, (x, y), (x + w, y + h), (50, 50, 255), 2)
        cv2.putText(frame_resized, str(output[0]), (x, y - 15),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)

        attendance = [str(output[0]), str(timestamp)]

    # Put camera feed into background template
    imgBackground[BOX_Y:BOX_Y + BOX_H, BOX_X:BOX_X + BOX_W] = frame_resized

    cv2.imshow("Attendance System", imgBackground)

    k = cv2.waitKey(1)

    if k == ord('o') and attendance is not None:
        speak("Attendance Taken")
        time.sleep(1)

        if exist:
            with open("Attendance/Attendance_" + date + ".csv", "+a") as csvfile:
                csv.writer(csvfile).writerow(attendance)
        else:
            with open("Attendance/Attendance_" + date + ".csv", "+a") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(COL_NAMES)
                writer.writerow(attendance)

    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
