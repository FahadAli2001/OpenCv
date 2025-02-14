import cv2 as cv
import numpy as np

# ----------- for image read

# img= cv.imread('Photos/cat.jpg')
# cv.imshow('image',img)
# cv.waitKey(0)

# -------------- for video read

# cap = cv.VideoCapture('Videos/cat.mp4') # 0 for web camera
# while True:
#     success, img = cap.read()
#     cv.imshow('video',img)
#     if cv.waitKey(1) & 0xFF == ord('q'): # means press q to exit
#         break

# cap.release()
# cv.destroyAllWindows()

# -------------- for horizontal 2 image

img = cv.imread('Photos/cat.jpg')
re_image = cv.resize(img,(300,300))
horizontal_img = np.hstack((re_image,re_image))

cv.imshow('horizontal',horizontal_img)
cv.waitKey(0)


