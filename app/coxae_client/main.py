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
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/91.0.4472.124 Safari/537.36 '
        }
        with open(dropped_files[0], 'rb') as image:
            files = {'file': image.read()}
        x = requests.post("http://127.0.0.1:8000/uploadfile",headers=headers, files=files)
        print(x.text)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWidget()
    ui.show()
    sys.exit(app.exec())