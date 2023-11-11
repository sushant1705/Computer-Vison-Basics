import cv2 as cv

capture = cv.VideoCapture('Videos\indian_flag_-_44042 (1080p).mp4')
# capture = cv.VideoCapture(0)              captures from webcam
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video' ,frame)
    
    # if cv.waitKey(1)==13:                 stops when Enter is pressed
    if cv.waitKey(20) & 0xFF ==ord('d'):    #stops when d is pressed
        
        break
    
capture.release()
cv.destroyAllWindows()