import email
from multiprocessing.reduction import send_handle
import socket
import selenium.webdriver as drv
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from time import sleep
import PyQt5

def captura_login():
    global email
    global senha 
    
    email = Dialog.edit_email.text()
    senha = Dialog.edit_senha.text()
    
    Dialog.edit_email.setText("")
    Dialog.edit_senha.setText("")
    Dialog.close()
    
app = QApplication([])
Dialog = uic.loadUi("login.ui") #Erro aqui
Dialog.btn_logar.clicked.connect(captura_login)
Dialog.show()
Dialog.edit_email.setfocus()

app.exec()

driver = drv.Chrome()

trying = 0
while trying == 0:
    ip = socket.gethostbyname(socket.gethostname())
    if ip == "127.0.0.1":
        print("Sem conexão com a internet. \n")
        print("Tentando novamente em 5 segundos...\n")
        sleep(5)
    else:
        print("\n \n Internet disponível... \n Conectando agora...")
        trying = 1
        
driver.get("https://www.ea.uniceub.br")

cx_email = driver.find_element_by_name("coAcesso")
cx_email.click()
cx_email.send_keys(email)

cx_senha = driver.find_element_by_name("coSenha")
cx_senha.click()
cx_senha.send_keys(senha  + "{ENTER}")




    
