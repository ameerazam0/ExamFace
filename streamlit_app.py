import cv2
import numpy as np
import datetime
import streamlit as st
st.title("Exam Attention")
# Load HAAR face classifier
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def tic():
    x = datetime.datetime.now()
    return str(x)
run = st.checkbox('Run to On the Camera')
FRAME_WINDOW = st.image([])
cap = cv2.VideoCapture(0)
count=0
def face_extractor(img):
    # Function detects faces and returns the cropped face
    # If no face detected, it returns the input image
    faces = face_classifier.detectMultiScale(img, 1.3, 5)

    if faces is ():
        return None

    # Crop all faces found
    for (x,y,w,h) in faces:
        x=x-10
        y=y-10
        cropped_face = img[y:y+h+50, x:x+w+50]

    return cropped_face
while run:
    ret, frame = cap.read()
    if face_extractor(frame) is not None:
        count+=1
        face = cv2.resize(face_extractor(frame), (400, 400))
        cv2.rectangle(frame,(90,45),(50,20),(0,255,0),6)
        cv2.putText(face, tic(), (30, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 1)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(face)
    else:
        cv2.putText(face, tic(), (30, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 1)
        cv2.putText(face, 'Face Not On Camera', (40, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 5)
        FRAME_WINDOW.image(face)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break


if st.button('close Camera'):
        cap.release()
        cv2.destroyAllWindows()
st.write('Stopped')
