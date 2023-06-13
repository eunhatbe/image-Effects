import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, qApp, QFileDialog, QLabel, QVBoxLayout, \
    QMessageBox, QProgressBar
from PyQt5.QtGui import QPixmap, QImage

import cv2

from utils.EffectApplier import EffectApplier


class App(QMainWindow):
    x = 400
    y = 100
    width = 800
    height = 600

    def __init__(self) -> None:
        super().__init__()


        self.effect_manager = EffectApplier()
        self.img_url = None  # 이미지 경로
        self.init_ui()


    def init_ui(self):
        # 윈도우 세팅
        self.setWindowTitle('Pencil drawing')
        self.move(App.x, App.y)
        self.resize(App.width, App.height)
        self.setFixedSize(QSize(App.width, App.height))

        # 이미지 영역 세팅
        self.img_label = QLabel(self)
        self.img_label.move(200, 50)  # 이미지 영역 좌표
        self.img_label.resize(400, 500)  # 이미지 크기

        # 메뉴바 세팅
        self.menu_bar = self.menuBar()
        self.menu_bar.setNativeMenuBar(False)

        ################################################################################################################
        # 파일 메뉴 생성
        ################################################################################################################
        # file menu event
        self.file_action = QAction("파일 불러오기")
        self.file_action.triggered.connect(self.load_file_action)

        self.quit_action = QAction("종료")
        self.quit_action.triggered.connect(qApp.quit)  # 종료

        # file menu 생성
        file_menu = self.menu_bar.addMenu("파일")
        file_menu.addAction(self.file_action)
        file_menu.addSeparator()  # 경계선 생성
        file_menu.addAction(self.quit_action)

        ################################################################################################################
        # 실행 메뉴 생성
        ################################################################################################################
        # action menu event
        self.pencil_img_action = QAction("연필 모드")
        # self.pencil_img_action.triggered.connect(lambda: pencil_draw(self.img_url)) # 연필 그리기 액션 테스트 코드
        self.pencil_img_action.triggered.connect(self.draw_pencil)  # 연필 그리기 액션

        #self.pencil_img_action.triggered.connect(self.effect_manager.render())


        # action menu 생성
        action_menu = self.menu_bar.addMenu("실행")
        action_menu.addAction(self.pencil_img_action)

        # ProgressBar 생성
        self.bar = QProgressBar(self)
        self.bar.setGeometry(10, 550, 780, 30)

        self.show()

    # 파일 로드
    def load_file_action(self):
        file_info = QFileDialog.getOpenFileName(self)  # 선택한 이미지 정보
        self.img_url = file_info[0]  # 파일 경로
        self.draw_img()  # 이미지 띄우기

        # self.show_url(fname)                        # Test code

    # 파일을 선택하면 이미지를 그림
    def draw_img(self):
        if self.img_url:
            pixmap = QPixmap(self.img_url)
            # 윈도우 비율에 맞게 이미지 크기 조정
            self.img_label.setPixmap(QPixmap(pixmap).scaled(self.width, self.height, Qt.KeepAspectRatio))

    def show_url(self, fname):
        # self.url_label.setText(self.img_url)
        pass

    # 연필 그리기 기능
    def draw_pencil(self):
        # 이미지 선택 판별

        if self.img_url:
            img = cv2.imread(self.img_url, cv2.IMREAD_COLOR)
            img = cv2.GaussianBlur(img, ksize=(9, 9), sigmaX=0)
            gray, color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.05, shade_factor=0.015)

            # cv2 img size
            height, width = gray.shape

            # cv2로 수정한 파일을 pixmap 으로 다시 변환
            gray_pixmap = QPixmap.fromImage(QImage(gray, width, height, QImage.Format_Grayscale8))
            self.img_label.setPixmap(gray_pixmap.scaled(self.width, self.height, Qt.KeepAspectRatio))
        else:
            QMessageBox.about(self, "error", "이미지를 선택해주세요")

    #  프로그레스바 처리
    def update_progress_bar(self):
        pass


    def apply_effect(self):
        pass
