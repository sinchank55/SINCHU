import cv2
import numpy as np


def convolution_filter(gray_img, kernel):
    # temporary operation
    # gray_img = cv2.resize(gray_img, (10, 10))

    kernel_size = len(kernel)

    row = gray_img.shape[0] - kernel_size + 1
    col = gray_img.shape[1] - kernel_size + 1

    result = np.zeros(shape=(row, col))

    for i in range(row):
        for j in range(col):
            current = gray_img[i:i+kernel_size, j:j+kernel_size]
            multiplication = np.abs(sum(sum(current * kernel)))
            result[i, j] = int(multiplication)

    return result


img=cv2.imread("D:/Sinchu documents/NCC/SUO SINCHAN KARMAKAR.JPG")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#-------- Edge detection operator-----
## robertX = [[1, 0], [0, -1]]
## robertY = [[0, 1], [-1, 0]]
##
## prewittX = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]
## prewittY = [[1, 1, 1], [0, 0, 0], [-1, -1, -1]]
##
# sobelX = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
# sobelY = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
##
laplacian = [[0, 1, 0],[1, -4, 1],[0, 1, 0]]
#-------- Edge detection operator-----

#-------- Image Enhancement using filter -----
#sharpen = [[0, -1, 0],[-1, 5, -1],[0, -1, 0]]

## avg = (1/9)*[[1, 1, 1], [1, 1, 1], [1, 1, 1]]

sharp = convolution_filter(gray, laplacian)


cv2.imshow('Input image', gray)
cv2.imshow('Sharp Image', sharp)


cv2.waitKey(0)
cv2.destroyAllWindows() 
