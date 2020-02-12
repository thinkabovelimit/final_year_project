import cv2
import numpy as np
image=cv2.imread('image5.jpeg')
cv2.imshow('original',image)
#cv2.waitKey(0)
dst=cv2.fastNlMeansDenoisingColored(image,None,6,6,7,21)
cv2.imshow('denoised image',dst)
cv2.waitKey(0)
