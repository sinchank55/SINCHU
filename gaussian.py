import cv2
import numpy as np

img=cv2.imread("C:/Users/User/OneDrive/Pictures/267434.jpg")
img_gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

noise=np.random.normal(0,50,img_gray.shape)

img_noised=img_gray+noise

img_noised=np.clip(img_noised,0,255).astype(np.uint8)

cv2.imshow('Input image',img)
cv2.imshow('Noisy image',img_noised)

cv2.waitKey(0)
cv2.destroyAllWindows()