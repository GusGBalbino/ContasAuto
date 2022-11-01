from selenium import webdriver
from selenium.webdriver.common.keys import Keys



#1° Teste - Receber boleto da faculdade



email_u = input("Digite seu email: ")
senha_u = input("Digite sua senha: ")


driver = webdriver.Chrome("C:/Users/gusta/OneDrive/Área de Trabalho/CDriver/chromedriver.exe")

driver.get("https://www.ea.uniceub.br")

user_input = driver.find_element("name", "coAcesso")
password_input = driver.find_element("name", "coSenha")

user_input.send_keys(email_u) #Digitar email
password_input.send_keys(senha_u) #Digitar senha

password_input.send_keys(Keys.RETURN)
