from gui.GUI import *

if __name__ == "__main__":
    # gui 생성
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())  # 앱이 종료될 떄까지 대기