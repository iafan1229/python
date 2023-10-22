from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)


def getIndeedData(lang, pageCount):
    URL = f"https://kr.indeed.com/jobs?q={lang}&start={pageCount}"

    driver.get(url=URL)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")

    # 원하는 태그(예: div)를 가져오기
    content = soup.find(name='div', id='mosaic-provider-jobcards')
    if content is None:
        return
    # 직계 자식 li 태그만 가져오기
    li_elements = content.find('ul').find_all(
        name='li', recursive=False)

    result_list = []  # 결과를 저장할 리스트

    # 가져온 li 태그 출력
    for li in li_elements:
        try:
            aTag = li.find('h2').find('a')
            href = aTag['href']
            jobTitle = aTag.find('span').get('title')
            companyInfos = li.find('div', 'companyInfo')
            result_dict = {'jobTitle': jobTitle, 'href': href, 'companyName': companyInfos.find(
                'span', _class='companyName'), 'location': companyInfos.find('span', _class='companyLocation')}
            result_list.append(result_dict)  # 딕셔너리를 리스트에 추가
        except AttributeError:
            continue  # 예외가 발생하면 건너뛰기

    return (result_list)
