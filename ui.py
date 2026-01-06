from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QPlainTextEdit, QHBoxLayout) 
from PyQt5.QtGui import QIcon

class View(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.te1 = QPlainTextEdit() 
        self.te1.setReadOnly(True) 

        self.btn1 = QPushButton('Message', self)
        self.btn2 = QPushButton('Clear', self) 

        hbox = QHBoxLayout() 
        hbox.addStretch(1) 
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)

        vbox = QVBoxLayout() 
        vbox.addWidget(self.te1) 
        vbox.addLayout(hbox) 
        vbox.addStretch(1) 

        self.setLayout(vbox) 

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png')) 
        self.resize(256, 256)
        self.show()

    def activateMessage(self): # 버튼을 클릭할 때 동작하는 함수 : 메시지 박스 출력
        self.te1.appendPlainText("Button clicked!")

    def clearMessage(self):  # 버튼2 핸들러 함수
        self.te1.clear()