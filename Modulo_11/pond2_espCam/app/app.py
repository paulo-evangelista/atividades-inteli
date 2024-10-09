import cv2
import matplotlib.pyplot as plt
import requests
import numpy as np
import time

url1 = r'http://192.168.18.191/capture'
requests.get(url1)

time.sleep(5)
print("---> TOOK PHOTO!")

url2 = r'http://192.168.18.191/saved-photo'
resp = requests.get(url2, stream=True).raw
img = np.asarray(bytearray(resp.read()), dtype="uint8")
img = cv2.imdecode(img, cv2.IMREAD_COLOR)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow("Faces:",cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

cv2.waitKey(0)