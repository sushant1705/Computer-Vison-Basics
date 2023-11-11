import cv2 as cv
import numpy as np

blank = np.zeros((600,600,3), dtype='uint8')
# cv.imshow("Blank", blank)

# Steps:
# 1.Paint the image a certain color
# blank[:]= 0,0,255                 colors whole page 
blank[200:300,300:400]= 0,0,255     #colors a particular section of the page
#array slicing of image img[height_line on y axis, width_line on x axis]


# 2.Draw Rectangle
cv.rectangle(blank, (0,0), (300,200), (255,0,0),thickness=2)

# 3.Draw Circle
cv.circle(blank, (300,500), 40, (205,100,0),thickness=-1)

# 4.Draw line
cv.line(blank, (0,0), (300,500), (255,250,250),thickness=2)

# 4.Write Text
cv.putText(blank, 'Hello World', (100,250),cv.FONT_HERSHEY_TRIPLEX, 1.0, (120,120,250),2)

cv.imshow('Red',blank)
cv.waitKey(0)