import time
import random
from enum import Enum

import cv2

# viedo
# cap = cv2.VideoCapture()

# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

class InputKey(Enum):
    ESC = 27
    SAVE = 's'

def wait_key():
    input_key = cv2.waitKey(0)

    if input_key == InputKey.ESC.value:
        cv2.destroyAllWindows()
    elif input_key == ord(InputKey.SAVE.value):  # 's' key
        cv2.imwrite('pencilcity.png', gray)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    img = cv2.imread('city.png', cv2.IMREAD_COLOR)
    img = cv2.GaussianBlur(img, ksize=(9, 9), sigmaX=0)

    gray, color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.05, shade_factor=0.015)

    # cv2.imshow('Original', img)
    cv2.imshow('gray', gray)

    wait_key()





