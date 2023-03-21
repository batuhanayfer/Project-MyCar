import cv2

# Open a connection to the camera
camera = cv2.VideoCapture(0)

# Loop until the user closes the window
while True:
    # Capture a frame from the camera
    ret, frame = camera.read()

    # Display the frame
    cv2.imshow("Camera Feed", frame)

    # Check for a keypress
    key = cv2.waitKey(1) & 0xFF

    # If the 'q' key is pressed, break out of the loop
    if key == ord('q'):
        break

# Release the camera and close the window
camera.release()
cv2.destroyAllWindows()
