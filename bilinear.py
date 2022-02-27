from PIL import Image
import cv2
import matplotlib.pyplot as plt
import math
import numpy as np

if __name__ == '__main__':
    img = cv2.imread('qr-polar.png', cv2.IMREAD_GRAYSCALE)
    qr_coordinate = np.zeros([1007, 1007])
    for i in range(1006):
        for j in range(1006):
            x, y = i * math.cos(j / 503 * math.pi) + 1006, i * math.sin(j / 503 * math.pi) + 1006
            int_x, int_y = math.floor(x), math.floor(y)
            delta_x, delta_y = x - int_x, y - int_y
            qr_coordinate[j][i] = delta_x * delta_y * img[int_y][int_x] + delta_x * (1-delta_y) * img[int_y+1][int_x] + (1-delta_x) * delta_y * img[int_y][int_x+1] + (1-delta_x) * (1-delta_y) * img[int_y+1][int_x+1]
    plt.imshow(np.flipud(qr_coordinate), cmap ="gray")
    plt.axis('off')
    plt.show()