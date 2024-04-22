# AI- Project : Face Recognition System


Working:

Initialization:
				The code starts by loading known face images and their corresponding names. This is typically done offline during a setup phase where known individuals' faces are captured and their face encodings are computed and stored.
The load_known_faces() function is responsible for this initialization step. It loads known face images, computes their encodings using the face_recognition library, and stores them in lists.
Face Recognition Loop:
			After the initialization, the code enters a loop where it continuously captures frames from a video stream, typically from a webcam.
Within each iteration of the loop, it detects faces in the current frame using the face_recognition library. This library uses pre-trained deep learning models to detect faces in images efficiently.
For each detected face, the library also computes a numerical encoding that represents the face's characteristics.
Comparison with Known Faces:
			The code then compares these computed face encodings with the encodings of known faces that were loaded during initialization.
This is done by iterating over the known face encodings and using a distance metric to measure the similarity between the computed encoding and each known encoding.
If a match is found (i.e., if the distance between the computed encoding and a known encoding is below a certain threshold), the code assigns the corresponding name to the detected face.
Displaying Results:
			For each detected face, the code draws a rectangle around the face region in the frame and labels it with the recognized name.
This is done using OpenCV (cv2) functions to draw rectangles and text on the frame.
Real-Time Processing:
			The loop continues this process in real-time, capturing frames, detecting faces, comparing them with known faces, and labeling them accordingly.


Result:
			The result of running this code is a real-time face recognition system that can identify known faces in a video stream from a webcam. As the system runs, it continuously processes incoming video frames, detecting faces within each frame, and comparing them with the known faces stored in its database. When a known face is detected, it labels the face with the corresponding name in the video stream.
The output of the code is typically a window displaying the video feed from the webcam, with rectangles drawn around detected faces and their corresponding names overlaid on top of the rectangles. This provides a visual indication of which known individuals are currently present in the video stream.

