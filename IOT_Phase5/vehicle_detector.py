import cv2 

import numpy as np 

# Load the pre-trained vehicle detection model 

vehicle_cascade = cv2.CascadeClassifier('haarcascade_car.xml') 


# Open a video stream from a camera (0 for the default camera) 

cap = cv2.VideoCapture(0) 

while True: 

    ret, frame = cap.read() 

  

    if not ret: 

        break 

  

    # Convert the frame to grayscale for vehicle detection 

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

  

    # Detect vehicles in the frame 

    vehicles = vehicle_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)) 

  

    # Draw rectangles around detected vehicles 

    for (x, y, w, h) in vehicles: 

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) 

  

    # Display the frame with detected vehicles 

    cv2.imshow('Vehicle Detection', frame) 

  

    # Exit the program on 'q' key press 

    if cv2.waitKey(1) & 0xFF == ord('q'): 

        break 

   # Release the video stream and close OpenCV windows 

     cap.release() 

     cv2.destroyAllWindows() 
