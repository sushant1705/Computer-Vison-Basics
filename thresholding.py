import cv2 as cv


img  = cv.imread('Photos/dexter.jpg')
cv.imshow('Dexter',img)

grey = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Grey Dexter', grey)
# simple threshold 
threshold,thresh = cv.threshold(grey,150,255,cv.THRESH_BINARY)
cv.imshow('Threshold Dexter', thresh)

threshold,thresh_inv = cv.threshold(grey,150,255,cv.THRESH_BINARY_INV)
cv.imshow('Threshold Dexter', thresh_inv)


# adaptive threshold
adaptiveThresh = cv.adaptiveThreshold(grey,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,1)
cv.imshow('Adaptive Threshold Dexter', adaptiveThresh)

cv.waitKey(0)