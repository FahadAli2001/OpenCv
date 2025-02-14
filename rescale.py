import cv2 as cv



# ----Resize and Rescale 

def rescaleFrame(framse,scale=0.96):
    # for images, videos and live video
    width = int(framse.shape[1]*scale) # 1 for width
    height = int(framse.shape[0]*scale) # 0 for height
    dimensions = (width,height)
    return cv.resize(framse,dimensions,interpolation=cv.INTER_AREA)

cap = cv.VideoCapture('Videos/cat.mp4') # 0 for web camera
while True:
    success, frame = cap.read()
    resized = rescaleFrame(frame)
    cv.imshow('video',frame)
    cv.imshow('resized',resized)
    if cv.waitKey(1) & 0xFF == ord('q'): # means press q to exit
        break

cap.release()
cv.destroyAllWindows()