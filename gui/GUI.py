import sys
import os

from PyQt5.QtCore import Qt, QSize, QTimer, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, qApp, QFileDialog, QLabel, QVBoxLayout, \
    QMessageBox, QProgressBar
from PyQt5.QtGui import QPixmap, QImage

import cv2
from PyQt5.uic.properties import QtCore

from utils.EffectApplier import EffectApplier
from utils.Effect import Effect, PencilEffect

class App(QMainWindow):
    x = 400
    y = 100
    width = 800
    height = 600

    def __init__(self) -> None:
        super().__init__()

        self.progress_bar = QProgressBar(self)
        self.timer = QTimer(self)
        self.progress = 0


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
        # effect init


        # action menu event
        self.pencil_img_action = QAction("연필 모드")
        # self.pencil_img_action.triggered.connect(self.draw_pencil)  # 연필 그리기 액션

        self.pencil_img_action.triggered.connect(lambda : self.apply_effect(PencilEffect()))

        # action menu 생성
        action_menu = self.menu_bar.addMenu("실행")
        action_menu.addAction(self.pencil_img_action)


        # ProgressBar 초기화
        self.progress_bar.setGeometry(10, 550, 780, 30)
        self.progress_bar.setValue(0)

        self.show()

    # 파일 로드
    def load_file_action(self):
        file_info = QFileDialog.getOpenFileName(self)  # 선택한 이미지 정보
        self.img_url = file_info[0]  # 파일 경로

        if self.is_valid_image(self.img_url):
            self.draw_img()  # 이미지 띄우기
        elif self.img_url == '':    # 이미지를 선택하지 않았다면 (아무것도 선택하지 않고 닫는다면)
            return
        else:
            QMessageBox.about(self, "error", "이미지 파일을 선택해주세요.")

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

    # 기능 적용 메서드
    def apply_effect(self, effect):
        # 이미지가 선택되었을 경우
        if self.img_url:
            self.effect_worker = EffectWorker(self.effect_manager, effect, self.img_url)
            self.effect_worker.processingFinished.connect(self.handle_processing_finished)
            self.effect_worker.start()
        else:
            QMessageBox.about(self, "error", "이미지를 선택해주세요")

    # 메인 스레드 ui 작업
    def handle_processing_finished(self, success, pix_map):
        if success:
            self.img_label.setPixmap(pix_map.scaled(self.width, self.height, Qt.KeepAspectRatio))
        else:
            print("pixmap error")


    # 이미지 파일 유효성 검사
    def is_valid_image(self, file_path):
        valid_extensions = [".png", ".jpg", ".jpeg", ".gif", ".bmp"]  # 허용하는 이미지 확장자
        file_extension = os.path.splitext(file_path)[1].lower()  # 파일 확장자 추출

        return file_extension in valid_extensions



    #  프로그레스바 처리
    def update_progress_bar(self):
        pass


# 이미지 처리를 위한 스레드
class EffectWorker(QThread):
    processingFinished = pyqtSignal(bool, QPixmap)

    def __init__(self, effect_manager, effect, img_url):
        super().__init__()
        self.effect_manager = effect_manager
        self.effect = effect
        self.img_url = img_url

    def run(self):
        pix_map = self.effect_manager.render(self.effect, self.img_url)
        self.processingFinished.emit(pix_map is not None, pix_map)

