import cv2 as cv


# rescaling images, videos and live videos
def rescale(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimension = (width,height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


# changing resolution works only for live videos
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)


capture = cv.VideoCapture('Videos\indian_flag_-_44042 (1080p).mp4')
while True:
    isTrue, frame = capture.read()
    
    frame_resized = rescale(frame)
    
    # resized video
    cv.imshow('Video_Resized' ,frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):     
        break
    


capture.release()
cv.destroyAllWindows()


img_resized = cv.imread('Photos/indian_flag.png')

cv.imshow("Resized Image", img_resized)

cv.waitKey(0)
