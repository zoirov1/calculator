from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget

calcu = QApplication([])
#oyna
window = QWidget()
window.setGeometry(500,500,280,350)
window.setStyleSheet('background-color:white;')

# functions

# clear all

def cle():
    stage.setText('')

#  right 

def rig():
    stage.setText(f"{stage.text()})")

# left

def lef():
    stage.setText(f"{stage.text()}(")

# nine

def nin():
    stage.setText(f"{stage.text()}9")

# eight

def eig():
    stage.setText(f"{stage.text()}8")

# seven

def seve():
    stage.setText(f"{stage.text()}7")

# six

def si():
    stage.setText(f"{stage.text()}6")

# five

def fiv():
    stage.setText(f"{stage.text()}5")

# four

def fou():
    stage.setText(f"{stage.text()}4")

# three

def thr():
    stage.setText(f"{stage.text()}3")

# two

def tw():
    stage.setText(f"{stage.text()}2")

# one

def on():
    stage.setText(f"{stage.text()}1")



# addition

def add():
    stage.setText(f"{stage.text()}+")

# subtraction

def sub():
    stage.setText(f"{stage.text()}-")

# division

def di():
    stage.setText(f"{stage.text()}/")

# multiply

def mul():
    stage.setText(f"{stage.text()}*")

# back

def ba():
    stage.setText(f"{stage.text()[:-1:]}")

# zero

def ze():
    stage.setText(f"{stage.text()}0")


# operation

def equ():
    try:
       stage.setText(f"{eval(stage.text())}") 

    except:
        stage.setText('error')


    

#stage

stage = QLabel(window)
stage.setGeometry(0,0,240,70)
stage.setStyleSheet('background-color:white;color:#18122B;font-size:35px;padding-top:10px;')
stage.setAlignment(Qt.AlignRight)


# 0 

zero = QPushButton(window)
zero.setText('0')
zero.setGeometry(0,70,70,50)
zero.setStyleSheet('background-color:#18122B;color:white;font-size:25px')
zero.clicked.connect(ze)

# =

equal = QPushButton(window)
equal.setText('=')
equal.setGeometry(71,70,70,50)
equal.setStyleSheet('background-color:#18122B;color:white;font-size:25px;padding-bottom:8px')
equal.clicked.connect(equ)

# back

back = QPushButton(window)
back.setText('«««')
back.setGeometry(142,70,70,50)
back.setStyleSheet('background-color:#18122B;color:white;font-size:25px;padding-bottom:8px;')
back.clicked.connect(ba)

# ÷

divis = QPushButton(window)
divis.setText('÷')
divis.setGeometry(213,70,70,50)
divis.setStyleSheet('background-color:gold;color:#18122B;font-size:25px;padding-bottom:8px;')
divis.clicked.connect(di)

# x

multi = QPushButton(window)
multi.setText('x')
multi.setGeometry(213,121,70,50)
multi.setStyleSheet('background-color:gold;color:#18122B;font-size:25px;padding-bottom:8px;')
multi.clicked.connect(mul)

# +

addi = QPushButton(window)
addi.setText('+')
addi.setGeometry(213,172,70,50)
addi.setStyleSheet('background-color:gold;color:#18122B;font-size:25px;padding-bottom:8px;')
addi.clicked.connect(add)

# -

subt = QPushButton(window)
subt.setText('-')
subt.setGeometry(213,223,70,50)
subt.setStyleSheet('background-color:gold;color:#18122B;font-size:25px;padding-bottom:8px;')
subt.clicked.connect(sub)

# 1

one = QPushButton(window)
one.setText('1')
one.setGeometry(0,121,70,50)
one.setStyleSheet('background-color:#18122B;color:white;font-size:25px;')
one.clicked.connect(on)

# 2

two = QPushButton(window)
two.setText('2')
two.setGeometry(71,121,70,50)
two.setStyleSheet('background-color:#18122B;color:white;font-size:25px;')
two.clicked.connect(tw)

# 3
 
three = QPushButton(window)
three.setText('3')
three.setGeometry(142,121,70,50)
three.setStyleSheet('background-color:#18122B;color:white;font-size:25px;')
three.clicked.connect(thr)

# 4

four = QPushButton(window)
four.setText('4')
four.setGeometry(0,172,70,50)
four.setStyleSheet('background-color:#18122B;color:white;font-size:25px;')
four.clicked.connect(fou)

# 5

five = QPushButton(window)
five.setText('5')
five.setGeometry(71,172,70,50)
five.setStyleSheet('background-color:#18122B;color:white;font-size:25px;')
five.clicked.connect(fiv)

# 6

six = QPushButton(window)
six.setText('6')
six.setGeometry(142,172,70,50)
six.setStyleSheet('background-color:#18122B;color:white;font-size:25px;')
six.clicked.connect(si)

# 7

seven = QPushButton(window)
seven.setText('7')
seven.setGeometry(0,223,70,50)
seven.setStyleSheet('background-color:#18122B;color:white;font-size:25px;')
seven.clicked.connect(seve)

# 8 

eight = QPushButton(window)
eight.setText('8')
eight.setGeometry(71,223,70,50)
eight.setStyleSheet('background-color:#18122B;color:white;font-size:25px;')
eight.clicked.connect(eig)

# 9

nine = QPushButton(window)
nine.setText('9')
nine.setGeometry(142,223,70,50)
nine.setStyleSheet('background-color:#18122B;color:white;font-size:25px;')
nine.clicked.connect(nin)

# (

left = QPushButton(window)
left.setText('(')
left.setGeometry(0,274,70,50)
left.setStyleSheet('background-color:#18122B;color:white;font-size:25px;')
left.clicked.connect(lef)

# )

right = QPushButton(window)
right.setText(')')
right.setGeometry(71,274,70,50)
right.setStyleSheet('background-color:#18122B;color:white;font-size:25px;')
right.clicked.connect(rig)

# Ac

ac = QPushButton(window)
ac.setText('AC')
ac.setGeometry(142,274,140,50)
ac.setStyleSheet('background-color:#18122B;color:white;font-size:25px;')
ac.clicked.connect(cle)





window.show()
calcu.exec_()
