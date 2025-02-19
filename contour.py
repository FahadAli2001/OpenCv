# boundries of object that join line or curve

import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpg')

grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('grey',grey)

canny = cv.Canny(grey,150,200)
cv.imshow('canny',canny)

blank = np.zeros(img.shape,dtype=np.uint8)
cv.imshow('blank',blank)


contours , hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print (len(contours))

cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('contours',blank)
cv.waitKey(0)

 

 