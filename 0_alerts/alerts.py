import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC


@pytest.fixture
def browser():
    # wd = webdriver.Chrome()
    wd = webdriver.Firefox()
    yield wd
    wd.quit()


def test_example(browser):
    browser.get("https://otus.ru/")
    browser.execute_script("alert('123');")
    time.sleep(2)
    WebDriverWait(browser, 10).until(EC.alert_is_present())
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)
    alert.accept()

    browser.execute_script("prompt('Type some stuff');")
    time.sleep(2)
    prompt = browser.switch_to.alert
    # Для хрома не работает
    prompt.send_keys('Helllo')
    time.sleep(2)
    prompt.dismiss()

    browser.execute_script("confirm('Are You Ok?');")
    time.sleep(2)
    confirm = browser.switch_to.alert
    print(confirm.text)
    confirm.accept()
