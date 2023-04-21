import cv2

# cap = cv2.VideoCapture(0)
# ret, frame = cap.read()

# cv2.imshow('frame',frame)

# initialize the video capture object
capture = cv2.VideoCapture(0)
# check if the capture was successful
if not capture.isOpened():
    raise Exception("Could not open video device")

# read a frame from the video capture object
ret, frame = capture.read()
if frame is not None:
    print('showing frame')
    cv2.imshow('Frame', frame)
    cv2.waitKey(1)

# check if the frame was read successfully
if not ret:
    raise Exception("Could not read frame from video device")


#show the frame
cv2.imshow("frame", frame)
#wait for keypress
cv2.waitKey(0)

# save the frame to disk as a PNG image
cv2.imwrite("captured_image.png", frame)

# release the video capture object and close the window
capture.release()
cv2.destroyAllWindows()
