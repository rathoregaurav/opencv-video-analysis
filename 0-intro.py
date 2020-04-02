import cv2
import numpy as np
import matplotlib.pyplot as plt

# IMREAD_GRAYSCALE = 0
# IMREAD_COLOR = 1
# IMREAD_UNCHANGED = -1
img = cv2.imread('road.jpg', cv2.IMREAD_GRAYSCALE)

# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.plot([50, 100], [80, 100], 'c', linewidth=5)
# plt.show()

cv2.imwrite('gray_road.jpg', img)
