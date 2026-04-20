import secrets
import string
import pyperclip
from PyQt6 import QtWidgets
import sys
import os
import stat
import requests
def main():
    try:
     alphabet = string.ascii_letters + string.digits
     password = ''.join(secrets.choice(alphabet) for i in range(12))
     msg = QtWidgets.QMessageBox()
     msg.setWindowTitle("Пароль сгенерирован")
     msg.setText(f"Ваш пароль: {password}")
     msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
     msg.exec()
     pyperclip.copy(password)
     name = os.path.expandvars(rf"%userprofile%\passwordbase.txt")
     with open(name,"a",encoding="utf-8") as f1:
         print(fr"User: {requests.get(r'https://api.ipify.org').text} , Сгенерированный пароль: {password}", end="\n" , file=f1,flush=True)
    except Exception as e:
        print(f"Ошибка {e}")
def add_pass():
 try:
  with open(os.path.expandvars(r"%USERPROFILE%\desktop\YOUR_PASS.txt"),"a",encoding="utf-8") as f5:
              print(fr"Соцсеть: {input3.text()}, Пароль: {input2.text()}", "\n",file=f5,flush=True)
              input2.clear()
              input3.clear()
  path = os.path.expandvars(r"%USERPROFILE%\desktop\YOUR_PASS.txt")
  if os.path.exists(path):
    os.chmod(path, stat.S_IWRITE)
 except Exception as e:
  print(f"Ошибка:{e}") 
def clean_file():
     path2 = os.path.expandvars(r"%USERPROFILE%\desktop\YOUR_PASS.txt")
     with open(path2,"w") as f9:
        f9.write("")
def show_pass():
     path3 = os.path.expandvars(r"%USERPROFILE%\desktop\YOUR_PASS.txt")
     os.system(rf"notepad.exe {path3}")
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('PasswordDog')
window.show()
window.resize(500,500)
button = QtWidgets.QPushButton('Сгенерировать пароль')
button.clicked.connect(main)
input2 = QtWidgets.QLineEdit('Введите пароль')
input3 = QtWidgets.QLineEdit('Введите название соцсети от пароля')
button2 = QtWidgets.QPushButton('Создать файл на рабочем столе с паролем')
button3 = QtWidgets.QPushButton('Очистить файл на рабочем столе с паролем')
button4 = QtWidgets.QPushButton('Показать пароли')
button4.clicked.connect(show_pass)
button3.clicked.connect(clean_file)
layout = QtWidgets.QVBoxLayout()
layout.addWidget(button)
layout.addWidget(button2)
layout.addWidget(input2)
layout.addWidget(input3)
button2.clicked.connect(add_pass)
layout.addWidget(button3)
layout.addWidget(button4)
window.setLayout(layout)
sys.exit(app.exec())
