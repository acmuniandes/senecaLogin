from selenium import webdriver
import os

def connect():
    browser = webdriver.Chrome('chromedriver')
    url = "http://wlan.uniandes.edu.co"
    browser.get(url)

    usuario = browser.find_element_by_name('username')
    usuario.send_keys('i.gomez10')

    lacontrasena = os.environ.get('CONTRASENA')

    contrasena = browser.find_element_by_name('password')
    contrasena.send_keys( lacontrasena )

    btnSubmit = browser.find_element_by_name("Submit")
    btnSubmit.click()

    # browser.submit()



connect()
