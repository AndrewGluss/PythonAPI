import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


desired_capabilities = {"platformName": "Android",
                        "platformVersion": "13",
                        "deviceName": "Android Emulator",
                        "app": "path/to/the/downloaded/apk"
}
def test_mobile_search():
    try:
        # соединяемся с appium через локальный сервер
        driver = webdriver.Remote('http://localhost:xxxx/wd/hub', desired_capabilities=desired_capabilities)

        # для определения локаторов приложения на андройде используем приложение UI Automator

        driver.implicitly_wait(5)

        login_input = driver.find_element(By.ID, 'resourced_id')
        login_input.send_keys("login")

        password_input = driver.find_element(By.ID, 'resourced_id')
        password_input.send_keys("password")

        sign_in_button = driver.find_element(By.ID, 'resourced_id')
        sign_in_button.click()

        search_button = driver.find_element(By.ID, 'resourced_id')
        sign_in_button.click()

        search_field = driver.find_element(By.ID, 'resourced_id')
        search_field.send_keys("Москва" + Keys.ENTER)

        # получаем список элементов по запросу Москва
        results = driver.find_elements(By.ID, 'resourced_id')
        count_result = 0
        for result in results:
            if "Москва" in result.text:
                count_result += 1
        assert count_result > 0, "Expected Москва in results"
        print('Количество результатов поиска по "Москва": ', count_result)


    finally:

        driver.quit()

if "__name__" == "__main__":
    pytest.main()
