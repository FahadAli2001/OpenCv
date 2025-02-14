import cv2 as cv

# ---- convert photo to grey scale

img = cv.imread('Photos/park.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# ------- Blur

blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT) # 7 for blur 
cv.imshow('blur',blur)


# ------ Edges

canny = cv.Canny(img,125,200)
cv.imshow('canny',canny)

# --- dialated image
dialated = cv.dilate(canny,(7,7),iterations=3)
cv.imshow('dialated',dialated)

# ------eroded image
erod = cv.erode(dialated,(7,7),iterations=3)
cv.imshow('erod',erod)
cv.waitKey(0)