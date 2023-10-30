import csv
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re


def getShoppingList(driver, name):
    URL = f"https://search.shopping.naver.com/search/all?query={name}"

    driver.get(URL)

    bodyElement = driver.find_element(By.TAG_NAME, "body")
    last_height = driver.execute_script("return document.body.scrollHeight")

    scroll_down = 0
    while True:
        bodyElement.send_keys(Keys.PAGE_DOWN)
        # 이렇게도 쓸 수 있음- driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(0.2)
        scroll_down += 1

        new_height = driver.execute_script("return window.scrollY")
        if new_height == last_height:
            print(f"{scroll_down}번: 끝에 도달")
            break

        last_height = new_height

    ul = driver.find_element(
        By.CLASS_NAME, "basicList_list_basis__uNBZx").find_element(By.TAG_NAME, "div")

    html_content = ul.get_attribute('innerHTML')
    soup = BeautifulSoup(html_content, 'html.parser')
    divs = soup.find_all('div', class_=re.compile(".*product_item.*"))

    list = [['이미지', '이름', '주소']]

    for div in divs:
        try:
            img = div.find('a', class_='thumbnail_thumb__Bxb6Z')['href']
            print(img)
            title = div.find('a', class_='product_link__TrAac').get_text()
            print(title)
            price = div.find('span', class_='price').find(
                'em').get_text()
            print(price)
            list.append([img, title, price])

        except AttributeError:
            print('데이터 없음')
            continue

    driver.close()

    with open('네이버쇼핑_리스트.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in list:
            writer.writerow(row)
