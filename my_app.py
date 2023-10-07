from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, QGridLayout, 
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *
from second_win import *

       
class MainWin(QWidget):
    def __init__(self):
        ''' the window which the greeting is located in '''
        super().__init__()

        '''apelarea metodei care creaza si configureaza elementele grafice'''
        self.initUI()
        
        '''apelul metodei care leaga partea vizuala (exemplu butonul) de 
           partea functionala (functia care se executa la apasarea butonului)'''
        self.connects()

        '''sets the window appearance (label, size, location)'''
        self.set_appear()
        
        '''start:'''
        self.show()

    ''' crearea, configurarea si adaugarea in interfata a elementelor grafice
        precum texte si butoane '''
    def initUI(self):
        self.btn_next = QPushButton(txt_next)
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)
        self.layout = QVBoxLayout()
        self.hello_text.addWidget(self.layout)
        self.instruction.addWidget(self.layout)
        self.button.addWidget(self.layout)
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        #adauga in panou Qlabelul instruction aliniat la stanga
        #adauga in panou Qbutonul next aliniat pe centru      
        self.setLayout(self.layout_line)

    '''functia care este declansata la apasarea butonului next'''
    def next_click(self):
        '''in aceasta functie trebuie sa instantiem (cream) fereastra a2-a'''
        '''numele clasei care creaza feastra a2-a o gasiti in fisierul secon_win.py'''
        self.tw = TestWin()
        self.hide() #aceasta instructiune ascunde fereastra actuala pt a face loc pt cea noua
    
    def connects(self):
        '''functia care conecteaza butonul de functia next_click'''
        self.btn_next.clicked.connect(self.set_appear)

    def set_appear(self):
        '''functia care seteaza aparenta ferestrei (titlu, dimensiune, pozitia pe ecran)'''
        '''in fisierul instr.py gasiti numele variabilelor in care sunt tinute titlul, latimea, lungimea si pozitia ferestrei'''
        self.setWindowTitle("Helth")
        self.resize(800, 500)
        self.move(win_x, win_y)

app = QApplication([])
mw = MainWin()
app.exec_()
