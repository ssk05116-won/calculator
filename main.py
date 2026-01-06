# ch 4.2.1 main.py
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QPlainTextEdit, QHBoxLayout) 
from PyQt5.QtGui import QIcon
    
class Calculator(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.te1 = QPlainTextEdit() # 텍스트 에디트 위젯 생성
        self.te1.setReadOnly(True) # 텍스트 에디트 위젯을 읽기만 가능하도록 수정

        self.btn1 = QPushButton('Message', self) # 버튼추가
        self.btn1.clicked.connect(self.activateMessage) # 버튼 클릭시 핸들러 함수 연결

        self.btn2 = QPushButton('Clear', self) # 버튼 추가
        self.btn2.clicked.connect(self.clearMessage) # 버튼 핸들러 함수 연결

        hbox = QHBoxLayout() # 수평 레이아웃 위젯 생성
        hbox.addStretch(1) # 빈공간
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)

        vbox = QVBoxLayout() # 수직 레이아웃 위젯 생성
        vbox.addWidget(self.te1) # 빈공간
        #vbox.addWidget(self.btn1) # 버튼위치
        vbox.addLayout(hbox) # 버튼1 위치에 hbox를 배치
        vbox.addStretch(1) # 빈공간

        self.setLayout(vbox) # 빈공간 - 버튼 - 빈공간 순으로 수직 배치된 레이아웃 설정

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png')) # 윈도 아이콘 추가
        self.resize(256, 256)
        self.show()

    def activateMessage(self): # 버튼을 클릭할 때 동작하는 함수 : 메시지 박스 출력
        QMessageBox.information(self, "information", "Button clicked!")

    def clearMessage(self):  # 버튼2 핸들러 함수
        self.te1.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    sys.exit(app.exec_())