import numpy as np
import cv2
img=cv2.imread("C:/Users/User/Pictures/Camera Roll/WIN_20231202_12_42_35_Pro.jpg")
h,w,c = img.shape
R,G,B=cv2.split(img)
gray = np.zeros([h, w], dtype=np.uint8)
for i in range(h):
    for j in range(w):
        gray[i, j] = int(R[i, j] * 0.114 + G[i, j] * 0.587 + B[i, j] * 0.299)
cv2.imshow('Gray image',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()