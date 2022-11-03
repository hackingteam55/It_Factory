import unittest2
from time import sleep
from unittest2 import TestCase
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Test(TestCase):


    # elementele din pagina
    # in loc sa le scriem de n ori in teste, le trecem aici o sg data
    SUBMIT_BTN = (By.XPATH, '//a[@role="button"]')
    FIRST_NAME_INPUT = (By.XPATH, '//input[@id="first-name"]')
    LAST_NAME_INPUT = (By.XPATH, '//input[@id="last-name"]')
    MESSAGE = (By.XPATH, '//div/div[@class="alert alert-success"]')
    JOB_TITLE = (By.XPATH, '//input[@id="job-title"]')
    HIGH_SCHOOL_BTN = (By.XPATH, "xpath pt HighSchool button")
    COLLEGE_BTN = (By.XPATH, "xpath pt HighSchool button")
    GRAD_SCHHOL_BTN = (By.XPATH, "xpath pt HighSchool button")
    MALE_CHEKBOX = (By.XPATH, "xpath pt HighSchool button")
    FEMALE_CHECKBOX = (By.XPATH, "xpath pt HighSchool button")
    NOTHING_TOSAY_CHECKBOX = (By.XPATH, "xpath pt HighSchool button")
    YRS_OF_EXP = (By.XPATH, "xpath pt HighSchool button")
    DATE_SELECT = (By.XPATH, "xpath pt HighSchool button")
    SELECT_OPTION = (By.XPATH, "xpath pt HighSchool button")
    COOKIES_CHOICE_BTN = (By.XPATH, "xpath pt HighSchool button")
    # se rulaza inainte de fiecare test si are rolul de a face setupul de chrome inainte de fiecare test
    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://formy-project.herokuapp.com/form')

    def tearDown(self) -> None:
        self.chrome.quit()


    def test_check_url(self):
        actual = self.chrome.current_url
        expected = 'https://formy-project.herokuapp.com/form'
        self.assertEqual(actual, expected, 'Pagina deschisa nu este corecta')

    def test_element_visible(self):
        self.chrome.find_element(*self.SUBMIT_BTN).click()
        message = self.chrome.find_element(*self.MESSAGE)
        self.assertTrue(message.is_displayed(), 'Mesajul afisat este corect')


    def test_form(self):
        WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located((By.ID, "cookiedismiss"))).click()
        input_first_name = self.chrome.find_element(*self.FIRST_NAME_INPUT)
        input_first_name.send_keys('Matei')
        self.assertTrue(input_first_name.is_displayed(), 'Mesajul afisat este corect')
        sleep(1)
        self.chrome.find_element(*self.LAST_NAME_INPUT).send_keys('Oltean')
        sleep(1)
        self.chrome.find_element(*self.JOB_TITLE).send_keys('Tester')
        sleep(1)
        self.chrome.find_element(*self.HIGH_SCHOOL_BTN).click()
        sleep(1)
        self.chrome.find_element(*self.MALE_CHEKBOX).click()
        sleep(1)
        self.chrome.find_element(*self.SELECT_OPTION).click()
        sleep(1)
        # selectam una dintre optiunile valabile
        sleep(1)
        # date picker click
        sleep(1)
        # select the date
        sleep(1)
        self.chrome.find_element(*self.SUBMIT_BTN).click()


