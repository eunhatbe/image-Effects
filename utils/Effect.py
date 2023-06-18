from abc import ABC, abstractmethod

import cv2
from PyQt5.QtGui import QPixmap, QImage


class Effect(ABC):

    @abstractmethod
    def apply(self, url: str) -> QPixmap:
        pass


class PencilEffect(Effect):

    def apply(self, url: str):
        if url:
            img = cv2.imread(url, cv2.IMREAD_COLOR)
            img = cv2.GaussianBlur(img, ksize=(9, 9), sigmaX=0)
            gray, color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.05, shade_factor=0.015)

            height, width = gray.shape
            gray_pixmap = QPixmap.fromImage(QImage(gray, width, height, QImage.Format_Grayscale8))
            return gray_pixmap

        return None


class CartoonEffect(Effect):

    def apply(self, url: str):
        pass


if __name__ == "__main__":
    pass