# exemplu cu pipe
# exemplu de parent ::
# frate anterior sau de dupa
# functia



# exemmplu de parinte

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
# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/form')

# exemplu cu parinte - aka parintele la label = strong
# text1 = chrome.find_element(By.XPATH, '//form//label[text()="First name"]/parent::strong')
# text1.screenshot('strong.png')


# exemplu cu pipe - pipe reprezinta " | " care tine locul de sau
# text2 = chrome.find_element(By.XPATH, '//input[@id="last-name"] | //input[@id="last-name2"] | //input[@id="last-name3"]')
# # text2.send_keys('Test Auto2')
# # text2.screenshot('testauto2.png')


#exemplu cu or
# text3 = chrome.find_element(By.XPATH, '//input[@id="last-name"]' or '//input[@id="last-name2"]' or '//input[@id="last-name3"]')
# text3.send_keys('Test Auto3')
# text3.screenshot('testauto3.png')


#exemplu frate
# text1 = chrome.find_element(By.XPATH, '//form//label[text()="First name"]/parent::*/following-sibling::input')
# //form//label[text()="First name"]/parent::* = reprezinta strong-ul
# /following-sibling::input = fratele lui strong


# text1 = chrome.find_element(By.XPATH, '//form//label[text()="First name"]/parent::*/following-sibling::input/preceding-sibling::strong')
# aici m-am "intors" la "fratele" strong al lui input - e o "porcarie" la baza, dar pentru a demonstra proprietatile "fratilor"


# exemplu de functie
def formy_input_by_placeholder(placeholder_text, input_value): # parametru - placeholder_text, input_value
    my_input = chrome.find_element(By.XPATH, f'//input[@placeholder="{placeholder_text}"]') # cautam dupa placeholder text
    my_input.send_keys(input_value)


formy_input_by_placeholder('Enter first name', 'Aladin') # apelez functia cu 'Enter first name' ca si placeholder text si vreau sa scriu Aladin
sleep(3)
formy_input_by_placeholder('Enter last name', 'SALAM') # aici scriu SALAM
sleep(3)
formy_input_by_placeholder('Enter your job title', 'QA AUTOMATION')
sleep(3)


