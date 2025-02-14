import cv2 as cv
import numpy as np

# -----------draw black image

# black = np.zeros((500,500),dtype= np.uint8)#unit8 for image dataType
# cv.imshow("black",black)

# ---------- paint a image with color

# blank = np.zeros((500,500,3),dtype = np.uint8) # 3 for color

# blank[:] = 0,0,200 #  blank[:] select all pixels
# cv.imshow("blank",blank)

# -------  draw rectangle 

blank = np.zeros((600,600,3),dtype=np.uint8)

cv.rectangle(blank,(0,0),(300,300),(0,255,255),thickness=-1 ) # thickness = -1 for fill the rectangle
cv.circle(blank,(300,300),100,(255,0,255),thickness=3)
cv.line(blank,(0,0),(300,300),(0,255,0),thickness=3)
cv.putText(blank,"hello", (300,300),cv.FONT_HERSHEY_TRIPLEX,2.0,(255,255,255),2)
cv.imshow("Blank",blank)


cv.waitKey(0)