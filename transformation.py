import cv2 as cv
import numpy as np

#  - translate image


img= cv.imread('Photos/cat.jpg')

def translate(img,x,y):
     translateMatrix = np.float32([[1,0,x],[0,1,y]])
     dimensions = (img.shape[1],img.shape[0])
     return cv.warpAffine(img,translateMatrix,dimensions)
 

#  -x -> left
#  -y -> up     
# x -> right
# y -> down

translated = translate(img,100,100)
cv.imshow('translated',translated)
cv.waitKey(0)
 

