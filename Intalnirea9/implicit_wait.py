# pip install selenium
# pip install webdriver-manager

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
# maximizam fereastra
chrome.maximize_window()

# setam implicit wait
# selenium va cauta toate elementele timp de x secunde dupa care va da eroare

chrome.implicitly_wait(10)

# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/form')

# elementul e gasit - aka id valid
# chrome.find_element(By.ID, 'first-name').send_keys('Matei')

# elementul nu e gasit - aka id invalid
chrome.find_element(By.ID, 'first-name123').send_keys('Matei')

# inchidem chrome
# chrome.close()

# de citit
# https://www.geeksforgeeks.org/implicit-waits-in-selenium-python/

