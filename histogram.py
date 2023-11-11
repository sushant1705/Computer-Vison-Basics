import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


img  = cv.imread('Photos/dexter.jpg')
cv.imshow('Dexter',img)

grey = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Grey Dexter', grey)



blank = np.zeros(img.shape[:2], dtype='uint8')

mask = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 250,255,-1)
cv.imshow('circle',mask)

masked_img = cv.bitwise_and(grey,grey, mask= mask)
cv.imshow('masked_img',masked_img)

hist = cv.calcHist([grey],[0],None,[256], [0,256])
hist_masked_img = cv.calcHist([masked_img],[0],None,[256], [0,256])

plt.figure() 
plt.title('Histogram')
plt.xlabel('Bins')
plt.ylabel('No. of Pixels')
plt.xlim(0,256)
plt.plot(hist)
plt.show()


plt.figure() 
plt.title('Histogram')
plt.xlabel('Bins')
plt.ylabel('No. of Pixels')
plt.xlim(0,256)
plt.plot(hist_masked_img)
plt.show()


color = ('b', 'g', 'r')

for i,col in enumerate(color):
    histr = cv.calcHist([img],[i], None,[256],[0,256])
    plt.plot(histr,color=col)
    plt.xlim(0,256) 
plt.show()

cv.waitKey(0)