import cv2 as cv


img  = cv.imread('Photos/dexter.jpg')
cv.imshow('Dexter',img)


# converting into grey scale
grey = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Grey Dexter', grey)

# blur image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT) #keep it odd like 7,7
cv.imshow('Blur Dexter', blur)



# edge cascade
canny = cv.Canny(img, 125,175)
cv.imshow('Cascade Dexter', canny)



# Dialate the image
dilated = cv.dilate(img, (7,7) , iterations=3)
cv.imshow('Dialate Dexter', dilated)


# Erode the image
eroded = cv.erode(dilated, (17,17) , iterations=1)
cv.imshow('Eroded Dexter', eroded)


# Resize the image
res = cv.resize(img, (500,500) ,interpolation=cv.INTER_CUBIC)
cv.imshow('Resized Dexter', res)
# What is interpolation in cv2?
# Interpolation is the way the extra pixels in the new image is calculated.

# Cropping the image
cropped = img[0:200, 200:1500] #array slicing of image img[height_line on y axis, width_line on x axis]
cv.imshow('Cropped Dexter', cropped)

cv.waitKey(0)