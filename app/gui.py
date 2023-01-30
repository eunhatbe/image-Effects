import sys
from PyQt5.QtWidgets import QApplication, QWidget

class App(QWidget):
    x = 400
    y = 100
    width = 800
    height = 600

    def __init__(self) -> None:
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle('Pencil drawing')
        self.move(App.x, App.y)
        self.resize(App.width, App.height)
        self.show()

# gui 생성
app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())   # 앱이 종료될 떄까지 대기