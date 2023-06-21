import random
import configparser
import datetime
from ui.passgen_ui import Ui_Form
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType('ui/passgen.ui')

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
cfg = configparser.ConfigParser()

# Generatepassword by S-Mamashin

def generator(length):
    allow = "1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ"
    password = "".join(random.choice(allow) for c in range(length) )
    time = datetime.datetime.now(tz=None)

    reg_password = open('C:/dev/projects/PassGenerator/source/passwords.txt', 'a+')
    reg_password.write(f'\n\nПароль: {password} , был сгенерирован: {time}') 

    line_edit = form.lineEdit.setText(password), form.label.setText(f"Сгенерирован пароль из {length} символов!"), form.label_3.setText(f"Последний пароль: {password}")

    return line_edit

form.pushButton.clicked.connect(lambda: generator(16))
form.pushButton_2.clicked.connect(lambda: generator(8))
form.pushButton_3.clicked.connect(lambda: generator(32))
form.pushButton_4.clicked.connect(lambda: generator(16))

app.exec()
