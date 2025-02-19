# color spaces converting image to diff color space
#  can not convert greyscale directly to hsv we have to convrt to bgr first
import cv2 as cv

img = cv.imread('Photos/cat.jpg')

# BGR to    Grey

grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('grey',grey)

# BGR TO HSV (hue Saturation Value)

hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)

# BGR TO L *A*B (lightness, a, b)

lab = cv.cvtColor(img,cv.COLOR_BGR2LAB) 
cv.imshow('lab',lab)

#  BGR TO RGB

rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)

cv.waitKey(0)
cv.destroyAllWindows()