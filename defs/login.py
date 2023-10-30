from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyautogui
import pyperclip


def login(id, password):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    driver.get(
        url='https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/')

    idInput = driver.find_element(By.ID, "id")
    idInput.click()
    pyperclip.copy(id)
    pyautogui.hotkey('ctrl', 'v')
    sleep(2)

    pwInput = driver.find_element(By.ID, "pw")
    pwInput.click()
    pyperclip.copy(password)
    pyautogui.hotkey('ctrl', 'v')
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".btn_login").send_keys(Keys.ENTER)
    return driver
    # driver.close()
