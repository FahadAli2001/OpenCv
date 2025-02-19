import os
import cv2 as cv

list_images = os.listdir(r"E:\python\OpenCv\Photos")
# print(list_images)


for name in list_images:
    images = cv.imread(f'Photos/{name}')
    images = cv.resize(images,(500,500))
    cv.imshow(name,images)
    cv.waitKey(2000)
    cv.destroyWindow(name)
    

    
    