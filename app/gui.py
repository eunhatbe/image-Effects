import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, qApp, QFileDialog, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap

import drawing

class App(QMainWindow):
    x = 400
    y = 100
    width = 800
    height = 600

    def __init__(self) -> None:
        super().__init__()

        self.img_url = None     # 이미지 경로
        self.init_ui()


    def init_ui(self):
        # 윈도우 세팅
        self.setWindowTitle('Pencil drawing')
        self.move(App.x, App.y)
        self.resize(App.width, App.height)

        # 이미지 영역 세팅
        self.img_label = QLabel("Test",self)
        self.img_label.move(30, 30)
        self.img_label.resize(400, 20)   # 길이, y좌표

        # 메뉴바 세팅
        self.menu_bar = self.menuBar()
        self.menu_bar.setNativeMenuBar(False)

        # file menu 액션
        self.new_action = QAction("파일 불러오기")
        self.new_action.triggered.connect(self.file_load_action)

        self.quit_action = QAction("종료")
        self.quit_action.triggered.connect(qApp.quit) # 종료

        # file menu 생성
        file_menu = self.menu_bar.addMenu("파일")
        file_menu.addAction(self.new_action)
        file_menu.addSeparator()
        file_menu.addAction(self.quit_action)

        # action menu 생성
        action_menu = self.menu_bar.addMenu("실행")

        self.show()

    # 파일 로드
    def file_load_action(self):
        fname = QFileDialog.getOpenFileName(self)   # 선택한 이미지 정보
        self.img_url = fname[0]                     # 파일 경로
        self.draw_img()                             # 이미지 띄우기
        self.show_url(fname)                        # Test code

    # 파일을 선택하면 이미지를 그림
    def draw_img(self):
        if self.img_url:
            pixmap = QPixmap(self.img_url)
            # 윈도우 비율에 맞게 이미지 크기 조정
            self.img_label.setPixmap(QPixmap(pixmap).scaled(self.width,self.height, Qt.KeepAspectRatio))
            self.img_label.resize(400,400)


    def show_url(self, fname):
        # self.url_label.setText(self.img_url)
        pass
