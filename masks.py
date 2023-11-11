import cv2 as cv
import numpy as np


img  = cv.imread('Photos/dexter.jpg')
cv.imshow('Dexter',img)

blank = np.zeros(img.shape[:2], dtype='uint8')

mask = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 250,255,-1)
cv.imshow('circle',mask)

maskrect = cv.rectangle(blank.copy(),(img.shape[1]//5, img.shape[0]//5),(img.shape[1]//2, img.shape[0]//2),255,-1)
cv.imshow('Rectangle',maskrect)

bitwiseand = cv.bitwise_and(maskrect,mask)
cv.imshow('bitwiseand',bitwiseand)



maskedimg = cv.bitwise_and(img, img , mask=mask)
cv.imshow('MAsked IMg' , maskedimg)

cv.waitKey(0)