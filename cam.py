import cv2

# Create a VideoCapture object to capture video from the camera
cap = cv2.VideoCapture(1)  # 0 represents the default camera, you can change it if you have multiple cameras

scale = 1

while True:
    ret, frame = cap.read()  # Read a frame from the camera

    frame = cv2.resize(frame, None, fx=scale, fy=scale)

    cv2.imshow('Camera', frame)  # Display the frame in a window named 'Camera'

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit the program
        break
    elif cv2.waitKey(1) & 0xFF == ord('s'):
        scale = float(int(input('enter scale factor: ')))


# Release the VideoCapture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()