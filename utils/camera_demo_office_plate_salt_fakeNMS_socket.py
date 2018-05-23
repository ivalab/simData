import sys
import time
import math
import cv2
import numpy as np

sys.path.append('./')

def colorDetect(image):

        # create NumPy arrays from the boundaries
        lower = np.array([160, 10, 10], dtype="uint8")
        upper = np.array([255, 160, 160], dtype="uint8")

        # find the colors within the specified boundaries and apply the mask
        mask = cv2.inRange(image*255, lower, upper)
        output = cv2.bitwise_and(image, image, mask=mask)

        coordinates = np.where(mask == 255)

        x_mean = np.mean(coordinates[0])
        y_mean = np.mean(coordinates[1])

        # if not math.isnan(x_mean):
        #     x_mean = int(x_mean)
        #     y_mean = int(y_mean)
        #     cv2.circle(output, (y_mean, x_mean), 1, (0, 255, 0), 2)

        # show the images
        cv2.imshow("images", np.hstack([image, output]))
        cv2.waitKey(1000)

        cv2.imwrite("test.png", image)
        cv2.imwrite("test_seg.png", output)
        return y_mean-10, x_mean-10, y_mean+10, x_mean+10


np_img = cv2.imread('data/004.png')
resized_img = cv2.resize(np_img, (448, 448))
#np_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)
colorDetect(resized_img)

print('done')









