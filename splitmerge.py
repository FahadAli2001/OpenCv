import cv2 as cv

#  it takes BGR image and split it into blue green and red


img = cv.imread('Photos/bostan.jpg')
cv.imshow('bostan',img)

b ,g , r = cv.split(img)

cv.imshow('blue',b)
cv.imshow('green',g)
cv.imshow('red',r)

merge = cv.merge([b,g,r])
cv.imshow('merge',merge)


cv.waitKey(0)