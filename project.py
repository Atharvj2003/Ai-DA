import numpy as np
import cv2
import face_recognition

# Load known faces
known_face_encodings = []
known_face_names = []

# Load images and encode known faces
def load_known_faces():
    # Load images and names
    # Example:
    # known_image = face_recognition.load_image_file("known_face.jpg")
    # known_encoding = face_recognition.face_encodings(known_image)[0]
    # known_face_encodings.append(known_encoding)
    # known_face_names.append("Name")

# Function to recognize faces in a video stream
def recognize_faces():
    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()

        # Find all face locations and encodings in the frame
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        # Loop through each face found in the frame
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Compare face encoding with known faces
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

            name = "Unknown"

            # If a match is found, use the name associated with it
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            # Draw a rectangle around the face and label it with the name
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Video', frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    load_known_faces()
    recognize_faces()
