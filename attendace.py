import face_recognition
import os
import cv2 as cv
import csv
import numpy as np
from datetime import datetime as dt


#taking input frm webcam

video_capture = cv.VideoCapture(0)   

# Directory containing known faces
known_faces_dir = "known"

# Load known faces
known_faces = []
known_names = []
# train model
for person_name in os.listdir(known_faces_dir):
    person_folder = os.path.join(known_faces_dir, person_name)
    if os.path.isdir(person_folder):
        for filename in os.listdir(person_folder):
            if filename.endswith(".jpeg"):
                image_path = os.path.join(person_folder, filename)
                image = face_recognition.load_image_file(image_path)
                face_encoding = face_recognition.face_encodings(image)[0]
                known_faces.append(face_encoding)
                known_names.append(person_name)


known_face_encodings={
    name: encoding for (name, encoding) in zip(known_names, known_faces)
}
students = known_names.copy()

#taking current date
now = dt.now()
current_date = now.strftime("%d-%m-%Y")

#creating csv

f = open(current_date+'.csv', 'w+',newline = '')
linewriter = csv.writer(f)


while True:
    ret, frame = video_capture.read()  # read a frame from camera   
    small_frame =cv.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame = cv.cvtColor(small_frame, cv.COLOR_BGR2RGB)
    
    if True:
        # Find video capture face locations and face encodings 
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations) 
        face_names=[]
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = ''
            face_distances = face_recognition.face_distance(known_face_encodings , face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_names[best_match_index]

            face_names.append(name)
            if name in known_names:
                if name in students:
                    students.remove(name)
                    print(students)
                    current_time = now.strftime("%H-%M-%S")
                    linewriter.writerow([name,current_time])
    cv.imshow("Attendance System", frame)
    if cv.waitKey(1)==13:  
        break
video_capture.release()
cv.destroyAllWindows()
f.close()


