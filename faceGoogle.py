import face_recognition
from googlesearch import search
import os

# Load the target image
target_image = face_recognition.load_image_file("unknowm\images (3).jpeg")
target_face_encoding = face_recognition.face_encodings(target_image)[0]

# Load known face encodings and names
# known_face_encodings = [encoded_image1, encoded_image2]  # Add your known face encodings
# known_face_names = ["Person 1", "Person 2"]  # Add corresponding names


# Directory containing known faces
known_faces_dir = "known"

# Load known faces
known_faces_encodings = []
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
                known_faces_encodings.append(face_encoding)
                known_names.append(person_name)

# Compare the target face encoding with known face encodings
results = face_recognition.compare_faces(known_faces_encodings, target_face_encoding)

name = "Unknown"  # Default name if no match is found

# If a match is found, assign the corresponding name
if True in results:
    match_index = results.index(True)
    name = known_names[match_index]

# Perform a Google search with the recognized name
query = f"Search for {name}"
print(query)
for result in search(query, num=10, stop=5):
    print(result)
