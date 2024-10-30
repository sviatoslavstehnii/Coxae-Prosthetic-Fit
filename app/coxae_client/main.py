from PyQt6.QtWidgets import QMainWindow, QApplication
import sys
import requests


class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Drag and Drop")
        self.resize(720, 480)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        dropped_files = [u.toLocalFile() for u in event.mimeData().urls()]
        obj = {"file": dropped_files[0]}
        x = requests.post("http://127.0.0.1:8000/api/v1/process/", files = {"image": ("image.jpg", "")})
        print(x.text)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWidget()
    ui.show()
    sys.exit(app.exec())