import cv2 as cv

img = cv.imread('Photos/indian_flag.png')
cv.imshow('India', img)

cv.waitKey(0)