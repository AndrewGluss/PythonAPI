import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_searsh_qa():
    link = 'https://www.yandex.ru/'

    try:
        browser = webdriver.Chrome()
        # browser.implicitly_wait(5)
        browser.get(link)

        yandex_search = browser.find_element(By.NAME, "text")
        # yandex_search = browser.find_element(By.ID, "text")
        # yandex_search = browser.find_element(By.TAG_NAME, "input")
        # yandex_search = browser.find_element(By.XPATH, "//input[@id = 'text']")
        yandex_search.send_keys('Planet for me' + Keys.ENTER)

        # links = browser.find_elements(By.CSS_SELECTOR, '#search-result > .serp-item a.link > b')
        links = browser.find_elements(By.TAG_NAME, 'a')
        count_links = 0
        for lnk in links:
            if lnk.get_attribute('href') == 'https://planetfor.me/':
                count_links += 1
        if count_links > 0:
            browser.get('https://planetfor.me/')


        # planet_search = browser.find_element(By.XPATH, "//input[@type='search']")
        # planet_search = browser.find_element(By.TAG_NAME, "input")
        # browser.find_element(By.XPATH, '//input[@data-qa="navbar-search-input"]')
        planet_search = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.TAG_NAME, "input"))
        )
        planet_search.send_keys('qa' + Keys.ENTER)
        '''
        На данном этапе у меня не прогружаются страница с результатами поиска запроса и тест закрывается.
        Если не ошибаюсь, то можно решить эту проблему с помощью DesiredCapability, но моих знаний не достаточно. Постараюсь заполнить пробелы.
        Решил посмотреть в DevTools какой json приходит в ответе на запрос и уже проходя циклом проверял есть ли qa  в теле json.
        '''

        qa_request = requests.get('https://api.pfm.team/v9/search/global?page=0&inquiry=qa')
        assert qa_request.status_code == 200, \
        "Something wrong"

        count_qa = 0
        for i in qa_request.json()["data"]["documents"]:
            if "qa" in i["user"]["login"]:
                count_qa += 1
        print("\nКоличество результатов где есть 'qa': ", count_qa)
        assert count_qa > 0, \
        "Not Found"

    finally:
        time.sleep(10)
        browser.quit()


if "__name__" == "__main__":
    pytest.main()