import cv2 as cv

img = cv.imread('Photos/bostan.jpg')
cv.imshow('bostan',img)

# averging {define kernal on a specfic area}

avg = cv.blur(img,(3,3))
cv.imshow ("avg",avg)   


cv.waitKey(0)


