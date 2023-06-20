import random
from ui.pasgen_ui import Ui_Form
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication



Form, Window = uic.loadUiType('C:/dev/projects/passgenerator/ui/passgen.ui')


app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

# Generate 16x / default password by S-Mamashin
def default():
    password = ""
    all_kinds = "1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ" 

    for a in range(16): 

        password = password + random.choice(list(all_kinds)) 

    return form.lineEdit.setText(password), form.label.setText("Сгенерирован пароль из 16-ти символов!") 


def gen_8():

    password_8 = ""
    all_kinds_8 = "1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ" 

    for a in range(8): 

        password_8 = password_8 + random.choice(list(all_kinds_8))  
       
    return form.lineEdit.setText(password_8), form.label.setText("Сгенерирован пароль из 8 символов!") 

def gen_32():

    password_32 = ""
    all_kinds_32 = "1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ" 

    for a in range(32): 

        password_32 = password_32 + random.choice(list(all_kinds_32)) 

    return form.lineEdit.setText(password_32), form.label.setText("Сгенерирован пароль из 32-х символов!") 



form.pushButton.clicked.connect( default )
form.pushButton_2.clicked.connect( gen_8 )
form.pushButton_4.clicked.connect( default )
form.pushButton_3.clicked.connect( gen_32 )
    

app.exec()