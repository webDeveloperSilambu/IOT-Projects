import cv2
import numpy as np
import time

# Initialize the camera
cap = cv2.VideoCapture(0)  # Use 0 for the default camera

# Parameters for speed calculation
fps = 30  # Frames per second
pixel_to_meter = 0.1  # Conversion factor (adjust as needed)
distance_between_points = 5  # Distance between the two points (in meters)
previous_frame = None
previous_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale for processing
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if previous_frame is not None:
        # Calculate optical flow using Lucas-Kanade method
        flow = cv2.calcOpticalFlowPyrLK(
            previous_frame, gray, None, None, winSize=(15, 15), maxLevel=2
        )

        # Filter out points that have moved
        good_new = flow[:, 0]
        good_old = flow[:, 1]

        # Calculate speed based on the points that moved
        speeds = np.linalg.norm(good_new - good_old, axis=1) * pixel_to_meter / (time.time() - previous_time)
        average_speed = np.mean(speeds)

        # Check if a vehicle has passed the measurement point
        if average_speed > 0:
            print(f"Vehicle speed: {average_speed} m/s")

    previous_frame = gray
    previous_time = time.time()

    # Display the video stream with speed info
    cv2.putText(frame, f"Speed: {average_speed:.2f} m/s", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("Traffic Management System", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
