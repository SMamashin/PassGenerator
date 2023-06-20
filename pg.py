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

# Generatepassword by S-Mamashin

def generator(length):
    allow = "1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ"
    password = "".join(random.choice(allow) for c in range(length) ) 

    return form.lineEdit.setText(password), form.label.setText(f"Сгенерирован пароль из {length} символов!") 

form.pushButton.clicked.connect(lambda: generator(16))
form.pushButton_2.clicked.connect(lambda: generator(8))
form.pushButton_3.clicked.connect(lambda: generator(32))
form.pushButton_4.clicked.connect(lambda: generator(16))

app.exec()