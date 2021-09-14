from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

navegador = webdriver.Chrome()
navegador.maximize_window()
navegador.get('https://github.com/login')

Username_login = 'seu email'
Senha_login = 'sua senha'

campo_username = navegador.find_element_by_css_selector('#login_field')
sleep(1)
campo_username.send_keys(Username_login)
campo_senha = navegador.find_element_by_css_selector('#password')
sleep(2)
campo_senha.send_keys(Senha_login)
sleep(2)

navegador.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]').click()



